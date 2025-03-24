# Community-Mod-Framework
Framework mod to support compatibility between including GUI, Political Movements, Parties and mod detection triggers

## Steam Page
https://steamcommunity.com/sharedfiles/filedetails/?id=3385002128

## Contents
* [Setting Dependency](#setting-dependency)
* [Political Movements](#political-movements)
* [Debug Mode](#debug-mode)
* [GUI Framework](#gui-framework)
    * [Alternative Event Windows](#alternative-event-windows)
    * [Hiding Objective Header](#hiding-objective-header)
    * [Custom Social Hierarchies](#custom-social-hierarchies)
    * [Sidebar Button](#sidebar-button)
    * [Characters in Journal Entry](#characters-in-journal-entry)
    * [Custom Owner Buildings](#custom-owner-buildings)
    * [Multi-line Production Methods](#multi-line-production-methods)
* [Structs](#structs)
    * [Creating a new Struct](#creating-a-new-struct)
    * [Setting Variables on a Struct](#setting-variables-on-a-struct)
* [Parties](#parties)
* [Community Mod Triggers](#community-mod-triggers)
* [Keybinds](#keybinds)
* [Additional Modifier Icons](#additional-modifier-icons)
* [Heir Blocker](#heir-blocker)
* [Weekly Event Framework](#weekly-event-framework)

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

# Political Movements

Overwrites vanilla Political Movement definitions with scripted triggers to aid in mod compatibility

Add dummy ideologies from mods into political movements, allowing them to spawn with the appropiate mod enabled:
* Add a dummy ideology with the same name as your mod ideology
* Assign the ideology to the appropiate political movements (and scripted triggers if needed)
* Load this mod below any other mod
* Your mod will overwrite the ideology definition and allow it to spawn in the specified political movements

# Debug Mode

The keybinding `CTRL + ALT + D` toggles the global variable `com_debug`.

This can be used to enable or disable debug content like debug Decisions or Events.

# GUI Framework

Current Scope:
1) A "sidebar" scripted widget to deconflict mods that want to add custom sidebar buttons. (Credit to Bahmut, LordR, & Alexedishi)
2) Modification to the GUI template fullscreen_hide to hide the outliner whenever a scripted widget window is open. (Credit to Bahmut & Alexedishi)
3) Modification to objective_types to add a scrollbar to the objectives screens. (Credit to Bahmut, KarafuruAmamiya, & Xier)
4) Modification to society_panel to add the ability to use custom social hierarchies. (Credit to Bahmut)
5) Integration of the "Modded DLC Framework" (Credit to 1230James)
6) Unified system for cooltip types (Credit to 1230James)
7) Modification to the outliner and journal GUIs to hide custom objectives during gameplay (Credit to Taylor)
8) Several "superevent" windows for extra flavor (Credit to Bananaman & Klein for the Newspaper window, Credit to Alexedishi for all others)
9) Modification to Journal Entry GUI to allow players to show characters (Credit to Bahmut and Mori)
10) Integration of the "Multi-line PM Framework" (Credit to 1230James)
11) Alerts can now open custom windows (Credit to Bahmut)
12) More than three local goods can now be shown in state building panel correctly (Credit to Bahmut)

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

Ethics Style Window:
- [event_window_ethics](docs/event_windows/event_window_ethics.png)

### Usage Notes
- For ease of use, any modded windows with characters will expect a character scope for the arguments `left_icon = scope:some_character`, `right_icon = scope:some_character` and `center_icon = scope:some_character` if the event has three characters. Just like the vanilla events do.
- `event_window_duel` also has an optional progress bar that will display below the flavor text
  - This is activated by setting the variable com_event_window_2char_duel_var
  - The progress bar will pull the value from this variable; it has a maximum of 100 and a minimum of 0
- `event_window_crisis` uses six character scopes saved as variables; documentation is provided in the `eventwindow.gui` file

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

To enable a custom social hierachy you have to execute this effect in a countries scope:
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
**Good practice here is to name the ideology and the scripted gui the same so even if you do not set the localization key for a language, the correct scripted gui is triggered!**

And at last we need to add the button to the sidebar.
This is done via the following effect (but with your ideology):
```
add_to_global_variable_list = {
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

## Characters in Journal Entry

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

### Opinions

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
```
**NOTE: Note that military buildings, such as barracks and naval bases, are NOT INTENDED TO BE USED WITH MPM due to the new unit graphics being displayed alongside the PMGs which now take up most of the space that the extra PMGs would overflow into.**

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

**NOTE: Internally structs are immortal Characters in the void. This means potential textures for the GUI could be set using a Characters ideology.**

# Parties

For naming, you need to include loc keys to avoid load-up error. These can be blank and overwritten by your own mod. 

# Community Mod Triggers

## Usage
1) Place the file `00_community_mod_compatibility_triggers.txt` in the `/common/scripted_triggers` folder of your mod. This file will contain the scripted triggers all set to return false by default. This is intentional.
```
YOURMODNAME_is_active_trigger = {
   always = no
}
```
2) Create another file with the name `zz_YOURMODNAME_compatibility_triggers.txt` that contains the following:
```
YOURMODNAME_is_active_trigger = {
   always = yes
}
```

## Currently Included:
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

# Weekly Event Framework

This is a framework to allow for a weekly firing script event on any day of the week, without a hidden journal entry being used.

To use:
1. In `com_weekly_on_action.txt`, rename `set_weekly_on_action_example` to a name of your choice and add this to the `on_monthly_pulse` on_actions block.
2. In the same file, rename the `com_run_weekly_event_example` to a relevant name
3. In `com_weekly_event.txt`, rename `com_run_weekly_event_example` to the same as what you named it above. Set weekday to your required day, rename the global variable `com_added_days` and replace `example_on_action_weekly` with your weekly on action.
4. Go back to `com_weekly_on_action.txt` and add your weekly on action as a new on action.
5. Rename `com_weekly_on_action.txt` and `com_weekly_event.txt` to something that won't conflict with other mods using this framework.


# Hide/Show Journal Entry Groups

This allows for hiding and showing any Journal Entry Group.

Usage:
`com_hide_journal_entry_group = { name = je_group_historical_content }` 
This would hide all National Agenda (`je_group_historical_content`) Journal Entries.

`com_show_journal_entry_group = { name = je_group_historical_content }` 
This would show them again.