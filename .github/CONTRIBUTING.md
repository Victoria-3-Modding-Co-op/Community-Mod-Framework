# Community Mod Framework
![banner.png](../docs/banner.png)

As the Community Mod Framework aims to support compatibility between different mods - sometimes you have to add something to it so your mods can integrate successfully.
In particular, this applies to things like Political Movements & Lobbies, where the script is very rigid.

So here's what you need to know to do this effectively.

## Contents
* [Ground Rules](#ground-rules)
* [File Categories](#file-categories)
* [File Naming](#file-naming)
* [Variable Prefixing](#variable-prefixing)
* [Community Engagement](#community-engagement)

## Ground Rules

As a *community* mod framework - we endeavour to make the bar to accessibility as low as we can make it without compromising functionality. However, please remember that we are all volunteers doing this for fun so please be respectful of our time.

## File Categories

To start with, the first thing you need to understand is that compatibility in Victoria 3 is always about receiving a trigger, providing a trigger, or selectively overwriting something.
Whether it's appropriate for CMF to overwrite some content, or whether your mod should overwrite CMF, depends on what exactly is trying to be achieved. CMF is a framework, so it's important that the way this works is consistent for all mods that interact with it.

This means that CMF content always falls into one of two categories:
- Universal Providers
- Universal Receviers

Universal Providers are content elements that you either use or overwrite in your own files, as needed. e.g. Mod Triggers (overwritten), Weekly Event Framework (utilised as a function)

Universal Receivers are content elements that overwrite your version of things, and contain elements that let them use your content in conjunction with other mods. e.g. Political Movements

## File Naming

CMF is designed to be (as much as possible) load-order agnostic - which means it doesn't matter where in a mod list it is loaded. As such, the way files are named is an important aspect of the framework's design.
File names control overwrite order (See the [Wiki](https://vic3.paradoxwikis.com/Mod_files_load_order) for more details.)

To ensure maximum robustness in compatibility design, it is important that universal receiver and universal provider content elements are not located in the same file as each other.

CMF universal providers should be named with either the `com_` prefix (for community files), or with the vanilla-style file name prefixes like `00_`.

CMF universal receivers should be named with either a `ycom_` prefix for general compatibility, or some `zz_` stytle prefix if there is no justified reason for another mod to ever overwrite it.

Ensure that you know whether your files need to overwrite, or be overwritten, by CMF, and name them appropriately.

# Variable Prefixing

If you add a variable, list, effect, trigger, etc. for use in CMF, please prefix it using `com_`. This is to prevent conflicts with both basegame and other mods.

It should be noted that, for functions which effectively add new features, we prefer generalized solutions which can be used by many different mods for consistent outcomes.

## Community Engagement

The absolute best place to connect with the project is via the Discord server: [Victoria 3 Mod Co-op](https://discord.gg/XJbqFbHdsM)
