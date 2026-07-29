# Community Mod Framework
![banner.png](https://raw.githubusercontent.com/Victoria-3-Modding-Co-op/Community-Mod-Framework/refs/heads/main/docs/images/banner.png)

**Community Mod Framework** primarily aims to support compatibility between different mods where collisions are unavoidable or deconfliction is impractical.
In particular, this applies to things like UI changes and Political Movement/Lobbies, where the script is very rigid and the [database entry modes](https://vic3.paradoxwikis.com/Mod_compatibility#Inject_and_replace) do not provide adequate coverage.

## Contents
* [Philosophy & Ground Rules](#philosophy--ground-rules)
* [File Categories](#file-categories)
* [File Naming](#file-naming)
* [Variable Prefixing](#variable-prefixing)
* [New Feature Modularity](#new-feature-modularity)

## Philosophy & Ground Rules
This framework aims to preserve base game behavior by default:
- If no other mods are in use, this framework should be *invisible* to the player.
- Any extensions, additions, or modifications should provide mod-makers that make use of it, new ways to show content or hook into base game functionality.
- CMF is open to Pull Requests from the modding community. These are approved or rejected by consensus on the CMF channel of the [Victoria 3 Mod Co-op](https://discord.com/channels/827163966551621662/1334219338202484746)

As a **community** mod framework - we endeavor to make the bar to accessibility as low as we can make it without compromising functionality. However, please remember that we are all volunteers doing this for fun so please be respectful of our time and do not aggressively ping contributors.

**The absolute best place to connect with the project is via the Discord server: [Victoria 3 Mod Co-op](https://discord.gg/XJbqFbHdsM)**

## File Categories

To start with, the first thing you need to understand is that compatibility in Victoria 3 is always about receiving a trigger, providing a trigger, or selectively overwriting something.
Whether it's appropriate for CMF to overwrite some content, or whether your mod should overwrite CMF, depends on what exactly is trying to be achieved. CMF is a framework, so it's important that the way this works is consistent for all mods that interact with it.

This means that CMF content always falls into one of two categories:
- Universal Providers
- Universal Receivers

Universal Providers are content elements that you either use or overwrite in your own files, as needed. e.g. Mod Triggers (overwritten), Weekly Event Framework (utilized as a function)

Universal Receivers are content elements that overwrite your version of things, and contain elements that let them use your content in conjunction with other mods. e.g. Political Movements

## File Naming

CMF is designed to be (as much as possible) load-order agnostic - which means it doesn't matter where in a mod list it is loaded. As such, the way files are named is an important aspect of the framework's design.
File names control overwrite order. See the [Victoria 3 Wiki](https://vic3.paradoxwikis.com/Mod_files_load_order) for more details.

To ensure maximum robustness in compatibility design, it is important that universal receiver and universal provider content elements are not located in the same file as each other.

CMF universal providers should be named with either the `com_` prefix (for community files),
or with the vanilla-style file name prefixes like `00_`.

CMF universal receivers should be named with either a `ycom_` prefix for general compatibility,
or some `zz_` style prefix if there is no justified reason for another mod to ever overwrite it.

Ensure that you know whether your files need to overwrite, or be overwritten, by CMF, and name them appropriately.

## Variable Prefixing

If you add a variable, list, effect, trigger, etc. for use in CMF, please prefix it using `com_`:
- This is to prevent conflicts with both base game keys and those of other mods.
- Note that some older keys may predate this convention. *This is not a license to forgo prefixing*.
- The [Mod Detection Triggers](https://github.com/Victoria-3-Modding-Co-op/Community-Mod-Framework/wiki/Mod-Detection-Triggers) specifically ignore this convention. These triggers use the conventions of their parent mods.

## New Feature Modularity
It should be noted that, for functions which effectively add new features, we vastly prefer generalized solutions which can be used by many different mods for consistent outcomes. See how the [Additional Journal Widgets](https://github.com/Victoria-3-Modding-Co-op/Community-Mod-Framework/wiki/Additional-Journal-Widgets), [International Situations Framework](https://github.com/Victoria-3-Modding-Co-op/Community-Mod-Framework/wiki/International-Situations), and [International Organizations Framework](https://github.com/Victoria-3-Modding-Co-op/Community-Mod-Framework/wiki/International-Organizations) are designed with *any* potential mod in mind rather than for a single mod-maker's use case.