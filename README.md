# Community Mod Framework
![banner.png](docs/images/banner.png)

The Community Mod Framework aims to support compatibility between different mods.
Including GUI, Political Movements, Parties, Mod detection triggers and much more.


## Content
* [Links](#links)
* [Getting Started](#getting-started)
* [Features](#features)
* [Philosophy](#philosophy)
* [Contributors](#contributors)


## Links
### Steam Page
- https://steamcommunity.com/sharedfiles/filedetails/?id=3385002128
### GitHubRepo
- https://github.com/Victoria-3-Modding-Co-op/Community-Mod-Framework


## Getting Started
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
*Also remember to add the mod to your required items on your own mods steam page.*


## Features
- [Mod Detection Triggers](Mod-Detection-Triggers): Shared triggers for detecting mods
- [Debug Features](Debug-Features): Debug mode toggle and flag viewer
- [Political Movement Weights](Political-Movement-Weights): Framework for deconflicting custom ideology movement weights
- [Political Party Names](Political-Party-Names): Framework for deconflicting custom political party names
- [UI Extensions](UI-Extensions): Framework for integrating extensions to the basegame UI
- [Custom Sidebar Buttons](Custom-Sidebar-Buttons): Framework for adding custom buttons to the sidebar
- [Additional Event Windows](Additional-Event-Windows): Custom event windows for modders
- [Additional Journal Widgets](Additional-Journal-Widgets): Injectable journal entry widgets for modders
- [Additional Modifier Icons](Additional-Modifier-Icons): Custom timed modifier icons for modders
- [Particle Effects and Shaders](Particle-Effects-and-Shaders): Custom particle effects and shaders for modders
- [International Situations and Organizations](International-Situations-and-Organizations): Frameworks providing support for CK3-style Situations and EU5-style IOs
- [Character Animations and Environment](Character-Animations-and-Environment): Frameworks for custom character animations, camera angles, and evironments.
- [Variable Error Supression](Variable-Error-Supression): Scripted effect for suppressing unset/unused variable and flag errors
- [Float Arrays](Float-Arrays): Indexed storage using scripted variables
- [Custom Mod Keybinds](Custom-Mod-Keybinds): Framework for unifying custom keybinds for mods
- [on_action Blockers](on_action-Blockers): Allows for blocking certain on_actions via variables
- [Weekly Event Framework](Weekly-Event-Framework): Allows for firing scripted events via a weekly pulse
- [Universal Names Compatibility](Universal-Names-Compatibility): sets up seamless compatibility with FUN's Universal Names mod

##  Philosophy
- This framework aims to preserve base game behavior and balance by default. If no other mods are in use, this framework should be *invisible* to the player.
- CMF is open to Pull Requests from the modding community. These are approved or rejected by consensus on the modding co-op. PRs will be rejected if they alter base game behavior. 


## Contributors
- 1230james
- Alexedishi
- Bagel
- Bahmut
- Bananaman
- BrokenRobot
- CaelReader
- CaesarVincens
- Dingbat32
- KarafuruAmamiya
- Klein
- LordR
 Marmot
- MasterofGrey
- Mori
- rskhm
- Taylor
- Xier