# Community-Mod-Framework
Framework mod to support compatibility between including GUI, Political Movements, Parties and mod detection triggers

## Political Movements ##

Overwrites vanilla Political Movement definitions with scripted triggers to aid in mod compatibility

Add dummy ideologies from mods into political movements, allowing them to spawn with the appropiate mod enabled:
* Add a dummy ideology with the same name as your mod ideology
* Assign the ideology to the appropiate political movements (and scripted triggers if needed)
* Load this mod below any other mod
* Your mod will overwrite the ideology definition and allow it to spawn in the specified political movements

## GUI Framework ##

Current Scope:
1) A "sidebar" scripted widget to deconflict mods that want to add custom sidebar buttons. (Credit to Bahmut, LordR and Alexedishi)
2) Modification to the GUI template fullscreen_hide to hide the outliner whenever a scripted widget window is open. (Already done by myself)
3) Modification to objective_types to add a scrollbar to the objectives screens. (Credit to Bahmut, KarafuruAmamiya and Xier)
4) Integration of the "Modded DLC Framework" (Credit to 1230James)
5) Unified system for cooltip types (Credit to 1230James)
6) Modification to the outliner and journal GUIs to hide custom objectives during gameplay (Credit to Taylor)
7) Several "superevent" windows for extra flavor (Credit to Bananaman & Klein for the Newspaper window)
8) Modification to journal.gui to allow players to show a character icon in a journal entry (Credit to Mori)

Usage Notes:
* The Objective header can be hidden by setting the global variable community_gui_objective_var
* "Superevent" windows activated by including in event: gui_window = (event_window_crisis/event_window_newspaper/event_window_fullscreen)

## Sidebar ##

How to add a new button to the sidebar.

First create an ideology in the `common/ideologies/` folder (See [example_button.txt](common/ideologies/example_button.txt)).
The icon set on the ideology is the icon shown on your button.
**Important here is that this ideology is never triggered or shown!**

Then we need a scripted gui in the `common/scripted_guis/` folder corresponding to the button (See [example_button_sgui.txt](common/scripted_guis/example_button_sgui.txt))

We then link those two via the localization of the ideology.
Localizations can be found in `localization/<language>/`.
Ideologies have two localization keys: \<ideology\> and \<ideology\>_desc

The key \<ideology\> should contain the name of your scripted_gui.
And the key \<ideology\>_desc contains the tooltip shown when hovering over the button (See [com_gui_l_english.yml](localization/english/com_gui_l_english.yml)).
**Good practice here is to name the ideology and the scripted gui the same so even if you do not set the localization key for a language, the correct scripted gui is triggered!**

And at last we need to add the button to the sidebar.
This is done via the following effect (but with your ideology):
```
add_to_global_variable_list = {
    name = custom_button_list
    target = ideology:gui_sidebar_example_button
}
```
This effect can be run wherever you want, like a journal entry or an event.
One possibility is to run it in `common/history/global/` (See [enable_example_button.txt](common/history/global/enable_example_button.txt)).

### GUI Window Visibility ###

When a sidebar button is clicked the following GUI variable is set to your scripted gui name: `com_open_window`
In your custom window you should check for it like this (with your scripted gui name):
```
visible = "[GetVariableSystem.HasValue('com_open_window', 'gui_sidebar_example_button')]"
```
If you want to close your window again you can do it by clearing the variable like this:
```
onclick = "[GetVariableSystem.Clear('com_open_window')]"
```

### Fullscreen GUI ###

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

## Parties ##
For naming, you need to include loc keys to avoid load-up error. These can be blank and overwritten by your own mod. 

## Community Mod Triggers ##

Usage
1) Place the file 00_community_mod_compatibility_triggers.txt  in the /common/scripted_triggers folder of your mod. This file will contain the scripted triggers all set to return false by default. This is intentional.
YOURMODNAME_is_active_trigger = {
  always = no
}

2) Create another file with the name zz_YOURMODNAME_compatibility_triggers.txt that contains the following:
YOURMODNAME_is_active_trigger = {
  always = yes
}

Currently Included:
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
* Magic Gate
* Morgenrote: Dawn of Flavor
* Newspapers Mod
* Rally Round the King
* States That Make Sense
* Western Clothes: Redux

## Keybinds ##

You can take a free keybind by doing this:
1) Check default.profile and see which keybind is still free. You can find free keybinds at the bottom of the file.
2) Add input_action = "input_$your_input$" to the button you want to use it for.
3) Add a localization for your button to "localization/language_x/replace" and use the name of the input_action.

Note: It is possible to add additional keybinds if there are no keybinds left.