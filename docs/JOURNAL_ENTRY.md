# Overview
Since 1.13 Journal Entries can have custom GUI elements injected into them.

The Community Mod Framework provides a set of custom elements for modders to use in their mods. Below you can find a list and how to use them.

All CMF elements are injected like this:
```
widget = {
    gui = "gui/com_journal_injects/injects.gui"
    name = "name_of_custom_element"
    container = "inject_anchor"
}
```

# Content
* [DLC Icon](#dlc-icon)
* [Characters with Opinions](#characters-with-opinions)
* [Wrap Modifiers](#wrap-modifiers)
* [Progress Bar Styling](#progress-bar-styling)

# Elements
## DLC Icon
- **Injection Name:** `com_journal_entry_dlc_icon`
- **Recommended Anchor:** `custom_widget_container_7`
- **Screenshots:** [DLC icon](images/journal_entries/example_dlc_icon.png)

To add DLC/Mod information to a journal entry, CMF offers the scripted effect `add_com_dlc_icon`.

It needs to be run in the journal entry scope.
The best place for that is the `immediate` block of a journal entry:
```
je_some_journal = {
    # journal definition  
    widget = {
        gui = "gui/com_journal_injects/injects.gui"
        name = "com_journal_entry_dlc_icon"
        container = "custom_widget_container_7"
    }
    
    immediate = {
        scope:journal_entry = {
            add_com_dlc_icon = {
                dlc = dlc_magic_gate
            }
        }
    }
    # some more journal definition
}
```

## Characters with Opinions
- **Injection Name:** `com_journal_entry_characters`
- **Recommended Anchor:** `custom_widget_container_1`
- **Screenshots:** [Single Character with Opinion](images/journal_entries/example_journal_entry_character_01.png), [Multiple Characters without Opinions](images/journal_entries/example_journal_entry_character_02.png)

To add one or more characters to a journal entry you need
to add them to a variable list called `com_journal_characters` in
the immediate block of a journal entry.

Here is an example where a countries ruler is added to a journal entry, but theoretically you can add whoever you want:
```
je_example_entry = {
	...
    widget = {
        gui = "gui/com_journal_injects/injects.gui"
        name = "com_journal_entry_characters"
        container = "custom_widget_container_1"
    }
    
	immediate = {
	    # Adding the ruler to the journal
        scope:journal_entry = {
            add_to_variable_list = {
                name = com_journal_characters
                target = prev.ruler
            }
        }
	}
	...
}
```

### Opinions

Characters in journal entries can also have opinions.
To define them, you need to set the flag variable `com_opinion` on the character.
```
set_variable = {
    name = com_opinion
    value = flag:gui_character_opinion_example
}
```
The text behind `flag:` is a localization key (See [com_gui_l_english.yml](../localization/english/com_gui_l_english.yml)).

**NOTE: Only one opinion can be set on a character at a time. So if you are using a character in multiple journal entries be aware of this.**

## Wrap Modifiers
- **Injection Name:** `com_journal_entry_header`
- **Recommended Anchor:** `custom_widget_container_je_icon`

This causes the journal modifiers to wrap in lines of 5. Now, up to 15 modifiers looks fine and don't just cross the screen.

## Progress Bar Styling
- **Injection Name:** `com_journal_entry_progress_bars`
- **Required Anchor:** `com_custom_widget_container_scripted_progress_bars` (This may change in the future)
- **Screenshots:** [Example drifting progress bar](images/journal_entries/example_progress_bars.png)

Scripted progress bars can be styled with a color, a drift effect, and a target marker, all dynamically settable and unsettable. For more details, see the [progress bar documentation](PROGRESS_BARS.md)

## EU5 Style Situation Journal Entries
- **Injection Names:**
  - `com_situation_header_versus`
  - `com_situation_header_single`
  - `com_situation_header_no_side`
  - `com_situation_header_text`
  - `com_situation_victory_conditions`
  - `com_situation_faction_list`
- **Screenshots:** [No sides](images/journal_entries/example_situations_no_sides.jpg), [One sides](images/journal_entries/example_situations_one_side.jpg)

**NOTE: CMF Situations do not work with the new global journal entries. Help us fix this by contributing!**

Situations are meant to model international events, such as clashes between factions, pandemics, and more.

Each situation can have multiple, different journal entries associated with it and provides a tool to model complex power struggles.

In the background, situations are Journal Entries with a few extra variables and a whole new UI.
This means using them should come natural to modders who have already used those.

Situations were inspired by [EU5](https://forum.paradoxplaza.com/forum/developer-diary/tinto-talks-70-2nd-of-july-2025.1823383/).

[The usage documentation can be found here.](SITUATIONS.md)

[While the script documentation can be found here.](SITUATIONS_SCRIPT_DOCS.md)

## Building
- **Injection Name:** `com_journal_entry_building`
- **Recommended Anchor:** `custom_widget_container_1`
- **Screenshots:** [Example](images/journal_entries/example_building.png)

To add a building you will need to set the building scope to a journal entry variable called `com_journal_entry_building` in the immediate block of a journal entry.

Here is an example where a railway is added to a journal entry, but theoretically you can add whatever building you want:
```
je_example_entry = {
	...
    widget = {
        gui = "gui/com_journal_injects/injects.gui"
        name = "com_journal_entry_building"
        container = "custom_widget_container_1"
    }
    
	immediate = {
	    # Adding railway building to the variable
		random_scope_building = {
			limit = {
				is_building_type = building_railway
			}
			scope:journal_entry = {
				set_variable = {
					name = com_journal_entry_building
					value = prev
				}
			}
		}
	}
	...
}
```

## Common/Shared CMF Journal Widgets
`/gui/com_journal_injects/com_shared_widgets.gui`

### Available as Widgets & Types:
- `com_journal_modifiers_container`- [Screenshot](/docs/images/journal_entries/type_com_journal_modifiers_container.png)
- `com_journal_scripted_buttons` - [Screenshot](/docs/images/journal_entries/type_com_journal_scripted_buttons.png)
- `com_journal_reason_text` - Contains blocks for visibility, text, and background
- `com_journal_involved_countries`- Contains block for element header
### Available as Types:
- `com_journal_scripted_button_item` - Resized to 460x38

## International Organizations Framework
`/gui/com_journal_injects/interorg_widgets.gui`

See [International Organizations](docs/INTERNATIONAL_ORGANIZATIONS.md) for usage notes.
### Available as Widgets:
- `widget_com_international_organization_base`
- `widget_com_supranational_organization`
- `widget_com_regional_organization`
- `widget_com_religious_organization`
- `widget_com_non_governmental_organization`
- `widget_com_sporting_organization`
- `widget_com_international_conference`
### Available Types:
- `com_international_organization_panel`
- `com_international_organization_details`
- `com_international_organization_panel`

## International Situations Framework
`/gui/com_journal_injects/situation_widgets.gui`

See [International Situations](docs/INTERNATIONAL_SITUATIONS.md) for usage notes.
### Available Widgets:
- `widget_com_international_situation`
- `widget_com_international_situation_illustration`
- `widget_com_international_situation_phase_information`
- `widget_com_international_situation_involved_countries`
- `widget_com_international_situation_outcome_container`
- `widget_com_international_situation_phase_progress`
### Available Types:
- `com_international_situation_header`
- `com_international_situation_illustration`
- `com_international_situation_phase_information`
- `com_international_situation_timeout`
- `com_international_situation_involved_countries`
- `com_international_situation_outcome_container`
- `com_international_situation_phase_progress`

## Base Game Journal Elements
`/gui/com_journal_injects/victoria_base_widgets.gui`

These are the base game journal entry elements.
### Available as Widgets & Types:
- `com_default_journal_buttons`
- `com_default_journal_reason`
- `com_default_journal_timeout`