# Overview
The **International Organizations Framework** is a feature of the Community Mod Framework that seeks to emulate the international organizations mechanic from EU5 through the use of journal entries. This takes advantage of the ability to inject widgets into journal entries as of V3 patch 1.13.

# Content
* [Elements](#elements)
* [Scripted Widget](#scripted-widget)
* [Custom Journal Groups](#custom-journal-groups)
* [Outliner Changes](#outliner-changes)
* [Hiding Journal Entry Elements](#hiding-journal-entry-elements)
* [Custom Interorg Widget](#custom-interorg-widget)
* [Usage](#usage)

# Elements
This framework consists of the following features:
- Scripted widget to display IOs which uses the CMF sidebar framework
- Custom journal groups that use the CMF hidden journal entries feature
- Modification to the outliner to add support for pinning IOs and situations
- Addition of variable checks to hide various elements from journal entries
- A custom injectable widget to provide a content baseline

## Scripted Widget
The IO panel is a scripted widget that displays any journal entry groups that have been added to the `com_international_organization_journal_groups` global list. This widget can display some basic information about the IO journal:
- The widget will always show the name of the journal and the list of involved countries
- The number of involved countries will be shown if the variable `com_interorg_involved_countries_var` is set on the journal
- The organization headquarters will be shown if the flag variable `com_interorg_headquarters_var` is set on the journal

*Note: The global list `com_international_organization_journal_groups` must be present for the sidebar button to appear!*

## Custom Journal Groups
This framework provides the following custom journal groups:
- `je_group_com_supranational_organizations`
- `je_group_com_regional_organizations`
- `je_group_com_religious_organizations`
- `je_group_com_non_governmental_organizations`
- `je_group_com_sporting_organizations`

These are automatically added to the `com_international_organization_journal_groups` global list.

## Outliner Changes
The top element of the outliner which displays pinned journal entries has been divided into three sections:
### Standard Journals
This section displays any pinned journal entry groups that are in neither of the two other sections.

### Situation Journals
This section displays any pinned journal entry groups that are included in the `com_international_situation_journal_groups` global list. The group `je_group_global_international_situations` is automatically added to this list.

### Interorg Journals
This section displays any pinned journal entry groups that are included in the `com_international_organization_journal_groups` global list. The five interorg journal groups are automatically added to this list.

## Hiding Journal Entry Elements
This framework includes the addition of several variable checks to hide/modify certain elements of the journal entry panel by setting variables on the journal entry scope.

- `com_header_var` to replace the journal sub-header with a flag variable
- `com_hide_timeout` to hide the timeout timer and effects
- `com_hide_status_desc` to hide the status desc
- `com_hide_scripted_buttons` to hide the scripted buttons
- `com_hide_journal_reason`  to hide the journal _reason
- `com_hide_involved_countries` to hide the involved countries
- `com_hide_complete_triggers` to the hide the journal completion triggers/effects
- `com_hide_fail_triggers` to the hide the journal failure triggers/effects


## Custom Interorg Widget
A series of custom interorg widgets are provided for users. These can be injected like any other journal widget. You should also hide all unwanted/redundant JE elements wth the above features. The following features are available in all widgets:
- The organization leader element will be shown if the flag variable `com_interorg_leader_country_var` is set on the journal
- The organization headquarters element will be shown if the flag variable `com_interorg_headquarters_var` is set on the journal
- Setting the variable `com_interorg_leader_character_var` will activate the character portrait to the left of the panel
- Modifiers will appear in a custom element if added to the journa
- Scripted buttons will appear in a custom button list similar to IOs from EU5

The parent widget `widget_com_international_organization_base` can also be invoked with the following features:
- The texture for the header frame can be changed by overriding the gui block `interorg_icon_frame_texture`
- The details elements to the right of the panel each have their own blocks to override visibility, text, and icons. There are a total of 5 detail entries, with the last two blank and hidden by default. All have gui blocks to override their content.

## Usage
To use these widgets, you must inject them using one of the journal anchor points available since V3 patch 1.13. It is recommended to inject these widget into the `custom_widget_container_je_icon` anchor point. This is a custom CMF anchor point that will remove the default journal icon. We also provide a scripted effect to hide all other journal elements.

### Steps:
First, you will need to inject the widget by placing this into your journal entry script:
```
widget = {
		gui = "gui/com_journal_injects/interorg_widgets.gui"
		name = "widget_com_supranational_organization"
		container = "custom_widget_container_je_icon"
}
```
Next, you will need to run this in the `immediate` of your contextless journal:
```
immediate = {
    scope:journal_entry = {
        com_hide_all_journal_elements_for_interorg_effect = yes
	}
}
```
Lastly, you will also need to activate the IO sidebar item and outliner functions. This effect can be fired from anywhere, but we recommend running it from the `immediate` of your contextless journal:
```
immediate = {
    com_activate_interorg_sidebar = yes
}
```