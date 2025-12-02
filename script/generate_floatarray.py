import os

def generate_binary_search_get(length):
    """Generates binary search for get operation with macro"""
    def generate_range(start, end, indent=1):
        if start == end:
            return f"{'	' * indent}set_variable = {{ name = returned value = var:z_fa_$NAME$_{start} }}\n"
        
        mid = (start + end) // 2
        result = f"{'	' * indent}if = {{\n"
        result += f"{'	' * (indent + 1)}limit = {{ var:INDEX <= {mid} }}\n"
        result += generate_range(start, mid, indent + 1)
        result += f"{'	' * indent}}}\n"
        result += f"{'	' * indent}else = {{\n"
        result += generate_range(mid + 1, end, indent + 1)
        result += f"{'	' * indent}}}\n"
        return result
    
    return generate_range(0, length - 1, 1)

def generate_binary_search_set(length):
    """Generates binary search for set operation with macro"""
    def generate_range(start, end, indent=1):
        if start == end:
            return f"{'	' * indent}set_variable = {{ name = z_fa_$NAME$_{start} value = var:VALUE }}\n"
        
        mid = (start + end) // 2
        result = f"{'	' * indent}if = {{\n"
        result += f"{'	' * (indent + 1)}limit = {{ var:INDEX <= {mid} }}\n"
        result += generate_range(start, mid, indent + 1)
        result += f"{'	' * indent}}}\n"
        result += f"{'	' * indent}else = {{\n"
        result += generate_range(mid + 1, end, indent + 1)
        result += f"{'	' * indent}}}\n"
        return result
    
    return generate_range(0, length - 1, 1)

def generate_foreach(length):
    """Generates foreach iteration using core effect"""
    lines = []
    for i in range(length):
        lines.append(f"\tcom_floatarray_foreach_core = {{ NAME = $NAME$ INDEX = {i} BODY = $BODY$ }}\n")
    return ''.join(lines)

def generate_floatarray(length, array_name_macro="NAME"):
    """Generates complete floatarray scripted effects with macros"""
    
    # Initialize function
    init_lines = [f"\tset_variable = {{ name = z_fa_${array_name_macro}$_{i} value = 0 }}\n" for i in range(length)]
    
    # Clear function
    clear_lines = [f"\tremove_variable = z_fa_${array_name_macro}$_{i}\n" for i in range(length)]
    
    script = f"""# Floatarray with length {length} (using ${array_name_macro}$ macro)
# Usage: Call with {array_name_macro} parameter, e.g., com_floatarray_{length}_initialize = {{ {array_name_macro} = mydata }}

com_floatarray_{length}_initialize = {{
	# Creates z_fa_${array_name_macro}$_0 to z_fa_${array_name_macro}$_{length-1}
{''.join(init_lines)}}}

com_floatarray_{length}_get = {{
	# Requires: ${array_name_macro}$ (array name), var:INDEX (0 to {length-1})
	# Returns: var:returned
{generate_binary_search_get(length)}}}

com_floatarray_{length}_set = {{
	# Requires: ${array_name_macro}$ (array name), var:INDEX (0 to {length-1}), var:VALUE
{generate_binary_search_set(length)}}}

com_floatarray_{length}_foreach = {{
	# Requires: ${array_name_macro}$ (array name), $BODY$ (scripted effect to execute per element)
	# Sets var:INDEX and var:VALUE for each iteration
{generate_foreach(length)}}}

com_floatarray_{length}_clear = {{
	# Deletes all variables in the array
	# Requires: ${array_name_macro}$ (array name)
{''.join(clear_lines)}}}

"""
    return script

def generate_core_effect():
    """Generates the core effect for foreach iteration"""
    return """# Core effect for foreach iteration
# This reduces code repetition significantly
com_floatarray_foreach_core = {
	set_variable = { name = VALUE value = var:z_fa_$NAME$_$INDEX$ }
	set_variable = { name = INDEX value = $INDEX$ }
	$BODY$ = yes
	set_variable = { name = z_fa_$NAME$_$INDEX$ value = var:VALUE }
}

"""

def main(sizes = [8, 16, 32, 64, 128, 256, 512]):
    # Configuration
    array_name_macro = "NAME"  # Change this to customize the macro name
    
    all_scripts = "# Auto-generated floatarray utilities\n"
    all_scripts += "# Generated with binary search for O(log n) performance\n"
    all_scripts += f"# Array name macro: ${array_name_macro}$\n"
    all_scripts += "# Variable prefix: z_fa_\n"
    all_scripts += "# Function prefix: com_\n\n"
    
    # Add core effect first
    all_scripts += generate_core_effect()
    
    for size in sizes:
        all_scripts += generate_floatarray(size, array_name_macro)
        all_scripts += "\n"
    
    # Get script directory and create output file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, "com_floatarray.txt")
    
    # Write to file
    with open(output_path, 'w', encoding='utf_8_sig') as f:
        f.write(all_scripts)
    
    # Get first size for examples
    example_size = sizes[0]
    last_index = example_size - 1
    
    print(f"""
✓ Successfully generated: {output_path}
  - Sizes: {', '.join(map(str, sizes))}
  Max depth: {max_depth}
""")

if __name__ == "__main__":
    main(sizes = [8, 16, 32, 64, 128, 256, 512])