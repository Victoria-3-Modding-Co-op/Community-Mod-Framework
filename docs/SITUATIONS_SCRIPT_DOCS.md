# Script Documentation
## Effects
* [save_com_situation_scope](#effect-save_com_situation_scope)
* [create_com_situation_journal_entry](#effect-create_com_situation_journal_entry)
* [create_com_situation_journal_entry_no_sides](#effect-create_com_situation_journal_entry_no_sides)
* [create_ongoing_com_situation_journal_entry](#effect-create_ongoing_com_situation_journal_entry)
* [add_ongoing_com_situation](#effect-add_ongoing_com_situation)
* [create_com_situation](#effect-create_com_situation)
* [create_com_situation_no_sides](#effect-create_com_situation_no_sides)
* [end_com_situation](#effect-end_com_situation)
* [set_com_situation_header](#effect-set_com_situation_header)
* [remove_com_situation_header](#effect-remove_com_situation_header)
* [set_je_reason_location](#effect-set_je_reason_location)
* [remove_je_reason_location](#effect-remove_je_reason_location)
* [create_com_situation_side](#effect-create_com_situation_side)
* [remove_com_situation_side](#effect-remove_com_situation_side)
* [change_com_situation_leader](#effect-change_com_situation_leader)
* [change_com_situation_side_name](#effect-change_com_situation_side_name)
* [change_com_situation_side_description](#effect-change_com_situation_side_description)
* [set_com_situation_side_victory_condition_text](#effect-set_com_situation_side_victory_condition_text)
* [set_com_situation_side_victory_effect_text](#effect-set_com_situation_side_victory_effect_text)
* [create_com_situation_faction](#effect-create_com_situation_faction)
* [remove_com_situation_faction](#effect-remove_com_situation_faction)
* [sort_com_situation_faction](#effect-sort_com_situation_faction)
* [clear_com_situation_factions](#effect-clear_com_situation_factions)
* [clear_com_situation_factions_all](#effect-clear_com_situation_factions_all)
* [add_com_situation_faction_country](#effect-add_com_situation_faction_country)
* [reassign_com_situation_faction_country](#effect-reassign_com_situation_faction_country)
* [remove_com_situation_faction_country](#effect-remove_com_situation_faction_country)
* [remove_com_situation_faction_country_all](#effect-remove_com_situation_faction_country_all)
* [create_com_situation_button_group](#effect-create_com_situation_button_group)
* [remove_com_situation_button_group](#effect-remove_com_situation_button_group)
* [add_com_situation_button_group_element](#effect-add_com_situation_button_group_element)
* [remove_com_situation_button_group_element](#effect-remove_com_situation_button_group_element)

## Triggers
* [is_com_situation_faction_member](#trigger-is_com_situation_faction_member)
* [is_in_any_com_situation_faction](#trigger-is_in_any_com_situation_faction)
* [is_party_in_com_situation](#trigger-is_party_in_com_situation)
* [is_com_situation_side_leader](#trigger-is_com_situation_side_leader)
* [has_com_situation_faction](#trigger-has_com_situation_faction)
* [num_com_situation_faction_members](#trigger-num_com_situation_faction_members)
* [has_any_com_situation_factions](#trigger-has_any_com_situation_factions)
* [exists_com_situtation](#trigger-exists_com_situtation)
* [exists_com_situtation_side](#trigger-exists_com_situtation_side)

## Lists
* [{any|every|random|ordered}_com_situation_countries](#list-anyeveryrandomordered_com_situation_countries)

## Details
### Effect: `save_com_situation_scope`
Set up an existing situation as an accessible scope.
This allows using effects and triggers that rely on the '**scope:com_situation**' outside the event chain.

**Parameters:**
- `situation_id` localization key identifier of the ongoing situation

### Effect: `create_com_situation_journal_entry`
Add journal entry to the scoped country
and add a newly created situation to that journal.

**Parameters:**
- `journal` journal entry key
- `situation_id` localization key identifier of the new situation
- `icon` icon ideology key for the situation
- `side_leader_country_left` country scope for the left side leader of the situation
- `side_name_left` name localization key for the left side leader of the situation
- `side_desc_left` description/tooltip localization key for the left side leader of the situation
- `side_leader_country_right` country scope for the right side leader of the situation
- `side_name_right` name localization key for the right side leader of the situation
- `side_desc_right` description/tooltip localization key for the right side leader of the situation

### Effect: `create_com_situation_journal_entry_no_sides`
Add journal entry to the scoped country
and add a newly created situation to that journal, without any main sides.

**Parameters:**
- `journal` journal entry key
- `situation_id` localization key identifier of the new situation
- `icon` icon ideology key for the situation

### Effect: `create_ongoing_com_situation_journal_entry`
Add journal entry to the scoped country
and add an already ongoing situation to that journal entry.

**Parameters:**
- `journal` journal entry key
- `situation_id` localization key identifier of the ongoing situation

### Effect: `add_ongoing_com_situation`
Add an ongoing situation to the current journal.
> NOTE: This effect has to be run inside a scope where '**scope:journal_entry**' is available!

**Parameters:**
- `situation_id` localization key identifier of the ongoing situation

### Effect: `create_com_situation`
Create and add a new situation to the current journal.
> NOTE: This effect has to be run inside a scope where '**scope:journal_entry**' is available!

**Parameters:**
- `situation_id` localization key identifier of the new situation
- `icon` icon ideology key for the situation
- `side_leader_country_left` country scope for the left side leader of the situation
- `side_name_left` name localization key for the left side leader of the situation
- `side_desc_left` description/tooltip localization key for the left side leader of the situation
- `side_leader_country_right` country scope for the right side leader of the situation
- `side_name_right` name localization key for the right side leader of the situation
- `side_desc_right` description/tooltip localization key for the right side leader of the situation

### Effect: `create_com_situation_no_sides`
Create and add a new situation, without any main sides, to the current journal.
> NOTE: This effect has to be run inside a scope where '**scope:journal_entry**' is available!

**Parameters:**
- `situation_id` localization key identifier of the new situation
- `icon` icon ideology key for the situation

### Effect: `end_com_situation`
This effect should be run after ALL corresponding journal entries have been concluded.

A good place to run it should be the `on_complete`/`on_fail`/`on_invalid`/`on_timeout` blocks of the master journal entry.

**Parameters:**
- `situation_id` localization key identifier of the ongoing situation

### Effect: `set_com_situation_header`
Set optional header to the situation journal entry
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `text` localization key for the situation header

### Effect: `remove_com_situation_header`
Remove optional header to the situation journal entry
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Effect: `set_je_reason_location`
Move journal reason text to header space in the situation journal entry; has no effect if left or right sides are set
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Effect: `remove_je_reason_location`
Move journal reason text to below faction space in the situation journal entry
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Effect: `create_com_situation_side`
Creates a new side, for use in changing situation types
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` = either 'left' or 'right'
- `side_name` = name localization key for the created side
- `side_desc` = description/tooltip localization key for the created side
- `side_leader_country` = country scope for the created side leader

### Effect: `remove_com_situation_side`
Removes a side from a situation
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` = either 'left' or 'right'

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

### Effect: `set_com_situation_side_victory_condition_text`
Change a side's victory condition text, if used on 'neutral' side, shows an alternative ending condition
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!
# Parameters:
- `side` = 'left', 'right', or 'neutral'
- `victory_condition` = localization key for the new victory condition text

### Effect: `set_com_situation_side_victory_effect_text`
Change a side's victory effect text, if used on 'neutral' side, shows an alternative ending effect
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!
# Parameters:
- `side` = 'left', 'right', or 'neutral'
- `victory_effect` = localization key for the new victory effect text

**Parameters:**
- `side` either 'left' or 'right'
- `desc` localization key for the new description/tooltip

### Effect: `create_com_situation_faction`
Create a new faction for the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` one of 'left', 'right' or 'neutral'
- `name` localization key for the name of the faction
- `desc` localization key for the description/tooltip of the faction

### Effect: `remove_com_situation_faction`
Remove a faction from the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` one of 'left', 'right' or 'neutral'
- `name` localization key for the name of the faction

### Effect: `sort_com_situation_faction`
Sorts members of a faction according to value or script value, uses `sort_variable_list`
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!
# Parameters:
- `side` = 'left', 'right', or 'neutral'
- `name` = localization key for the name of the faction
- `order` = a value or script value that can sort the members

**Parameters:**
- `side` one of 'left', 'right' or 'neutral'
- `name` localization key for the name of the faction

### Effect: `clear_com_situation_factions`
Clear all factions from the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` one of 'left', 'right' or 'neutral'

### Effect: `clear_com_situation_factions_all`
Clear all factions for all sides.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Effect: `add_com_situation_faction_country`
Add a new country to a faction for the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` one of 'left', 'right' or 'neutral'
- `name` localization key for the name of the faction
- `country` country scope for the new member

### Effect: `reassign_com_situation_faction_country`
Reassign a country to a new faction for the given side.
This removes the country from all other factions and adds it to the new one.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` one of 'left', 'right' or 'neutral'
- `name` localization key for the name of the faction
- `country` country scope for the new member

### Effect: `remove_com_situation_faction_country`
Remove a country from a faction for the given side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` one of 'left', 'right' or 'neutral'
- `name` localization key for the name of the faction
- `country` country scope for the removed member

### Effect: `remove_com_situation_faction_country_all`
Removes a country from all factions regardless of side or faction.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
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

### Trigger: `is_com_situation_faction_member`
Check whether the currently scoped country is part of the given faction.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` one of 'left', 'right' or 'neutral'
- `faction` localization key for the name of the faction

### Trigger: `is_in_any_com_situation_faction`
Check whether the currently scoped country is part of any faction.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Trigger: `is_com_situation_side_leader`
Check whether the currently scoped country is the leader of the specified side.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'

### Trigger: `is_party_in_com_situation`
Check whether the currently scoped country is part of the situation in any way (leader or a faction member).
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Trigger: `has_com_situation_faction`
Check whether the situation has the given faction.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` = 'left', 'right', or 'neutral'
- `name` = localization key for the name of the faction

### Trigger: `num_com_situation_faction_members`
Check whether the given faction has a certain amount of members.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` = 'left', 'right', or 'neutral'
- `name` = localization key for the name of the faction
- `op` = comparison operator, from the usual set
- `size` = value to test against

### Trigger: `has_any_com_situation_factions`
Check whether the situation has any factions.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### Trigger: `exists_com_situtation`
Check whether the given situation id exists.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `situation_id` = localization key for the situation

### Trigger: `exists_com_situtation_side`
Check whether the given situation side exists.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- side = either "left" or "right"

### List: `{any|every|random|ordered}_com_situation_countries`
Iterate over all countries involved in the situation (leader or a faction member).
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!