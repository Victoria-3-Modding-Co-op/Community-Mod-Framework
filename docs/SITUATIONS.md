# Documentation
## Effects
* [create_com_situation_journal_entry](#effect-create_com_situation_journal_entry)
* [create_ongoing_com_situation_journal_entry](#effect-create_ongoing_com_situation_journal_entry)
* [add_ongoing_com_situation](#effect-add_ongoing_com_situation)
* [create_com_situation](#effect-create_com_situation)
* [end_com_situation](#effect-end_com_situation)
* [set_com_situation_header](#effect-set_com_situation_header)
* [remove_com_situation_header](#effect-remove_com_situation_header)
* [change_com_situation_leader](#effect-change_com_situation_leader)
* [change_com_situation_side_name](#effect-change_com_situation_side_name)
* [change_com_situation_side_description](#effect-change_com_situation_side_description)
* [create_com_situation_faction](#effect-create_com_situation_faction)
* [remove_com_situation_faction](#effect-remove_com_situation_faction)
* [clear_com_situation_factions](#effect-clear_com_situation_factions)
* [clear_com_situation_factions_both](#effect-clear_com_situation_factions_both)
* [add_com_situation_faction_country](#effect-add_com_situation_faction_country)
* [remove_com_situation_faction_country](#effect-remove_com_situation_faction_country)
* [create_com_situation_button_group](#effect-create_com_situation_button_group)
* [remove_com_situation_button_group](#effect-remove_com_situation_button_group)
* [add_com_situation_button_group_element](#effect-add_com_situation_button_group_element)
* [remove_com_situation_button_group_element](#effect-remove_com_situation_button_group_element)

### Effect: `create_com_situation_journal_entry`
Add journal entry to the scoped country
and add a newly created situation to that journal.

**Parameters:**
- `journal` journal entry key
- `situation_id` id of the new situation
- `icon` icon ideology key for the situation
- `side_leader_country_left` country scope for the left side leader of the situation
- `side_name_left` name localization key for the left side leader of the situation
- `side_desc_left` description/tooltip localization key for the left side leader of the situation
- `side_leader_country_right` country scope for the right side leader of the situation
- `side_name_right` name localization key for the right side leader of the situation
- `side_desc_right` description/tooltip localization key for the right side leader of the situation

### Effect: `create_ongoing_com_situation_journal_entry`
Add journal entry to the scoped country
and add an already ongoing situation to that journal entry.

**Parameters:**
- `journal` journal entry key
- `situation_id` id of the ongoing situation

### Effect: `add_ongoing_com_situation`
Add an ongoing situation to the current journal.
> NOTE: This effect has to be run inside a scope where '**scope:journal_entry**' is available!

**Parameters:**
- `id` id of the ongoing situation

### Effect: `create_com_situation`
Create and add a new situation to the current journal.
> NOTE: This effect has to be run inside a scope where '**scope:journal_entry**' is available!

**Parameters:**
- `id` id of the new situation
- `icon` icon ideology key for the situation
- `side_leader_country_left` country scope for the left side leader of the situation
- `side_name_left` name localization key for the left side leader of the situation
- `side_desc_left` description/tooltip localization key for the left side leader of the situation
- `side_leader_country_right` country scope for the right side leader of the situation
- `side_name_right` name localization key for the right side leader of the situation
- `side_desc_right` description/tooltip localization key for the right side leader of the situation

### Effect: `end_com_situation`
This effect should be run after ALL corresponding journal entries have been concluded.

A good place to run it should be the on_complete/on_fail/on_invalid/on_timeout blocks of the master journal entry.

**Parameters:**
- `id` id of the situation

### Effect: `set_com_situation_header`
Set optional header to the situation journal entry
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `text` localization key for the situation header

### Effect: `remove_com_situation_header`
Remove optional header to the situation journal entry
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Effect: `change_com_situation_leader`
Change a sides situation leader country
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'
- `leader` country scope of the new side leader

### Effect: `change_com_situation_side_name`
Change a sides name
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'
- `name` localization key for the new name

### Effect: `change_com_situation_side_description`
Change a sides description/tooltip
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'
- `desc` localization key for the new description/tooltip

### Effect: `create_com_situation_faction`
Create a new faction for the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'
- `name` localization key for the name of the faction
- `desc` localization key for the description/tooltip of the faction

### Effect: `remove_com_situation_faction`
Remove a faction from the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'
- `name` localization key for the name of the faction

### Effect: `clear_com_situation_factions`
Clear all factions from the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'

### Effect: `clear_com_situation_factions_both`
Clear all factions for both sides.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Effect: `add_com_situation_faction_country`
Add a new country to a faction for the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'
- `name` localization key for the name of the faction
- `country` country scope for the new member

### Effect: `remove_com_situation_faction_country`
Remove a country from a faction for the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'
- `name` localization key for the name of the faction
- `country` country scope for the removed member

### Effect: `create_com_situation_button_group`
Create a button group for the situation.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `name` localization key for the name of the button group
- `desc` localization key for the description/tooltip of the button group

### Effect: `remove_com_situation_button_group`
Remove a button group from the situation.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `name` localization key for the name of the button group

### Effect: `add_com_situation_button_group_element`
Add a scripted button to a button group.
The scripted button has to be added to the journal entry as normal first.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `name` localization key for the name of the scripted button
- `group` localization key for the name of the button group

### Effect: `remove_com_situation_button_group_element`
Remove a scripted button from a button group.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `name` localization key for the name of the scripted button
- `group` localization key for the name of the button group

