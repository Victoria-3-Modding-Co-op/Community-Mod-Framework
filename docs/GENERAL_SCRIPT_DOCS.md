# General Effect Script Docs
The following effects are provided as quality of life features:

## Effects
* [fix_variable_error](#effect-fix_variable_error)
* [com_update_value_in_variable_map](#effect-com_update_value_in_variable_map)
* [com_update_value_in_global_variable_map](#effect-com_update_value_in_global_variable_map)

## Details

### Effect: `fix_variable_error`
Suppresses errors printed from unset or unused variables and flags

**Parameters:**
- `variable` the name of the variable or flag

### Effect: `com_update_value_in_variable_map`
Checks for the presence of a key in a variable map, and removes it before re-adding the key-value pair. Currently, `add_to_variable_map` will fail if the key is already present in the variable map.

**Parameters:**
- `name` 
- `key` 
- `value`

### Effect: `com_update_value_in_global_variable_map`
Checks for the presence of a key in a global variable map, and removes it before re-adding the key-value pair. Currently, `add_to_global_variable_map` will fail if the key is already present in the global variable map.

**Parameters:**
- `name`
- `key`
- `value`