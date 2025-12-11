# Progress bar styling guide
With this part of the Community Mod Framework, journal entry progress bars can be given styling to show 'drift' and target values.

These styles are entirely optional and do not replace base game or previous CMF progress bar styles. They can also be used with [situations](SITUATIONS.md).

Most of the complexity is masked behind tailored and documented scripted effects.
A full list of them can be found below in the [script docs](#script-docs).

# Content
* [Usage](#usage)
  * [Setting up a new progress bar style](#setting-up-a-new-progress-bar-style)
  * [Modifying a progress bar](#modifying-a-progress-bar)
  * [Drift and target values](#drift-and-target-values)
    * [Colors and icons](#colors-and-icons)
  * [Example progress bar setup](#example-progress-bar-setup)
* [Script docs](#script-docs)
  * [Effects](#effects)
  * [Triggers](#triggers)
  * [Details](#details)
* [Compatibility notes](#compatibility-notes)

# Usage
## Setting up a new progress bar style
Each progress bar in a journal entry can be styled separately, and most stylings are independently settable

- Each bar is identified by its id, which can be any localization key
- If multiple countries have the same journal entry active, each bar is considered a separate entity

To set up a progress bar with custom styling, there is a basic initialization and four more complete versions:
* [initialize_com_progress_bar](#effect-initialize_com_progress_bar) initializes the progress bar as available for styling.
* [create_com_progress_bar](#effect-create_com_progress_bar) initializes the progress bar and sets its color.
* [create_com_progress_bar_with_drift](#effect-create_com_progress_bar_with_drift) initializes the progress bar, sets its color, and sets the color and value of the 'drift' effect.
* [create_com_progress_bar_with_target](#effect-create_com_progress_bar_with_target) initializes the progress bar, sets its color, and sets the style and value of the target effect.
* [create_com_progress_bar_with_both](#effect-create_com_progress_bar_with_both) initializes the progress bar, sets its color, and sets up both the drift and target effect.

> **NOTE** If a progress bar has already been initialized,
> any of the other creation effects work as expected, and do not reset anything other than specified.

## Modifying a progress bar
All effects and triggers and lists from the [script docs](#script-docs) can be used from any context.

For other effects and triggers, use the wrappers [run_in_com_progress_bar_scope](#effect-run_in_com_progress_bar_scope) and [test_in_com_progress_bar_scope](#trigger-test_in_com_progress_bar_scope).

For example, to set a custom icon, you can use the following format:
```
run_in_com_progress_bar_scope = {
  progress_bar = <progress_bar_id>
  effect = "set_ideology = ideology:<custom_ideology_name>"
}
```

## Drift and target values
The progress bar drift and target each require an associated script value. The drift script value should generally match the value of the scripted progress, plus the current value of the progress bar. Note that the final value must be in the range 0-1, so it should be divided by `bar max value - bar min value`.

The target script value can be set to match the current value, replicating base game behavior, or it be set to a static or dynamic value to create a visual target for the bar to approach. This value is also in the range 0-1.

### Colors and icons
The progress bar and the drift style can be given one of five colors, `default`/`blue`, `bad`/`red`, `green`, `gold`, and `white`, or made blank with `transparent`. 

## Example progress bar setup
There is an example journal entry which was used for testing in the Community Mod Framework.

[This journal entry can be found here.](/common/journal_entries/com_progress_in_style.txt)

# Script docs
These are following effects and triggers available to use for styling progress bars:

## Effects
* [save_com_progress_bar_scope](#effect-save_com_progress_bar_scope)
* [run_in_com_progress_bar_scope](#effect-run_in_com_progress_bar_scope)
* [initialize_com_progress_bar](#effect-initialize_com_progress_bar)
* [create_com_progress_bar](#effect-create_com_progress_bar)
* [create_com_progress_bar_with_drift](#effect-create_com_progress_bar_with_drift)
* [create_com_progress_bar_with_target](#effect-create_com_progress_bar_with_target)
* [create_com_progress_bar_with_both](#effect-create_com_progress_bar_with_both)
* [remove_com_progress_bar](#effect-remove_com_progress_bar)
* [set_com_progress_bar_color](#effect-set_com_progress_bar_color)
* [remove_com_progress_bar_color](#effect-remove_com_progress_bar_color)
* [set_com_progress_bar_drift](#effect-set_com_progress_bar_drift)
* [remove_com_progress_bar_drift](#effect-remove_com_progress_bar_drift)
* [set_com_progress_bar_target](#effect-set_com_progress_bar_target)
* [remove_com_progress_bar_target](#effect-remove_com_progress_bar_target)
* [com_debug_progress_bar](#effect-com_debug_progress_bar)

## Triggers
* [exists_com_progress_bar](#trigger-exists_com_progress_bar)
* [is_com_progress_bar_hidden](#trigger-is_com_progress_bar_hidden)
* [test_in_com_progress_bar_scope](#trigger-test_in_com_progress_bar_scope)

## Details
Most effects require a parameter `progress_bar`, which is the localization key used to initialize the progress bar

### Effect: `save_com_progress_bar_scope`
Set an initialized progress bar as an accessible scope. All effects below automatically do this.
This allows using effects and triggers in '**scope:com_$progress_bar$**' outside the event chain.

**Parameters:**
- `progress_bar` localization key identifier of the progress_bar

### Effect: `run_in_com_progress_bar_scope`
A wrapper effect to easily run an effect inside '**scope:com_$progress_bar$**'

**Parameters:**
- `progress_bar` name localization key of progress bar
- `effect` effect or series of effects to be run inside '**scope:com_$progress_bar$**'

### Effect: `initialize_com_progress_bar`
This is the basic initialization effect to set up a progress bar for styling.
This effect has to be run inside a scope where '**scope:journal_entry**' is available! Typically, this in the `immediate` block.
THIS DOES NOT REPLACE THE VANILLA SETUP!

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `index` 0-indexed position of the progress bar in the journal, first scripted progress bar in the journal entry is 0, second is 1, and so on.

### Effect: `create_com_progress_bar`
Extension of `initialize_com_progress_bar` that also sets the color of the progress bar.
This effect has to be run inside a scope where '**scope:journal_entry**' is available! Typically, this in the `immediate` block.
THIS DOES NOT REPLACE THE VANILLA SETUP!

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `index` 0-indexed position of the progress bar in the journal
- `color` color of base bar, valid colors are `default`/`blue`, `bad`/`red`, `green`, `gold`, and `white`, or `transparent`

### Effect: `create_com_progress_bar_with_drift`
Extension of `initialize_com_progress_bar` that also sets the color and drift style of the progress bar.
This effect has to be run inside a scope where '**scope:journal_entry**' is available! Typically, this in the `immediate` block.
THIS DOES NOT REPLACE THE VANILLA SETUP!

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `index` 0-indexed position of the progress bar in the journal
- `color` color of base bar, valid colors are `default`/`blue`, `bad`/`red`, `green`, `gold`, and `white`, or `transparent`
- `bar_increase_color` color of drift bar when increasing, same valid colors as the base
- `bar_decrease_color` color of drift bar when decreasing, same valid colors as the base
- `drift_value` a 0-1 script value key which sets the size and direction of the drift 

### Effect: `create_com_progress_bar_with_target`
Extension of `initialize_com_progress_bar` that also sets the color and target style of the progress bar.
This effect has to be run inside a scope where '**scope:journal_entry**' is available! Typically, this in the `immediate` block.
THIS DOES NOT REPLACE THE VANILLA SETUP!

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `index` 0-indexed position of the progress bar in the journal
- `color` color of base bar, valid colors are `default`/`blue`, `bad`/`red`, `green`, `gold`, and `white`, or `transparent`
- `target_type` = icon type for target value, valid values are `journal_icon`, `gold_marker`, `gold_bar`, and `"color"_line`, where "color" is any of the valid colors
- `target_value` = a 0-1 script value key which sets the position of the target

### Effect: `create_com_progress_bar_with_both`
Extension of `initialize_com_progress_bar` that also sets the color, drift effect, and target style of the progress bar
This effect has to be run inside a scope where '**scope:journal_entry**' is available! Typically, this in the `immediate` block.
THIS DOES NOT REPLACE THE VANILLA SETUP!

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `index` 0-indexed position of the progress bar in the journal
- `color` color of base bar, valid colors are `default`/`blue`, `bad`/`red`, `green`, `gold`, and `white`, or `transparent`
- `bar_increase_color` color of drift bar when increasing, same valid colors as the base
- `bar_decrease_color` color of drift bar when decreasing, same valid colors as the base
- `drift_value` a 0-1 script value key which sets the size and direction of the drift 
- `target_type` = icon type for target value, valid values are `custom_icon`, `journal_icon`, `gold_marker`, `gold_bar`, and `"color"_line`, where "color" is any of the valid colors
- `target_value` = a 0-1 script value key which sets the position of the target

### Effect: `remove_com_progress_bar`
Clean up effect that also removes any styling.
This effect should be run when the journal entry concludes.
Parameters:
- `progress_bar` localization key identifier of progress bar

### Effect: `set_com_progress_bar_color`
Sets the color of the progress bar.

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `color` color of bar, valid colors are `default`/`blue`, `bad`/`red`, `green`, `gold`, and `white`, or `transparent`
- `side` which side to color, 'left' or 'right'

### Effect: `remove_com_progress_bar_color`
Unsets the color of the progress bar, i.e. returns it to base game color

**Parameters:**
- `progress_bar` localization key identifier of progress bar

### Effect: `set_com_progress_bar_drift`
Sets the drift style of the progress bar.

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `bar_increase_color` color of drift bar when increasing, valid colors are `default`/`blue`, `bad`/`red`, `green`, `gold`, and `white`, or `transparent`
- `bar_decrease_color` color of drift bar when decreasing, same valid colors as the increase colors
- `drift_value` a 0-1 script value key which sets the size and direction of the drift 

### Effect: `remove_com_progress_bar_drift`
Removes the drift style of the progress bar

**Parameters:**
- `progress_bar` localization key identifier of progress bar

### Effect: `set_com_progress_bar_target`
Sets the target style of the progress bar. The custom icon uses the an ideology, so custom ideologies can be defined to use any desired image or icon.
To set a custom icon, set the custom ideology in '**scope:com_$progress_bar$**'

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `target_type` = icon type for target value, valid values are `custom_icon`, `journal_icon`, `gold_marker`, `gold_bar`, and `"color"_line`, where "color" is any of the valid colors
- `target_value` = a 0-1 script value key which sets the position of the target

### Effect: `remove_com_progress_bar_target`
Removes the target style of the progress bar

**Parameters:**
- `progress_bar` localization key identifier of progress bar

### Effect: `hide_com_progress_bar`
Hides the specified progress bar from the journal

**Parameters:**
- `progress_bar` localization key identifier of progress bar

### Effect: `unhide_com_progress_bar`
Unhides the specified progress bar from the journal

**Parameters:**
- `progress_bar` localization key identifier of progress bar

### Effect: `com_debug_progress_bar`
Debug effect to check variable values, should be used in script explorer only.

**Parameters:**
- `progress_bar` localization key identifier of progress bar
- `index` 0-indexed position of the progress bar in the journal
- `je` journal entry key

### Trigger: `exists_com_progress_bar`
Check whether the given progress bar has been initialized for styling.

**Parameters:**
- `progress_bar` = localization key identifier of the progress_bar

### Trigger: `is_com_progress_bar_hidden`
Check whether the given progress bar is visible or not.

**Parameters:**
- `progress_bar` = localization key identifier of the progress_bar

### Trigger: `test_in_com_progress_bar_scope`
A wrapper effect to easily check a trigger inside '**scope:com_$progress_bar$**'

**Parameters:**
- `progress_bar` name localization key of progress bar
- `trigger` trigger or series of triggers to be run inside '**scope:com_$progress_bar$**'

# Compatibility notes
If you do not want to make the Community Mod Framework a required dependency for you mod, but you want the styles to be used when the CMF is enabled, you can define a set of dummy scripted effects and triggers with the same names as everything in the [script docs](#script-docs), these should in a file that comes before `com_progressbar_effects.txt` so that it is overwritten by CMF and the effects can be active.

To avoid errors because of the parameters, you can have the dummy effects set a local variable for each parameter, such as `set_local_variable = $progress_bar$`