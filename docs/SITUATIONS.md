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
  * [Modifying a situation](#modifying-a-situation)
  * [Scoping to side leaders](#scoping-to-side-leaders)
  * [Victory conditions](#victory-conditions)
  * [Example Journal](#victory-conditions)
  * [Optional features](#optional-features)
    * [Factions](#factions)
    * [Button Groups](#button-groups)

# Usage
## Setting up a new situation
There are three types of situations: two-sided, one-sided, and no-sided. They are broadly the same, and it is possible to change between the formats dynamically.

All situations can have two main sides, plus a third "neutral" side. These can be set up at the start or later through effects, and there are futher effects to modify sides.
The main sides each have a name, description and a leader country.

- The whole situation itself is identified by its id
- The id can be any localization key
- The framework guarantees that situations with the same id are always the same anywhere they are used
- This means as long as the same ids are used, the situation is the same everywhere and manipulation in one context is reflected in another

To set up a new situation, there are two possible effects, either with the main sides specified or not:
* [create_com_situation_journal_entry](SITUATIONS_SCRIPT_DOCS.md#effect-create_com_situation_journal_entry) adds a journal entry to the country and also creates a new situation for that journal entry.
* [create_com_situation_journal_entry_no_sides](SITUATIONS_SCRIPT_DOCS.md#effect-create_com_situation_journal_entry_no_sides) adds a journal entry to the country and also creates a new situation for that journal entry, without the main sides.
* [create_com_situation](SITUATIONS_SCRIPT_DOCS.md#effect-create_com_situation) just creates and sets up the situation. It is meant to be used in the `immediate` block of a journal entry.
* [create_com_situation_no_sides](SITUATIONS_SCRIPT_DOCS.md#effect-create_com_situation_no_sides) just creates and sets up the situation, without the main sides. It is meant to be used in the `immediate` block of a journal entry.

> **NOTE** If a situation already exists,
> both effects work the same as [create_ongoing_com_situation_journal_entry](SITUATIONS_SCRIPT_DOCS.md#effect-create_ongoing_com_situation_journal_entry) and [add_ongoing_com_situation](SITUATIONS_SCRIPT_DOCS.md#effect-add_ongoing_com_situation)!
> So there can always be only one situation with a specific **id** no matter how many journal entries try to create it.

## Modifying a situation
Inside the event chain, all effects, triggers and lists from the [script docs](SITUATIONS_SCRIPT_DOCS.md) can be used.

Outside the event chain, the context has to first be established.
This can be done using the [save_com_situation_scope](SITUATIONS_SCRIPT_DOCS.md#effect-save_com_situation_scope) effect.
After that effect was run, all documented effects, triggers and lists can be used as normal.

## Scoping to side leaders
To scope to the leader of a specific side in the situation, a provided trigger and list need to be combined.
The [{any|every|random|ordered}_com_situation_countries](SITUATIONS_SCRIPT_DOCS.md#list-anyeveryrandomordered_com_situation_countries) list
and the [is_com_situation_side_leader](SITUATIONS_SCRIPT_DOCS.md#trigger-is_com_situation_side_leader) trigger.

Here is an example:
```
scope:com_situation = {
    every_com_situation_countries = {
        limit = {
            is_com_situation_side_leader = {
                side = left
            }
        }
        # Do something to the leader country of the left side
    }
}
```

## Victory conditions
Each side has its own victory condition.
This is modeled through the `complete` and `fail` blocks of the journal.

The `complete` blocks (`complete`, `on_complete`, etc.)
are the victory conditions for the left side of the situation,
while `fail` blocks (`fail`, `on_fail`, etc.) are the victory conditions for the right side of the situation.

To change the localization for "If completed:" or "Will complete if:"
the game offers these properties in journal entries:
- `custom_on_completion_header = <loc key>`
- `custom_on_failure_header = <loc key>`
- `custom_completion_header = <loc key>`
- `custom_failure_header = <loc key>`

Here is a set of example locs for those:
```yaml
 je_springtime_of_the_peoples_complete_header: "#title Will result in a #b Revolutionary#! victory if:#!\n"
 je_springtime_of_the_peoples_on_complete_header: "#title On a #b Revolutionary#! victory:#!\n$EFFECT$"
 je_springtime_of_the_peoples_fail_header: "#title Will result in a #b Conservative#! victory if:#!\n"
 je_springtime_of_the_peoples_on_fail_header: "#title On a #b Conservative#! victory:#!\n$EFFECT$"
```
> **NOTE** The `$EFFECT$` has to be part of the effect localization blocks to hide the base effect blocks

Custom victory condition and effect text can be set for either side with [set_com_situation_side_victory_condition_text](SITUATIONS_SCRIPT_DOCS.md#effect-set_com_situation_side_victory_condition_text) and [set_com_situation_side_victory_effect_text](SITUATIONS_SCRIPT_DOCS.md#effect-set_com_situation_side_victory_effect_text). This can also be used on the neutral side to display alternative ending conditions.

## Example Journal
There is an example journal entry which was used for testing in the Community Mod Framework.

[This journal entry can be found here.](/common/journal_entries/com_rise_of_communism.txt)

## Optional features
Situations can have scripted progress bars, scripted buttons and so on as any other journal entry.

Though there are some situation specific features that can be used if needed.

### Factions
Factions are subgroups of countries inside a side of the situation.
These can be used to model how a side in the situation may have a unified goal but is still made up of different internal factions.
Each side has a name, a description and is composed of member countries.

For example, a 'Communists' side could have factions like 'Hardliners' and 'Reformers'.

A new faction can be created and assigned using the [create_com_situation_faction](SITUATIONS_SCRIPT_DOCS.md#effect-create_com_situation_faction) effect.
After the creation of a faction,
countries can be assigned to it using the [add_com_situation_faction_country](SITUATIONS_SCRIPT_DOCS.md#effect-add_com_situation_faction_country) effect.

There is a third "side" for factions, neutral, which cannot have a leader. The neutral factions are not shown if none are set up.

### Button Groups
Button groups allow scripted buttons of the journal entry to be categorized into groups.
Each side has a name and a description.

To use button groups first one needs to be created using [create_com_situation_button_group](SITUATIONS_SCRIPT_DOCS.md#effect-create_com_situation_button_group)
and then [add_com_situation_button_group_element](SITUATIONS_SCRIPT_DOCS.md#effect-add_com_situation_button_group_element) can be used to assign scripted buttons to the group

> **NOTE** As soon as there is at least one button group, all buttons need to be put into a group for them to be visible to the user!