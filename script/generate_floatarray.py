import os
import math

def generate_core_getset_functions():
    """Generates the shared core get/set functions (binary tree approach)"""
    
    # Base wrapper functions that do the actual getting/setting
    core = """# ===== CORE GET/SET WRAPPERS =====
# These are shared by all array sizes

com_floatarray_get = {
	# Base get function - requires var:INDEX to be an integer
	set_variable = { name = returned value = var:z_fa_$NAME$_$INDEX$ }
}

com_floatarray_set = {
	# Base set function - requires var:INDEX to be an integer and var:VALUE
	set_variable = { name = z_fa_$NAME$_$INDEX$ value = var:VALUE }
}

"""
    
    # Generate binary tree levels: getset_1, getset_2, getset_4, getset_8, getset_16, getset_32
    for level in [1, 2, 4, 8, 16, 32]:
        if level == 1:
            # Level 1: direct call to base get/set
            core += f"""com_floatarray_getset_{level} = {{
	if = {{
		limit = {{ var:INDEX <= $LOWER_0$ }}
		com_floatarray_$GETSET$ = {{ NAME = $NAME$ INDEX = $LOWER_0$ }}
	}}
	else = {{
		com_floatarray_$GETSET$ = {{ NAME = $NAME$ INDEX = $UPPER_0$ }}
	}}
}}

"""
        else:
            # Higher levels: call the previous level
            prev_level = level // 2
            num_pairs = level // 2
            
            core += f"""com_floatarray_getset_{level} = {{
	if = {{
		limit = {{ var:INDEX <= $UPPER_{num_pairs - 1}$ }}
		com_floatarray_getset_{prev_level} = {{
			NAME = $NAME$
			GETSET = $GETSET$
"""
            # Add parameters for first half
            for i in range(num_pairs):
                core += f"\t\t\tLOWER_{i} = $LOWER_{i}$ UPPER_{i} = $UPPER_{i}$\n"
            
            core += """\t\t}
	}
	else = {
		com_floatarray_getset_""" + str(prev_level) + """ = {
			NAME = $NAME$
			GETSET = $GETSET$
"""
            # Add parameters for second half
            for i in range(num_pairs):
                core += f"\t\t\tLOWER_{i} = $LOWER_{i + num_pairs}$ UPPER_{i} = $UPPER_{i + num_pairs}$\n"
            
            core += """\t\t}
	}
}

"""
    
    return core

def generate_foreach_core():
    """Generates a single size-agnostic foreach core function"""
    return """com_floatarray_foreach_core = {
	set_variable = { name = VALUE value = var:z_fa_$NAME$_$IND$ }
	set_variable = { name = INDEX value = $IND$ }
	$BODY$ = { }
	set_variable = { name = z_fa_$NAME$_$IND$ value = var:VALUE }
}

"""

def generate_foreach(length):
    """Generates foreach function for a specific length"""
    
    core = f"""com_floatarray_{length}_foreach = {{
	# Requires: $NAME$ (array name), $BODY$ (scripted effect to execute per element)
	# Sets var:INDEX and var:VALUE for each iteration
"""
    
    for i in range(length):
        core += f"\tcom_floatarray_foreach_core = {{ NAME = $NAME$ IND = {i} BODY = $BODY$ }}\n"
    
    core += "}\n"
    return core

def generate_getset_wrappers(length):
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
    
    get_func = f"""com_floatarray_{length}_get = {{
	# Requires: $NAME$ (array name), var:INDEX (0 to {length-1})
	# Returns: var:returned
	com_floatarray_getset_{core_level // 2} = {{
		NAME = $NAME$
		GETSET = get
"""
    
    set_func = f"""com_floatarray_{length}_set = {{
	# Requires: $NAME$ (array name), var:INDEX (0 to {length-1}), var:VALUE
	com_floatarray_getset_{core_level // 2} = {{
		NAME = $NAME$
		GETSET = set
"""
    
    # Add all parameter pairs
    for idx, (lower, upper) in enumerate(param_pairs):
        get_func += f"\t\tLOWER_{idx} = {lower}\n"
        get_func += f"\t\tUPPER_{idx} = {upper}\n"
        set_func += f"\t\tLOWER_{idx} = {lower}\n"
        set_func += f"\t\tUPPER_{idx} = {upper}\n"
    
    get_func += "\t}\n}\n"
    set_func += "\t}\n}\n"
    
    return get_func + "\n" + set_func

def generate_init_clear(length):
    """Generates initialize and clear functions"""
    
    init = f"""com_floatarray_{length}_initialize = {{
	# Creates z_fa_$NAME$_0 to z_fa_$NAME$_{length-1}
"""
    for i in range(length):
        init += f"\tset_variable = {{ name = z_fa_$NAME$_{i} value = 0 }}\n"
    init += "}\n"
    
    clear = f"""com_floatarray_{length}_clear = {{
	# Deletes all variables in the array
"""
    for i in range(length):
        clear += f"\tremove_variable = z_fa_$NAME$_{i}\n"
    clear += "}\n"
    
    return init + "\n" + clear



def main(sizes=[8, 16, 32], output_file='com_floatarray.txt'):
    
    all_scripts = """# Auto-generated floatarray utilities (Binary Tree System)
# Shared core functions allow multiple array sizes without conflicts
# Array name macro: $NAME$
# Variable prefix: z_fa_
# Variable naming: z_fa_$NAME$_INDEX (e.g., z_fa_mydata_0, z_fa_mydata_1, ...)

"""
    
    # Generate shared core functions ONCE
    all_scripts += generate_core_getset_functions()
    all_scripts += generate_foreach_core()

    # Generate size-specific functions
    for size in sizes:
        all_scripts += f"\n# ===== FLOATARRAY SIZE {size} =====\n\n"
        all_scripts += "# --- FOREACH ---\n"
        all_scripts += generate_foreach(size)
        all_scripts += "\n# --- GET/SET ---\n"
        all_scripts += generate_getset_wrappers(size)
        all_scripts += "\n# --- INITIALIZE & CLEAR ---\n"
        all_scripts += generate_init_clear(size)
    
    # Get script directory and create output file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_file)
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(all_scripts)
    
    # Calculate max nesting depth
    max_size = max(sizes)
    max_depth = math.ceil(math.log2(max_size)) + 1
    
    print(f"""
✓ Successfully generated: {output_path}
  Floatarray sizes: {', '.join(map(str, sizes))}
""")

if __name__ == "__main__":
    main(sizes=[8, 16, 32, 64, 128, 256, 512], output_file='com_floatarray.txt')