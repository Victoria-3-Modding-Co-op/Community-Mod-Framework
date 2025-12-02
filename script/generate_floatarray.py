import os

def generate_binary_search_getset(sizes, array_name_macro="NAME"):
    """Generates the shared core get/set functions (binary tree approach)"""
    
    # Base wrapper functions that do the actual getting/setting
    core = f"""# ===== CORE GET/SET WRAPPERS =====
# These are shared by all array sizes

# Base get function - requires INDEX to be an integer
com_floatarray_get_at = {{
	set_variable = {{ name = com_fa_return value = var:com_fa_${array_name_macro}$_$INDEX$ }}
}}

# Base set function_at - requires INDEX to be an integer and var:com_fa_value to be set
com_floatarray_set = {{
	set_variable = {{ name = com_fa_${array_name_macro}$_$INDEX$ value = var:com_fa_value }}
}}

"""
    max_level = max(sizes)
    levels = []
    level = 512 #handling for up to 512 is already included in CMF
    while level < max_level:
        levels.append(level)
        level *= 2
    # Generate binary tree levels: getset_1, getset_2, getset_4, getset_8, getset_16, getset_32
    for level in levels:
        if level == 1:
            # Level 1: direct call to base get/set
            core += f"""com_floatarray_getset_{level} = {{
	if = {{
		limit = {{ var:com_fa_index < $UPPER_0$ }}
		com_floatarray_$GETSET$_at = {{ {array_name_macro} = ${array_name_macro}$ INDEX = $LOWER_0$ }}
	}}
	else = {{
		com_floatarray_$GETSET$_at = {{ {array_name_macro} = ${array_name_macro}$ INDEX = $UPPER_0$ }}
	}}
}}

"""
        else:
            # Higher levels: call the previous level
            prev_level = level // 2
            num_pairs = level // 2
            
            core += f"""com_floatarray_getset_{level} = {{
	if = {{
		limit = {{ var:com_fa_index <= $LOWER_{num_pairs}$ }}
		com_floatarray_getset_{prev_level} = {{
			{array_name_macro} = ${array_name_macro}$
			GETSET = $GETSET$
"""
            # Add parameters for first half
            for i in range(num_pairs):
                core += f"\t\t\tLOWER_{i} = $LOWER_{i}$ UPPER_{i} = $UPPER_{i}$\n"
            
            core += f"""\t\t}}
	}}
	else = {{
		com_floatarray_getset_{str(prev_level)} = {{
			{array_name_macro} = ${array_name_macro}$
			GETSET = $GETSET$
"""
            # Add parameters for second half
            for i in range(num_pairs):
                core += f"\t\t\tLOWER_{i} = $LOWER_{i + num_pairs}$ UPPER_{i} = $UPPER_{i + num_pairs}$\n"
            
            core += f"""\t\t}}
	}}
}}

"""
    
    return core

def generate_initialize_wrapper(sizes, array_name_macro="NAME"):
    """Generates initialize wrapper effect to call the actual scripted effects"""
    wrapper = f"""
# {array_name_macro} is name of array
# SIZE is array size
com_floatarray_initialize = {{
	switch = {{
		trigger = $SIZE$
"""
    
    for i in sizes:
        wrapper += f"\t\t{i} = {{ com_floatarray_{i}_initialize = {{ {array_name_macro} = ${array_name_macro}$ }} }}\n"

    wrapper += f"""        fallback = {{
            error_log = com_floatarray_size_mismatch
        }}
    }}
}}

"""
    return wrapper

def generate_foreach_core(array_name_macro="NAME"):
    """Generates a single size-agnostic foreach core function"""
    return f"""com_floatarray_foreach_core = {{
	set_variable = {{ name = com_fa_value value = var:com_fa_${array_name_macro}$_$IND$ }}
	set_variable = {{ name = com_fa_index value = $IND$ }}
	$BODY$
	set_variable = {{ name = com_fa_${array_name_macro}$_$IND$ value = var:com_fa_value }}
}}

"""

def generate_foreach(length, array_name_macro="NAME"):
    """Generates foreach function for a specific length"""
    
    core = f"""# Requires: ${array_name_macro}$ (array name), $BODY$ (scripted effect to execute per element)
# Sets var:com_fa_index and var:com_fa_value for each iteration
com_floatarray_{length}_foreach = """ + "{\n"
    
    for i in range(length):
        if i & 1:
            core += f" com_floatarray_foreach_core = {{ {array_name_macro} = ${array_name_macro}$ IND = {i} BODY = $BODY$ }}\n"
        else:
            core += f"\tcom_floatarray_foreach_core = {{ {array_name_macro} = ${array_name_macro}$ IND = {i} BODY = $BODY$ }}"
    
    core += "}\n"
    return core

def generate_getset_wrappers(length, array_name_macro="NAME"):
    """Generates get/set wrapper functions for a specific length"""
    
    # Determine which core function to use (next power of 2)
    core_level = 1
    while core_level < length:
        core_level *= 2
    
    # Generate pairs for this length
    pairs = []
    for i in range(length):
        pairs.append(i)
    
    # Group pairs into the structure needed by the core function
    param_pairs = []
    for i in range(0, len(pairs), 2):
        if i + 1 < len(pairs):
            param_pairs.append((pairs[i], pairs[i + 1]))
        else:
            param_pairs.append((pairs[i], pairs[i]))
    
    get_func = f"""# Requires: ${array_name_macro}$ (array name), var:com_fa_index (0 to {length-1})
# Returns: var:com_fa_return
com_floatarray_{length}_get = {{
	com_floatarray_getset_{core_level // 2} = {{
		{array_name_macro} = ${array_name_macro}$
		GETSET = get
"""
    
    set_func = f"""# Requires: ${array_name_macro}$ (array name), var:com_fa_index (0 to {length-1}), var:com_fa_value
com_floatarray_{length}_set = {{
	com_floatarray_getset_{core_level // 2} = {{
		{array_name_macro} = ${array_name_macro}$
		GETSET = set
"""
    
    # Add all parameter pairs
    for idx, (lower, upper) in enumerate(param_pairs):
        get_func += f"\t\tLOWER_{idx} = {lower} UPPER_{idx} = {upper}\n"
        set_func += f"\t\tLOWER_{idx} = {lower} UPPER_{idx} = {upper}\n"
    
    get_func += f"\t}}\n}}\n"
    set_func += f"\t}}\n}}\n"
    
    return get_func + "\n" + set_func

def generate_init_clear(length, array_name_macro="NAME"):
    """Generates initialize and clear functions"""
    
    init = f"""# Creates com_fa_${array_name_macro}$_0 to com_fa_${array_name_macro}$_{length-1}
com_floatarray_{length}_initialize = {{
"""
    init += f"\tfix_variable_error = {{ variable = com_fa_${array_name_macro}$_size }} set_variable = {{ name = com_fa_${array_name_macro}$_size value = {length} }}\n"
    for i in range(length):
        if i & 1:
            init += f" com_floatarray_initialize_core = {{ {array_name_macro} = ${array_name_macro} INDEX = {i} }}\n"
        else:
            init += f"\tcom_floatarray_initialize_core = {{ {array_name_macro} = ${array_name_macro} INDEX = {i} }}"
    init += "}\n"
    
    clear = f"""# Deletes all variables in the array
com_floatarray_{length}_clear = """ + "{\n"

    clear += f"\tremove_variable = com_fa_${array_name_macro}$_size\n"
    for i in range(length):
        if i & 1:
            clear += f" remove_variable = com_fa_${array_name_macro}$_{i}\n"
        else:
            clear += f"\tremove_variable = com_fa_${array_name_macro}$_{i}"
    clear += f"}}\n"
    
    return init + "\n" + clear



def main(sizes=[8, 16, 32], output_file='com_floatarray.txt'):
    array_name_macro ="NAME"
    all_scripts = f"""# Auto-generated floatarray utilities (Binary Tree System)
# Shared core functions allow multiple array sizes without conflicts
# Array name macro: ${array_name_macro}$
# Variable prefix: com_fa_
# Variable naming: com_fa_${array_name_macro}$_INDEX (e.g., com_fa_mydata_0, com_fa_mydata_1, ...)

"""
    
    # Generate shared core functions ONCE
    all_scripts += generate_initialize_wrapper(sizes, array_name_macro)
    #all_scripts += generate_binary_search_getset(sizes, array_name_macro) #default included in CMF, uncomment for additional sizes
    #all_scripts += generate_foreach_core(array_name_macro) #default included in CMF, uncomment to regenerate

    # Generate size-specific functions
    for size in sizes:
        all_scripts += f"\n# ===== FLOATARRAY SIZE {size} =====\n\n"
        all_scripts += "# --- FOREACH ---\n"
        all_scripts += generate_foreach(size, array_name_macro)
        all_scripts += "\n# --- GET/SET ---\n"
        all_scripts += generate_getset_wrappers(size, array_name_macro)
        all_scripts += "\n# --- INITIALIZE & CLEAR ---\n"
        all_scripts += generate_init_clear(size, array_name_macro)
    
    # Get script directory and create output file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, "com_floatarray_effects.txt")
    
    # Write to file
    with open(output_file, 'w', encoding='utf_8_sig') as f:
        f.write(all_scripts)
        
    print(f"""
✓ Successfully generated: {output_file}
  Floatarray sizes: {', '.join(map(str, sizes))}
""")

if __name__ == "__main__":
    main(sizes=[8, 16, 32, 64, 128, 256, 512])