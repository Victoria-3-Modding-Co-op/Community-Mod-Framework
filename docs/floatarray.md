# Floatarray Utilities Documentation

## Overview

Floatarrays are a custom data type implemented through scripted variables, enabling efficient indexed storage similar to float arrays in traditional programming languages.

* **Array name macro**: `$NAME$`
* **Variable prefix**: `com_fa_` (short for floatarray)
* Optimized with reduced nesting depth using a pair-based hierarchy

Floatarrays allow you to store numerical values at indexed positions, access them quickly, iterate efficiently through all elements, and clear them when no longer needed. They behave like classic arrays: you can store any number at any index, and values may appear multiple times.

Large arrays (512 or more entries) may load slowly in the Script Explorer’s **Script Variables** tab due to the high number of generated variables — avoid opening this tab in scopes where very large arrays are stored.

---

## Working With Floatarrays in Scripted Effects

Below are the generated helper effects that allow you to create, read, write, iterate, and clear floatarrays. All functions use the `$NAME$` macro parameter to refer to the array.

### Initialize Array

```
com_floatarray_initialize = {
    NAME = ...
    SIZE = N
}
```

Creates variables `com_fa_$NAME$_0` to `com_fa_$NAME$_{N-1}` initialized to 0 in the current scope.

### Get Array Value

For uncertain indices:
```
com_floatarray_get = {
    NAME = ...
    SIZE = N
}
```
For known indices
```com_floatarray_get_at = {
    NAME = ...
    INDEX = N
}
```
* **Requires**: `var:com_fa_index` (0 to N-1)
* **Returns**: `var:com_fa_return` (value at index)

Random-access reads are very fast.

### Set Array Value

For uncertain indices:
```
com_floatarray_set = {
    NAME = ...
    SIZE = N
}
```
For known indices
```com_floatarray_set_at = {
    NAME = ...
    INDEX = N
}
```
* **Requires**: `var:com_fa_index` (0 to N-1), `var:com_fa_value`
* Sets the value at the specified index

Setting a value at a specific index is also very fast.

### Set index variable
Sets the value of `var:com_fa_index` to VALUE
`com_floatarray_set_index = { VALUE = ... }`

### Set value variable
Sets the value of `var:com_fa_value` to VALUE
`com_floatarray_set_value = { VALUE = ... }`

### For-Each Loop

```
com_floatarray_foreach = {
    NAME = ...
    SIZE = N
}
```

* **Sets**: `var:com_fa_index` and `var:com_fa_value` when iterating
* `BODY` is a fully scripted effect, such as `"your_scripted_effect = yes"` or `"add_treasury = var:com_fa_value"`
* The `BODY` effect is called **once per iteration** over the array
* In each iteration:

  * `var:com_fa_index` is set to the **current index** of the iteration
  * `var:com_fa_value` contains the **current element at that index** (the value retrieved from the array)
  * You can **modify `var:com_fa_value`** inside the effect, and the updated value will be stored back in the array at the same index

For iterating over an entire array, `foreach` is **best practice** and highly performant. If you plan to iterate many very large arrays frequently, consider performing this work in a **monthly or yearly pulse**.



### Clear Array

```
com_floatarray_clear = {
    NAME = ...
    SIZE = N
}
```

Deletes all variables belonging to the array.

---

## Complete Usage Example

```
com_test_floatarray = {
    # 1. Initialize array
    com_floatarray_initialize = { NAME = mydata SIZE = 8 }
    
    # 2. Fill array with foreach
    com_floatarray_128_foreach = {
        NAME = mydata
        BODY = "body_fill = yes"
    }
    
    # 3. Get value from index 5
    com_floatarray_set_index = { VALUE = 5 }
    com_floatarray_get = { NAME = mydata SIZE = 8 }
    # var:returned now contains 5
    
    # 4. Set value at index 5
    com_floatarray_set_index = { VALUE = 5 }
    com_floatarray_set_value = { VALUE = 42 }
    com_floatarray_set = { NAME = mydata SIZE = 8 }
    
    # 5. Initialize sum variable
    set_variable = { name = sum value = 0 }
    
    # 6. Sum all values with foreach
    com_floatarray_foreach = {
        NAME = mydata
        SIZE = 8
        BODY = "body_sum = yes"
    }
    
    # 7. Clear array when done
    com_floatarray_clear = { NAME = mydata SIZE = 8 }
}

# Body effect for foreach - executed for each element
body_fill = {
    set_variable = { name = com_fa_value value = var:com_fa_index }
}

body_sum = {
    change_variable = { name = sum add = var:com_fa_value }
}
```

---

## File Locations

All generated floatarray scripted effects are defined in:
**`\common\scripted_effects\com_floatarray.txt`**
Static wrapper and utility effects are defined in:
**`\common\scripted_effects\com_floatarray_utils.txt`**
---

## Generator Script

The Python script that generates all floatarray helper functions is located at:
**`\script\generate_floatarray.py`**

Default configuration:

```python
if __name__ == "__main__":
    main(sizes=[8, 16, 32, 64, 128, 256, 512], output_file='com_floatarray.txt')
```

You can freely configure custom floatarray sizes:

```python
main(sizes=[8, 16, 1024])
```

Custom output file:

```python
main(sizes=[8, 16, 32, 64, 4096], output_file='my_arrays.txt')
```

There is **no maximum floatarray size**, but extremely large arrays may impact performance. When processing many large arrays frequently, consider executing such logic on **monthly or yearly pulses**.
