# Community Mod Framework
![banner.png](docs/banner.png)

The Community Mod Framework aims to support compatibility between different mods.
Including GUI, Political Movements, Parties, Mod detection triggers and much more.

## Steam Page
https://steamcommunity.com/sharedfiles/filedetails/?id=3385002128

## Contents
* [Setting Dependency](#setting-dependency)
* [Debug Features](#debug-features)
* [Political Movements](#political-movements)
    * [Adding New Ideologies](#adding-new-ideologies)
    * [Modifying Movement Weights](#modifying-movement-weights)
* [GUI Framework](#gui-framework)
    * [Alternative Event Windows](#alternative-event-windows)
    * [Hiding Objective Header](#hiding-objective-header)
    * [Custom Social Hierarchies](#custom-social-hierarchies)
    * [Sidebar Button](#sidebar-button)
    * [Character Animation, Camera and Environment](#character-animation-camera-and-environment)
    * [Custom Owner Buildings](#custom-owner-buildings)
    * [Multi-line Production Methods](#multi-line-production-methods)
    * [Journal Extensions](#journal-extensions)
      * [Hide/Show Journal Entry Groups](#hideshow-journal-entry-groups)
      * [EU5 Style Situation Journal Entries](#eu5-style-situation-journal-entries)
      * [Progress Bar Styling](#progress-bar-styling)
      * [Characters in Journal Entry](#characters-in-journal-entry)
* [Structs](#structs)
    * [Creating a new Struct](#creating-a-new-struct)
    * [Setting Variables on a Struct](#setting-variables-on-a-struct)
    * [Destroying a Struct](#destroying-a-struct)
* [Fixing Variable Errors](#fixing-variable-errors)
* [Extracting Character Names](#extracting-character-names)
* [Dictionaries](#dictionaries)
* [Float Arrays](#float-arrays)
* [Parties](#parties)
* [Community Mod Triggers](#community-mod-triggers)
* [Keybinds](#keybinds)
* [Additional Modifier Icons](#additional-modifier-icons)
* [Weekly Event Framework](#weekly-event-framework)
* [Heir Blocker](#heir-blocker)
* [Formation Event Blocker](#formation-event-blocker)
* [Regency Blocker](#regency-blocker)
* [Built-In Universal Names Compatibility](#built-in-universal-names-compatibility)
* [Power Bloc Disbander](#power-bloc-disbander)

# Setting Dependency

To set this mod as a dependency to your own mod, you will need to add this to your `metadata.json` file:
```
  "relationships" : [
    {
      "rel_type" : "dependency",
      "id" : "com.github.Victoria-3-Modding-Co-op.Community-Mod-Framework",
      "display_name" : "Community Mod Framework",
      "resource_type" : "mod",
      "version" : "1.*"
    }
  ]
```
**Also remember to add the mod to your required items on your own mods steam page.**

# Debug Features

- The keybinding `CTRL + ALT + D` toggles the global variable `com_debug`. This can be used to enable or disable debug content like debug Decisions or Events.
- The keybinding `CTRL + ALT + Q` will toggle the game in and out of debug mode. This executes the `debug_mode` console command. This will break achievements if used.

# Political Movements

CMF overwrites vanilla Political Movement definitions with versions that have scripted triggers to aid in mod compatibility

## Adding New Ideologies
To add dummy ideologies from your mods into political movements, allowing them to spawn with the appropriate mod enabled:
* Add a dummy ideology to CMF with the same name as your mod ideology in a file named `00_dummy_ideologies_<your_mod>`.
* Assign the ideology to the appropriate political movements (and scripted triggers if needed).
* Ensure the ideologies in your mod are in a file that will overwrite the dummy one (see [File Naming](.github/CONTRIBUTING.md#file-naming)).
* Your mod will overwrite the ideology definition and allow it to spawn in the specified political movements.

## Modifying Movement Weights
Depending on whether your mod must depend on CMF, or functions in a standalone capacity, what you do may be slightly different.
* Work out where you need to either add or multiply values for a particular movement.
* Add a bloc to the CMF movement that looks like:
```
# Your_Mod
add/multiply = {
	value = <your_mod>_<movement_type>_<movement_section>_<function>
	desc = "YOUR_LOCALIZATION"
}
```
> **For example:**  
> `mog_plp_movement_minority_rights_pop_support_weight_mult`  
> **Is made up of:**  
> mod: mog_plp_  
> type: movement_minority_rights_  
> section: pop_support_weight_  
> function: mult
* Then; create a file in common\script_values called `00_<your_mod>_movement_values`.
* Define all values you want added in this file, = 0 for `add` and = 1 for `mult` (as seen in `00_mog_plp_movement_values`)
* Define the values again in your own mod, with all the maths for what you need, in a file that will overwrite the dummy one. (see [File Naming](.github/CONTRIBUTING.md#file-naming))
* *Optional:* If your mod will depend on CMF (cannot work without CMF) you can define the maths in your `00_<your_mod>_movement_values` file (as seen in `00_anzfp_movement_values`) as long as you have a scripted trigger for when your mod is active. (see [Community Mod Triggers](#community-mod-triggers))


# GUI Framework

Current Scope:
1) A "sidebar" scripted widget to deconflict mods that want to add custom sidebar buttons. (Credit to Bahmut, LordR, & Alexedishi)
2) Modification to the GUI template fullscreen_hide to hide the outliner whenever a scripted widget window is open. (Credit to Bahmut & Alexedishi)
3) Modification to objective_types to add a scrollbar to the objectives screens. (Credit to Bahmut, KarafuruAmamiya, & Xier)
4) Modification to society_panel to add the ability to use custom social hierarchies. (Credit to Bahmut)
5) Integration of the "Modded DLC Framework" (Credit to 1230James)
6) Modification to the outliner and journal GUIs to hide custom objectives during gameplay (Credit to Taylor)
7) Several custom event windows for extra flavor (Credit to Bananaman & Klein for the OG superevent window, Credit to Alexedishi & Bahmut for most others)
8) Modification to Journal Entry GUI to allow players to show characters (Credit to Bahmut and Mori)
9) Integration of the "Multi-line PM Framework" (Credit to 1230James)
10) Alerts can now open custom windows (Credit to Bahmut)
11) More than three local goods can now be shown in state building panel correctly (Credit to Bahmut)
12) Variables can be set on journal entries to change the colors of certain progress bars (Credit to Alexedishi)
13) Framework to create EU5 style situation journal entries (Credit to Bahmut & CaesarVincens)
14) Support for more than 3 unit types in GUI (Credit to lil jimmy & 1230James)
15) Support for more mobilization options per category in GUI (Credit to lil jimmy & 1230James)
16) Configurable Character portraits (Credit to Bahmut & CaesarVincens)
17) Journal progress bars can be styled with 'drift' and target effects (Credit to CaesarVincens, idea from MasterOfGrey)
18) Framework for a two character journal entry (Credit to Bagel)

## Alternative Event Windows

Modded event windows are available and can be used by passing this in your event:
```
gui_window = <event_window_key>
```
### Available Event Windows

Character Windows:
- [event_window_1char_adventure](docs/event_windows/event_window_1char_adventure.png)
- [event_window_2char_adventure](docs/event_windows/event_window_2char_adventure.png)
- [event_window_2char_duel](docs/event_windows/event_window_2char_duel.png)
- [event_window_highlander](docs/event_windows/event_window_highlander.png)
- [event_window_3char_selection](docs/event_windows/event_window_3char_selection.png)

Superevent Windows:
- [event_window_superevent_newspaper](docs/event_windows/event_window_superevent_newspaper.png)
- [event_window_superevent_newspaper_full](docs/event_windows/event_window_superevent_newspaper_full.png)
- [event_window_superevent_classic](docs/event_windows/event_window_superevent_classic.png)
- [event_window_superevent_classic_full](docs/event_windows/event_window_superevent_classic_full.png)
- [event_window_superevent_modern](docs/event_windows/event_window_superevent_modern.png)
- [event_window_superevent_modern_full](docs/event_windows/event_window_superevent_modern_full.png)
- [event_window_superevent_crisis](docs/event_windows/event_window_superevent_crisis.png)

Widescreen Windows:
- [event_window_widescreen_classic](docs/event_windows/event_window_widescreen_classic.png)
- [event_window_widescreen_newspaper](docs/event_windows/event_window_widescreen_newspaper.png)

Special Windows:
- [event_window_ethics](docs/event_windows/event_window_ethics.png)
- [event_window_com_focus_text](docs/event_windows/event_window_com_focus_text.png)

Paper Style Window:
- [com_event_window_letter_simple](docs/event_windows/com_event_window_letter_simple.png)
- [com_event_window_letter_image](docs/event_windows/com_event_window_letter_image.png)
- [com_event_window_letter_paper](docs/event_windows/com_event_window_letter_paper.png) (Default View)
- [com_event_window_letter_paper](docs/event_windows/com_event_window_letter_paper_transcribed.png) (Transcribed View)
- [com_event_window_telegram](docs/event_windows/com_event_window_telegram.png)
- [com_event_window_newspaper](docs/event_windows/com_event_window_newspaper.png)

Europa Universalis V Style Windows:
- [event_window_europa_classic](docs/event_windows/event_window_europa_variants.png)
- [event_window_europa_1_char](docs/event_windows/event_window_europa_variants.png)
- [event_window_europa_2_char](docs/event_windows/event_window_europa_variants.png)

### Usage Notes
- For ease of use, any modded windows with characters will expect a character scope for the arguments `left_icon = scope:some_character`, `right_icon = scope:some_character` and `center_icon = scope:some_character` if the event has three characters. Just like the vanilla events do.
- `event_window_duel` also has an optional progress bar that will display below the flavor text
  - This is activated by setting the variable com_event_window_2char_duel_var
  - The progress bar will pull the value from this variable; it has a maximum of 100 and a minimum of 0
- `event_window_crisis` uses six character scopes saved as variables; documentation is provided in the `eventwindow.gui` file
- `event_window_com_focus_text` needs an additional localization key `<event_id>.st` to define the header for the buttons

### Newspaper Events
The Newspaper event allows overwriting of the header texts.
There are three optional localization keys that can be defined to overwrite the following values:
- `event_name.1.sub_title` - Newspaper name (default: Western Mail)
- `event_name.1.sub_left` - Topbar left text (default: No. 512)
- `event_name.1.sub_right` - Topbar right text (default: ONE PENNY)
- `event_name.1.sub_middle` - Topbar middle text (default: The current game date)

For the newspaper image,
the recommended minimum size is 440x292px,
or a multiple of that to keep the aspect ratio correct.

### Ethic Events
- Ethic events can have up to 9 buttons
- This is the order they are created in:
  - Center Button (Required)
  - Top & Bottom
  - Left & Right
  - Bottom Right & Top Left
  - Bottom Left & Top Right
- The Buttons do not support classical text but are optimized for texticons (i.e. `@innovation!`)

## Hiding Objective Header

The Objective header can be hidden by setting the global variable `community_gui_objective_var` like this:
```
set_global_variable = community_gui_objective_var
```

## Custom Social Hierarchies

To enable a custom social hierarchy you have to execute this effect in a countries scope:
```
set_variable = {
    name = custom_social_hierarchy
    value = active_law:lawgroup_of_your_hierarchy
}
```
**I recommend doing this in the history file of a country `common/history/countries`**

## Sidebar Button

Screenshot: [Example](docs/example_sidebar_01.png)

How to add a new button to the sidebar.

First create an ideology in the `common/ideologies/` folder (See [example_button.txt](common/ideologies/example_button.txt)).
The icon set on the ideology is the icon shown on your button.
**Important here is that this ideology is never triggered or shown!**

Then we need a scripted gui in the `common/scripted_guis/` folder corresponding to the button (See [example_button_sgui.txt](common/scripted_guis/example_button_sgui.txt))

We then link those two via the localization of the ideology.
Localizations can be found in `localization/<language>/`.
Button ideologies have three localization keys: \<ideology\>, \<ideology\>_desc and \<ideology\>_tooltip

The key \<ideology\> should contain the name of your scripted_gui.
And the key \<ideology\>_desc contains the name shown when hovering over the button.
The \<ideology\>_tooltip is optional and will be shown as a tooltip if you hover over the button (See [com_gui_l_english.yml](localization/english/com_gui_l_english.yml)).
**Good practice here is to name the ideology and the scripted gui the same, so even if you do not set the localization key for a language, the correct scripted gui is triggered!**

### Adding the Button

And at last we need to add the button to the sidebar.
This is done by adding your ideology as a flag to a list.

#### Global

To add the buttons for all countries:
```
add_to_global_variable_list = {
    name = custom_button_list_flag
    target = flag:gui_sidebar_example_button
}
```

#### Country

To add the button for only one country:
```
add_to_variable_list = {
    name = custom_button_list_flag
    target = flag:gui_sidebar_example_button
}
```

This effect can be run wherever you want, like a journal entry or an event.
One possibility is to run it in `common/history/global/` (See [enable_example_button.txt](common/history/global/enable_example_button.txt)).

### GUI Window Visibility

When a sidebar button is clicked the following GUI variable is set to your scripted gui name: `com_open_window`
In your custom window you should check for it like this (with your scripted gui name):
```
visible = "[GetVariableSystem.HasValue('com_open_window', 'gui_sidebar_example_button')]"
```
If you want to close your window again you can do it by clearing the variable like this:
```
onclick = "[GetVariableSystem.Clear('com_open_window')]"
```

### Fullscreen GUI

If your GUI is fullscreen you will also need to set and remove the following GUI variable: `com_fullscreen`
The best solution is to use the GUI state system like this:
```
state = {
    name = _show
    # Toggle doesn't work here as it is still toggled on reload, so I have to set it instead
    on_finish = "[GetVariableSystem.Set('com_fullscreen', 'com_fullscreen')]" 
}
state = {
    name = _hide
    on_finish = "[GetVariableSystem.Clear('com_fullscreen')]"
}
```
Setting it will hide the base game GUI and removing it will show the base game GUI again.

### Custom Alerts

When you create an alert, you also need to define an action in a loc key.
This action string will be written into the GUI variable `com_alert_action`.

You can then check for this in your custom GUI like this:
```
visible = "[GetVariableSystem.HasValue('com_alert_action', 'Example Panel')]"
```
OR
```
visible = "[GetVariableSystem.HasValue('com_alert_action', Localize('mod_alert_send_to_example_panel'))]"
```
If you have multiple alerts which should all open the same panel you can use full line substitution:
```
 alert_first_alert_name_action: "$mod_alert_send_to_example_panel$"
 alert_second_alert_name_action: "$mod_alert_send_to_example_panel$"
 alert_third_alert_name_action: "$mod_alert_send_to_example_panel$"
 
 mod_alert_send_to_example_panel: "Example Panel"
```
> **NOTE:** If using this in a widget; you will need a scripted widget definition in `gui\scripted_widgets\` to load your widget.

## Character Animation, Camera and Environment

To change a characters animation,
camera and environment CMF provides a series of scripted effects to set them:
* `set_com_character_animation` - sets only the animation
* `set_com_character_camera` - sets only the camera
* `set_com_character_environment` - sets only the environment
* `set_com_character_portrait` - sets all three elements
* `set_com_character_portrait_everywhere` - sets all three elements for every portrait of the character

Another scripted effect `remove_com_character_portrait` removes all three elements. Individual elements can be removed with `remove_variable = com_character_"element"`

All of these effects must be run in the scope of the character.

> **NOTE** These effects will change the character portrait in all COM event windows and `set_com_character_portrait_everywhere` does so EVERYWHERE the character is shown and will be PERMANENT unless removed! So use this effect with caution.

The `set_com_character_portrait` and `set_com_character_portrait_everywhere` effects have three required parameters:
- `animation` - A localization key containing the animation name
- `camera` - A localization key containing the camera name
- `environment` - A localization key containing the environment name

The other three setting effects have only one of those parameters, matching the effect's name. `remove_com_character_portrait` has no parameters.

CMF has predefined the base game animations, cameras, and environments.
They can be found [here](localization/english/com_character_portrait_l_english.yml).

> **NOTE** Either localization or the "base" value can be used; i.e. both `com_animation_idle` and `idle` produce the same pose - as long as `idle` is not also a localization key.

If you want to use custom values for modded animations, cameras, and environments,
you can simply define them as localization keys, like CMF already does.

### Usage Example

One of the main use cases for this feature is posing characters in specific events.
Here is a very simple example event:
```
some_event.1 = {
	# ... event stuff

    gui_window = event_window_1char_tabloid
    left_icon = root.ruler

	immediate = {
		ruler = {
            set_com_character_portrait = {
                animation = com_animation_idle
                camera = com_camera_lifestyles
                environment = com_environment_agitator_main
            }
		}
	}

    after = {
        ruler = {
            remove_com_character_portrait = yes
        }
    }
    
	# ... event stuff
}
```

## Custom Owner Buildings

To add a new custom owner building type just add it to the global list `com_custom_owner_buildings` like this:
```
add_to_global_variable_list = {
    name = com_custom_owner_buildings
    target = bt:building_university # Use your building here
}
```
This can be done in history global or wherever you want this effect to run.

## Multi-line Production Methods

MPM edits certain panels in the UI to make them display extra PM groups by wrapping them around instead of adding the extra ones on the same line and causing them to appear off the edge of the panel or under other text and buttons. MPM provides changes to the following files:
```
gui/building_details_panel.gui
gui/goods_state_panel.gui
gui/production_methods.gui
gui/building_browser_panel.gui
gui/map_list_panel.gui
```
**NOTE: Note that military buildings, such as barracks and naval bases, are NOT INTENDED TO BE USED WITH MPM due to the new unit graphics being displayed alongside the PMGs which now take up most of the space that the extra PMGs would overflow into.**

## Journal Extensions
CMF adds several extensions for the journal system, including hidden entries, EU5-alike situations, and more.

### Hide/Show Journal Entry Groups

This allows for hiding and showing any Journal Entry Group.

Usage:
`com_hide_journal_entry_group = { name = je_group_historical_content }` 
This would hide all National Agenda (`je_group_historical_content`) Journal Entries.

`com_show_journal_entry_group = { name = je_group_historical_content }` 
This would show them again.

### EU5 Style Situation Journal Entries
**NOTE: CMF Situations are not yet tested with the new global journal entries and may not work correctly**

Situations are meant to model international events, such as clashes between factions, pandemics, and more.

Each situation can have multiple, different journal entries associated with it and provides a tool to model complex power struggles.

In the background, situations are Journal Entries with a few extra variables and a whole new UI.
This means using them should come natural to modders who have already used those.

Situations were inspired by [EU5](https://forum.paradoxplaza.com/forum/developer-diary/tinto-talks-70-2nd-of-july-2025.1823383/).

[The usage documentation can be found here.](docs/SITUATIONS.md)

[While the script documentation can be found here.](docs/SITUATIONS_SCRIPT_DOCS.md)

### DLC Icons in Journal Entries

To add DLC/Mod information to a journal entry, CMF offers the scripted effect `add_com_dlc_icon`.

It needs to be run in the journal entry scope.
The best place for that is the `immediate` block of a journal entry:
```
je_some_journal = {
    # journal definition
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

### Characters in Journal Entry

Screenshots: [Single Character with Opinion](docs/example_journal_entry_character_01.png), [Multiple Characters without Opinions](docs/example_journal_entry_character_02.png)

To add one or more characters to a journal entry you need
to add them to a variable list called `com_journal_characters` in
the immediate block of a journal entry.

Here is an example where a countries ruler is added to a journal entry, but theoretically you can add whoever you want:
```
je_example_entry = {
	...
	immediate = {
		every_scope_character = {
			limit = {
				exists = this
				is_character_alive = yes
				is_ruler = yes
			}
			save_temporary_scope_as = list_character
			scope:journal_entry = {
				add_to_variable_list = {
					name = com_journal_characters
					target = scope:list_character
				}
			}
		}
	}
	...
}
```

### Two Characters Journal Entry (country rulers)

Screenshots: [Britain and EIC as example](docs/two_char_je_example.png), 

To use the two characters in a journal entry you must use the following variables:

com_style_two_characters -> in immediate block, used to designate a je as using this gui

ex. scope:journal_entry = {
			set_variable = {
            	name = com_style_two_characters
        	}
		}

com_character_country_right -> in immediate block, used to designate what country's ruler is on the right side

ex. scope:journal_entry = {
			set_variable = {
            	name = com_character_country_right
           		value = c:GBR
        	}
		}

com_character_country_left -> in immediate block, used to designate what country's ruler is on the left side

ex. scope:journal_entry = {
			set_variable = {
            	name = com_character_country_left
           		value = c:BIC
        	}
		}
  
com_character_country_right_title -> in immediate block, used to designate the text on the top right

ex. scope:journal_entry = {
			set_variable = {
            	name = com_character_country_right_title
           		value = flag:british_government_text
        	}
		}

com_character_country_left_title -> in immediate block, used to designate the text on the top left

ex. scope:journal_entry = {
			set_variable = {
            	name = com_character_country_left_title
           		value = flag:company_shareholder_text
        	}
		}

Here is an example where the ruler of Great Britain and the East India Company are used, but theoretically you can use whatever country you want to:
```
je_example_entry = {
	...
	immediate = {
		scope:journal_entry = {
			set_variable = {
            	name = com_style_two_characters
        	}
		}

		scope:journal_entry = {
			set_variable = {
            	name = com_character_country_right_title
           		value = flag:british_government_text
        	}
		}

		scope:journal_entry = {
			set_variable = {
            	name = com_character_country_left_title
           		value = flag:company_shareholder_text
        	}
		}

		scope:journal_entry = {
			set_variable = {
            	name = com_character_country_right
           		value = c:GBR
        	}
		}

		scope:journal_entry = {
			set_variable = {
            	name = com_character_country_left
           		value = c:BIC
        	}
		}
	}
	...
}
```

### Removing Icons in Journal Entries
If you want to remove the icon from the top of the journal entry screen for any reason CMF has a feature to do so.

To remove the icon from a journal entry the following variable is needed:

`com_remove_journal_icon-` -> in the immediate block

Here is an example:

```
je_example_entry = {
	...
	immediate = {
		scope:journal_entry = {
			set_variable = {
        name = com_remove_journal_icon
      }
		}
	}
	...
}
```




### Progress Bar Styling
Scripted progress bars can be styled with a color, a drift effect, and a target marker, all dynamically settable and unsettable. For more details, see the [progress bar documentation](/docs/Progress_bars.md)

> **NOTE**  The following custom color styles still work, but have been superseded by the more advanced progress bar framework.

These work by setting specific variables in the journal entry scope. These will change which progress bar is displayed. Currently, the following variables are used:
- `com_double_bad_gold_marker` -- replaces the journal entry marker in double_sided_bad with the marker from double_sided_gold
- `com_double_bad_white_bar` -- replaced double_sided_bad with white_progressbar_horizontal
- `com_double_bad_gold_bar` -- replaced double_sided_bad with gold_progressbar_horizontal
- `com_bear_spray_applied` -- removes the bear and lion icons from double_sided_gold and resizes the progress bar

### Wrap Journal Modifiers

This works by setting the variable `com_flex_je_modifiers` in the journal entry scope. This causes the journal modifiers to wrap in lines of 5. Now, up to 15 modifiers looks fine and don't just cross the screen.

#### Opinions

Characters in journal entries can also have opinions.
To define them, you need to set the flag variable `com_opinion` on the character.
```
set_variable = {
    name = com_opinion
    value = flag:gui_character_opinion_example
}
```
The text behind `flag:` is a localization key (See [com_gui_l_english.yml](localization/english/com_gui_l_english.yml)).

**NOTE: Only one opinion can be set on a character at a time. So if you are using a character in multiple journal entries be aware of this.**


# Structs

CMF now allows for structs that can be used to categorize variables. They are especially meant to be used with GUI but can be used anywhere.

## Creating a new Struct
This command needs to run in a country scope:
```
create_struct = {
	struct_scope = test_struct
	struct_type = 1
}
```
The `struct_scope` is the output scope of the created struct that you can use to add variables or add the struct to a list.
The `struct_type` is a type that can be set on the struct. To use "names" here, you can define Script Values to use as a `struct_type`.

## Setting Variables on a Struct
After creating a struct, you can use its scope to set variables on it. Or use it as a variable in another scope:
```
scope:test_struct = {
	set_variable = {
		name = some_example_variable
		value = 42
	}
	set_variable = another_example_variable
}
```
```
# Country Scope Example
c:GBR = {
	set_variable = {
		name = some_variable_with_a_struct
		value = scope:test_struct
	}
}
```

## Destroying a Struct
A struct will live **forever** and can become a performance issue.
So you need to manage their lifetime if you are using them for temporary applications.

You can destroy them using this scripted effect:
```
destroy_struct = {
	struct = var:some_struct
}
```
```
destroy_struct = {
	struct = scope:some_struct
}
```

**NOTE: Internally structs are immortal Characters in the void. This means potential textures for the GUI could be set using a Characters ideology.**

# Fixing Variable Errors
When you are using a variable only in the GUI or in localizations, the game creates errors and spams the error log.
To avoid this, there is a helper scripted effect in CMF that suppresses these types of errors.
```
fix_variable_error = {
	variable = variable_or_flag_name
}
```
Usage examples can be found [here](events/com_debug.txt).

**NOTE**: This works for both **variables** and **flags**.

# Extracting Character Names
CMF has the ability to set character names as **flag** variables on the characters scope.
To do this just add the character to the `com_character_name_extract` global list.

In the background a GUI hack will be used to set the following variables on the character:
- `com_name_full`
- `com_name_full_no_formatting`
- `com_name_full_title`
- `com_name_full_title_no_formatting`
- `com_name_first`
- `com_name_first_no_formatting`
- `com_name_last`
- `com_name_last_no_formatting`

# Dictionaries

Dictionaries store numeric key value pairs.
You can use `set_dict_id` to create unique IDs in other scopes which support variables which can then be safely used as dictionary keys.

Keys can be any number from 0 to 2047  
Values can be any number from -45035996273.70496 to 45035996273.70495  

⚠️ Dictionaries store both the key and value in a single number using bit shifts, you must be careful to ensure your keys and values do not overflow.
For performance reasons there are no internal safety checks. Using numbers outside of these ranges will result in undefined behavior.

Alternatively, you can use a more specialized scope value map. This allows mapping any scope to numeric values. It uses dictionaries behind
the scenes, so is limited to 2048 keys and the same value range. Scope value maps do not support removing elements once they are added! Attempting
to remove elements from the map will result in undefined behavior.

## Set
```
add_to_dict = {
  dict  = dictionary_name
  key   = numeric_key
  value = numeric_value
}

add_to_scope_value_map = {
  name  = map_name
  key   = scope:any_scope
  value = numeric_value
}
```
## Get
```
every_in_list = {
  variable = dictionary_name
  limit = {
    this.kvp_to_key = numeric_key
  }
  multiply = this.kvp_to_value
}

# Where scripted effects are supported
# `scope:key` and `scope:value` are available inside the limit and effect blocks
every_in_scope_value_map = {
  variable = map_name
  limit = " # Quotes not braces
    scope:key = {
      ...
    }
  "
  effects = " # Quotes not braces
    add = scope:value
  "
}

# Where scripted effects are not supported (eg: math blocks)
save_temporary_scope_as = base
every_in_list = {
  variable = map_name
  save_temporary_scope_as = kvp
  scope:base = {
    ordered_in_list = {
      variable = map_name_keys
      position = scope:kvp.kvp_to_key
      save_temporary_scope_as = key
    }
  }
  if = {
    limit = {
      scope:key = { ... }
    }
    subtract = scope:kvp.kvp_to_value
  }
}
```
## Remove
```
remove_dict_variable = {
  variable = dictionary_name
  key = numeric_key
}
```
## IDs
```
every_country = {
  set_dict_id = yes # Generates a new ID for this scope if one does not already exist
  save_temporary_scope_as = country
  every_scope_culture = {
    add_to_dict = {
      dict  = dictionary_name
      key   = scope:country.var:dict_id # The generated ID is safe to use as a unique key
      value = numeric_value
    }
  }
}
```
# Float Arrays
Floatarrays are a custom data type implemented through scripted variables, enabling efficient indexed storage similar to float arrays in traditional programming languages. Credit to BigBruh and CaesarVincens.

See [the documentation page for details](/docs/floatarray.md) on effects and triggers.

# Parties

For naming, you need to include loc keys to avoid load-up error. These can be blank and overwritten by your own mod. 

# Community Mod Triggers

## Usage
Request to have CMF add a trigger for your mod into the CMF compatibility file `01_community_mod_compatibility_triggers.txt`.
This file contains the scripted triggers all set to return false by default. This is intentional. Your trigger should look like this:
```
YOURMODNAME_is_active_trigger = {
   always = no
}
```
Create another file with the name `zz_YOURMODNAME_compatibility_triggers.txt` in the `/common/scripted_triggers` folder of your mod,
that contains the following:
```
YOURMODNAME_is_active_trigger = {
   always = yes
}
```

## Currently Included
* Anno 1836
* Australia & New Zealand Flavor Pack
* Basileia Romaion
* Better Decrees
* Better Politics Mod
* Community Outfit Mod
* East Asian Clothes Patch
* Gas, Guns, Garb, & Grub
* Gilded Age
* Greece, Byzantium, & the Balkans Flavor
* Grey's Little Reworks
* Hail, Columbia!
* James's Korea Flavor Pack
* James's Pop Clothing Tweaks
* Manaflow: Ankaris Arrival
* War Goal Framework
* Morgenrote: Dawn of Flavor
* Newspapers Mod
* Rally Round the King
* States That Make Sense
* Western Clothes: Redux

# Keybinds

You can take a free keybind by doing this:
1) Check default.profile and see which keybind is still free. You can find free keybinds at the bottom of the file.
2) Add input_action = "input_$your_input$" to the button you want to use it for.
3) Add a localization for your button to "localization/language_x/replace" and use the name of the input_action.

Note: It is possible to add additional keybinds if there are no keybinds left.

# Additional Modifier Icons

Over 100 new modifier icons for more variety. Credit to Caelreader. PSD template available in docs.
Screenshot: [Modifier Icons](docs/timed_modifier_icons.png)

# Weekly Event Framework

This is a framework to allow for a weekly firing script event on any day of the week, without a hidden journal entry being used.

To use:
1. Create a new `on_monthly_pulse` or reuse an existing one.
2. Set it up like in `com_weekly_on_action.txt`:
3. Add your own `on_action` to the `on_monthly_pulse` from step 1.
4. Add the `com_run_weekly_event_country_effect` into this new on_action and set the two parameters. Example: `com_run_weekly_event_country_effect = { weekday = 1 on_action = another_on_action }`. Weekday decides the weekday ranging from 0 (Sunday) to 6 (Saturday).
5. Define your new on_action (`another_on_action` in the example in 4.)

# Heir Blocker

Mods interested in having specially generated heirs (especially for things like historical heirs) in countries with hereditary transfers of power can utilize the Heir Blocking Framework's feature to prevent the visual appearance of an heir. That is, while the heir technically is generated (as there is no useful way to prevent that), we can intercept the new heir and remove them whilst blocking the "Heir Born" message at the same time, giving the *appearance* to the user that no heirs are actually being born.

To use it, just set a variable named `no_heirs` in the country that should have its heirs blocked; e.g.,
```
c:GBR = {
    set_variable = no_heirs
}
```
Modified on action logic for heir births will take care of the rest automatically.

To allow randomly-generated heirs again, simply remove the variable.

Note:
1. No considerations have been made regarding any failsafes. You are solely responsible for unblocking heirs later, even if the country switches away from a government type with hereditary transfer of power.
2. Heirs created via `create_character` and heirs set via `set_heir` are *not* blocked, as they do not count as a "natural" heir birth. This means the variable does not need to be briefly unset when generating or setting heirs via script, such as for historical heirs.

# Formation Event Blocker

This allows for blocking the formation events that occur whenever the player forms a country. This can be used for blocking the events' effect of adding claims to all homeland states which is vanilla behavior.

To use it, just set a variable named `com_no_formation_events` in the country that should have formation events blocked; e.g.,
```
c:GRE = {
    set_variable = com_no_formation_events
}
```

To allow formation events again, simply remove the variable.

Notes:
1. No considerations have been made regarding any failsafes. You are solely responsible for unblocking formation events later, even if the country successfully completes additional formations.
2. Changing country via the `change_tag` effect will **not** remove the `com_no_formation_events`variable.

# Regency Blocker

This allows for preventing `on_new_ruler` from firing as needed. This on action is very aggressive and will interrupt mid-event chain and create a regency even if you immediately replace your ruler immediately after an effect that removed the previous ruler.

To use it, just set a variable named `com_no_regencies` in the country that should have regencies blocks; e.g.,
```
c:GRE = {
    set_variable = com_no_regencies
}
```

To allow regencies again, simply remove the variable.

Notes:
1. No considerations have been made regarding any failsafes. You are solely responsible for unblocking regencies later, even if the country changes government types and transfer of power.
2. Changing country via the `change_tag` effect will **not** remove the `com_no_regencies` variable.
3. Setting the variable *after* removing the ruler will **not** prevent the regency on action from firing.

# Built-In Universal Names Compatibility

CMF sets up seamless compatibility with [FUN's Universal Names mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2880875193) for its own use in certain GUI windows, but it can be used by any other mods as well.

The Universal Names mod, among a few other things, corrects the display of full names for characters belonging to cultures whose full name order is `Last-First`, as opposed to `First-Last`, improving the presentation of relevant cultures, especially East Asian characters or Hungarians.

Universal Names works by replacing `Character.GetFullName` calls in GUI and localization with a call to a customizable localization it defines. CMF defines clones of these custom locs in a manner that allows UN to overwrite them if UN is enabled; otherwise, CMF's definitions provide a fallback to the equivalent datafunctions. This allows seamless compatibility with compliant text - any applicable characters will either have their names displayed identically to vanilla, or their names will be fixed if the user has UN installed without any additional actions required on the user's part.

In the interest of promoting this improved user experience, it is recommended to use the Universal Names custom locs for printing full names in any journals, events, GUIs, etc. whenever they are used. Below is a list of all the vanilla name datafunctions and their Universal Names custom locs counterparts which CMF provides seamless compatibility for:
```
Character.GetFullName                      => Character.GetCustom('GetUniversalFullName')
Character.GetFullNameNoFormatting          => Character.GetCustom('GetUniversalFullNameNoFormatting')
Character.GetFullNameWithTitle             => Character.GetCustom('GetUniversalFullNameWithTitle')
Character.GetFullNameWithTitleNoFormatting => Character.GetCustom('GetUniversalFullNameWithTitleNoFormatting')
Character.GetPrimaryRoleTitle              => Character.GetCustom('GetUniversalTitle')
```
Simple localization usage example:
```
original_text: "Hello, my name is [Character.GetFullNameNoFormatting]"
improved_text: "Hello, my name is [Character.GetCustom('GetUniversalFullNameNoFormatting')]"
```
Consider a Korean character whose name in the real world would be written as `Yi Sun-sin`. Korean names are `Last-First` names, so `Sun-sin` is the given name and `Yi` is the surname.
- With `original_text`, it would render as `Hello, my name is Sun-sin Yi`. In reality this would be *incorrect*.
- With `improved_text`, it would render as `Hello, my name is Yi Sun-sin`. This is correct and improves character flavor!

# Power Bloc Disbander

CMF provides a scripted effect to disband a power bloc arbitrarily. To disband a power bloc, use the `com_disband_power_bloc` scripted effect:
```
com_disband_power_bloc = {
    power_bloc = scope_to_some_power_bloc
}
```
This scripted effect expects a `power_bloc` argument, and the argument must point to the scope of the power bloc to be disbanded.

For example, to dissolve the British Empire power bloc, you can write any one of the following examples:
```
# Example 1
com_disband_power_bloc = {
    power_bloc = c:GBR.power_bloc
}

# Example 2
c:GBR = {
    com_disband_power_bloc = {
        power_bloc = power_bloc
    }
}

# Example 3
c:GBR.power_bloc = {
    save_scope_as = bloc_i_want_to_get_rid_of
}
com_disband_power_bloc = {
    power_bloc = scope:bloc_i_want_to_get_rid_of
}
```
