# Overview
Situations are meant to model clashes between factions on an international scale.

They can have multiple journal entries associated with it and provide a tool to model complex power struggles.

In the background, situations are Journal Entries with a few extra variables and a whole new layout.
This means using them should come natural to modders who have already used those.

Most of the complexity is masked behind tailored and documented scripted effects.
A full list of them can be found below.

# Content
* [Overview](#overview)
* [Usage](#usage)
  * [Setting up a new situation](#setting-up-a-new-situation)
  * [Victory conditions](#victory-conditions)
  * [Optional features](#optional-features)
    * [Factions](#factions)
    * [Button Groups](#button-groups)
* [Script Documentation](#script-documentation)
  * [Effects](#effects)
  * [Triggers](#triggers)
  * [Lists](#lists)

# Usage
## Setting up a new situation
All situations have two main sides that are set up at the start (Though there are effects to change them).
Each side has a name, description and a leader country.

- The whole situation itself is identified by its id
- The id can be anything that can be assigned to a variable
- The framework guarantees that situations with the same id are always the same anywhere they are used
- This means as long as the same ids are used, the situation is the same everywhere and manipulation in one context is reflected in another

To set up a new situation, there are two possible effects:
* [create_com_situation_journal_entry](#effect-create_com_situation_journal_entry) adds a journal entry to the country and also creates a new situation for that journal entry.
* [create_com_situation](#effect-create_com_situation) just creates and sets up the situation. It is meant to be used in the `immediate` block of a journal entry.

> **NOTE** If a situation already exists,
> both effects work the same as [create_ongoing_com_situation_journal_entry](#effect-create_ongoing_com_situation_journal_entry) and [add_ongoing_com_situation](#effect-add_ongoing_com_situation)!
> So there can always be only one situation with a specific **id** no matter how many journal entries try to create it.

## Victory conditions
Each side has its own victory condition.
This is modeled through the `complete` and `fail` blocks of the journal.

The `complete` blocks (`complete`, `on_complete`, etc.)
are the victory conditions for the left side of the situation,
while `fail` blocks (`fail`, `on_fail`, etc.) are the victory conditions for the right side of the situation.

## Optional features
Situations can have scripted progress bars, scripted buttons and so on as any other journal entry.

Though there are some situation specific features that can be used if needed.

### Factions
Factions are subgroups of countries inside a side of the situation.
These can be used to model how a side in the situation may have a unified goal but is still made up of different internal factions.
Each side has a name, a description and is composed of member countries.

For example, a 'Communists' side could have factions like 'Hardliners' and 'Reformers'.

A new faction can be created and assigned using the [create_com_situation_faction](#effect-create_com_situation_faction) effect.
After the creation of a faction,
countries can be assigned to it using the [add_com_situation_faction_country](#effect-add_com_situation_faction_country) effect.

### Button Groups
Button groups allow scripted buttons of the journal entry to be categorized into groups.
Each side has a name and a description.

To use button groups first one needs to be created using [create_com_situation_button_group](#effect-create_com_situation_button_group)
and then [add_com_situation_button_group_element](#effect-add_com_situation_button_group_element) can be used to assign scripted buttons to the group

> **NOTE** As soon as there is at least one button group, all buttons need to be put into a group for them to be visible to the user!

# Script Documentation
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
* [save_com_situation_scope](#effect-save_com_situation_scope)

## Triggers
* [is_com_situation_faction_member](#trigger-is_com_situation_faction_member)
* [is_party_in_com_situation](#trigger-is_party_in_com_situation)

## Lists
* [{any|every|random|ordered}_com_situation_countries](#list-anyeveryrandomordered_com_situation_countries)

## Details
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

### Effect: `save_com_situation_scope`
Set up an existing situation as an accessible scope.
This allows using effects and triggers that rely on the '**scope:com_situation**' outside the event chain.

**Parameters:**
- `id` id of the ongoing situation

### Trigger: `is_com_situation_faction_member`
Check whether the currently scoped country is part of the given faction.
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

**Parameters:**
- `side` either 'left' or 'right'
- `name` localization key for the name of the faction

### Trigger: `is_party_in_com_situation`
Check whether the currently scoped country is part of the situation in any way (leader or a faction member).
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!

### List: `{any|every|random|ordered}_com_situation_countries`
Iterate over all countries involved in the situation (leader or a faction member).
> NOTE: This effect has to be run inside a scope where '**scope:com_situation**' is available!