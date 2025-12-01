# Floatarray Utilities Documentation

## Overview

Floatarrays are a custom data type implemented through scripted variables, enabling efficient indexed storage similar to float arrays in traditional programming languages.

* **Array name macro**: `$NAME$`
* **Variable prefix**: `z_fa_` (short for floatarray)
* Optimized with reduced nesting depth using a pair-based hierarchy

Floatarrays allow you to store numerical values at indexed positions, access them quickly, iterate efficiently through all elements, and clear them when no longer needed. They behave like classic arrays: you can store any number at any index, and values may appear multiple times.

Large arrays (512 or more entries) may load slowly in the Script Explorer’s **Script Variables** tab due to the high number of generated variables — avoid opening this tab in scopes where very large arrays are stored.

---

## Working With Floatarrays in Scripted Effects

Below are the generated helper effects that allow you to create, read, write, iterate, and clear floatarrays. All functions use the `$NAME$` macro parameter to refer to the array.

### Initialize Array

```
com_floatarray_N_initialize = { NAME = ... }
```

Creates variables `z_fa_$NAME$_0` to `z_fa_$NAME$_{N-1}` initialized to 0 in the current scope.

### Get Value

```
com_floatarray_N_get = { NAME = ... }
```

* **Requires**: `var:INDEX` (0 to N-1)
* **Returns**: `var:returned` (value at index)

Random-access reads are very fast.

### Set Value

```
com_floatarray_N_set = { NAME = ... }
```

* **Requires**: `var:INDEX` (0 to N-1), `var:VALUE`
* Sets the value at the specified index

Setting a value at a specific index is also very fast.

### For-Each Loop

```
com_floatarray_N_foreach = { NAME = ... BODY = ... }
```

* **Sets**: `var:INDEX` and `var:VALUE` when iterating
* `BODY` must be the name of a **scripted effect you define yourself**
* The `BODY` effect is called **once per iteration** over the array
* In each iteration:

  * `var:INDEX` is set to the **current index** of the iteration
  * `var:VALUE` contains the **current element at that index** (the value retrieved from the array)
  * You can **modify `var:VALUE`** inside the effect, and the updated value will be stored back in the array at the same index

For iterating over an entire array, `foreach` is **best practice** and highly performant. If you plan to iterate many very large arrays frequently, consider performing this work in a **monthly or yearly pulse**.



### Clear Array

```
com_floatarray_N_clear = { NAME = ... }
```

Deletes all variables belonging to the array.

---

## Complete Usage Example

```
com_test_floatarray = {
    # 1. Initialize array
    com_floatarray_8_initialize = { NAME = mydata }
    
    # 2. Fill array with foreach
    com_floatarray_8_foreach = {
        NAME = mydata
        BODY = body_fill
    }
    
    # 3. Get value from index 5
    set_variable = { name = INDEX value = 5 }
    com_floatarray_8_get = { NAME = mydata }
    # var:returned now contains 5
    
    # 4. Set value at index 5
    set_variable = { name = INDEX value = 5 }
    set_variable = { name = VALUE value = 42 }
    com_floatarray_8_set = { NAME = mydata }
    
    # 5. Initialize sum variable
    set_variable = { name = sum value = 0 }
    
    # 6. Sum all values with foreach
    com_floatarray_8_foreach = {
        NAME = mydata
        BODY = body_sum
    }
    
    # 7. Clear array when done
    com_floatarray_8_clear = { NAME = mydata }
}

# Body effect for foreach - executed for each element
body_fill = {
    set_variable = { name = VALUE value = var:INDEX }
}

body_sum = {
    change_variable = { name = sum add = var:VALUE }
}
```

---

## File Locations

All generated floatarray scripted effects are stored in:
**`\common\scripted_effects\com_floatarray.txt`**

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
