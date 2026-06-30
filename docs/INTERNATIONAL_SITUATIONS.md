# Overview
Situations are meant to model clashes between factions on an international scale. They can have multiple journal entries associated with it and provide a tool to model complex power struggles.

These are implemented as contextless journals in the `je_group_global_international_situations` journal group. CMF's **International Situation Framework** seeks to aid this by providing a custom journal entry widget and some supporting effects. This takes advantage of the ability to inject widgets into journal entries as of V3 patch 1.13.
# Content
* [Elements](#elements)
  * [Outliner Changes](#outliner-changes)
  * [Hiding Journal Entry Elements](#hiding-journal-entry-elements)
  * [Journal Entry Widget](#journal-entry-widget)
  * [Usage](#usage)
* [Script docs](#script-docs)
    * [Effects](#effects)
    * [Details](#details)
    * 
# Elements
This framework consists of the following features:
- Modification to the outliner to add support for pinning IO and Situation journals
- Addition of variable checks to hide various elements from journal entries
- Custom injectable journal widget that combines the design of V3 journals, CK3 struggles, and EU5 situations
- 
## Outliner Changes
This framework takes advantage of the partitioning of the outliner journal pins provided by the *International Organizations Framework*.

### Situation Journals
This section displays any pinned journal entry groups that are included in the `com_international_situation_journal_groups` global list. The group `je_group_global_international_situations` is automatically added to this list.

## Hiding Journal Entry Elements
This framework takes advantage of the *International Organizations Framework*'s variable checks to hide/modify certain elements of the journal entry panel by setting variables on the journal entry scope.
- `com_header_var` to replace the journal sub-header with a flag variable
- `com_hide_timeout` to hide the timeout timer and effects
- `com_hide_status_desc` to hide the status desc
- `com_hide_scripted_buttons` to hide the scripted buttons
- `com_hide_journal_reason`  to hide the journal _reason
- `com_hide_involved_countries` to hide the involved countries
- `com_hide_complete_triggers` to the hide the journal completion triggers/effects
- `com_hide_fail_triggers` to the hide the journal failure triggers/effects
- `com_hide_modifiers` to the hide the journal modifiers

## Journal Entry Widget
This framework is centered on a custom journal widget that combines features from the CK3 Struggle GUI and EU5 Situations GUI with the V3 journal entry. This is injected like any other journal entry widget. The effect `com_hide_all_journal_elements_for_situation_effect` is provided to hide all journal entry elements to avoid collisions with the widget. The following features are included:

- Small header textbox at the top of the widget that accepts a flag variable
- Rectangular illustration widget that accepts a custom background texture (inspired by EU5 situations)
- Situation phase UI element that allows for displaying phase information (inspired by CK3 struggles)
- Collapsible container that shows involved countries with an option secondary container for "Interloper" countries (derived from the IO framework)
- Scripted button container from the IO framework
- Collapsible container that displays the potential outcomes of the journal entry (inspired by CK3 struggles)
- Toggleable containers that display progress towards phases and their factors (inspired by CK3 struggles)

## Usage
To use these widgets, you must inject them using one of the journal anchor points available since V3 patch 1.13. It is recommended to inject these widget into the `custom_widget_container_je_icon` anchor point. This anchor point removes the default journal icon. We also provide a scripted effect to hide all other journal elements.

### Widget Setup Steps:
First, you will need to inject the widget by placing this into your journal entry script:
```
	widget = {
		gui = "gui/com_journal_injects/situation_widgets.gui"
		name = "widget_com_international_situation"
		container = "custom_widget_container_je_icon"
	}
```
Second, you will need to run this in the `immediate` of your contextless journal:
```
immediate = {
    scope:journal_entry = {
        com_hide_all_journal_elements_for_situation_effect = yes
	}
}
```

### Individual Widget Elements
All elements of `widget_com_international_situation` are completely optional. The core journal entry mechanics are unchanged by this framework so the underlying journal logic such as `complete`/`fail` trigger and any pulses will work as expected. The activation of the widget's elements are driven by a system of variables set on the journal scope.

#### Situation Header
This is a small header that appears at the very top of the widget. This is activated by setting `com_situation_header_var` on the journal. This variable expects a flag and will display the localization entry at the top of the widget.

#### Situation Illustration
This is a rectangular element inspired by the situations UI from EU5. This is activated by setting `com_situation_illustration_var` on the journal scope. Usage is as follows:
- `com_situation_illustration_var` expects a saved `ig_trait:` scope from which it will pull it's background. See `/common/interest_group_traits/com_situation_illustrations.txt` for some pre-made traits with working backgrounds.
- The start date of the struggle can be displayed on the upper right of the illustration box. This is activated by setting both `com_situation_start_month_var` and `com_situation_start_year_var` on the journal scope. `com_situation_start_month_var` expects a flag variable while `com_situation_start_year_var` expects an integer value. Both must be set for this element to appear. The effects `com_set_international_situation_start_date_today_effect` and `com_set_international_situation_start_date_effect` are provided to streamline this process.

#### Situation Phase Information
This element is inspired by the CK3 phase information element. This is activated by setting both `com_situation_phase_icon_var` and `com_situation_phase_name_var` on the journal scope. Usage is as follows:
- `com_situation_phase_icon_var` expects a text icon that is scaled to fit the UI element
- `com_situation_phase_name_var` expects a flag variable
- The "Phase Effects" container use the `[JournalEntry.GetTimedModifiers]` datamodel; remember that contextless journal modifiers flow down to all involved countries

#### Situation Timeout & Involvement Container
This small container displays the journal timeout timer and also provides a small textbox. This can be activated by setting `com_involvement_status_var` on the journal scope. Usage is as follows:
- The timer will only be present if `JournalEntry.CanTimeOut` returns true
- `com_involvement_status_var` expects a flag variable

#### Situation Flavor Text Container
This container implements the base game journal entry flavor text contianer. This is activated by setting `com_situation_reason_var` on the journal scope. `com_situation_reason_var` expects a flag variable.

#### Situation Involved & Interloper Countries Container
This container contains two `dynamicgridbox` elements that display participating countries. Usage is as follows:
- The first is always active and uses the `[JournalEntry.GetInvolvedCountries]` datamodel.
- The second can be activated by setting the variable list `com_situation_interloper_list` on the journal scope.

#### Situation Outcomes
*WIP*

#### Situation Phase Progress
*WIP*

# Script Docs
These are following effects and triggers available to use for managing journals with the International Organization Framework:

## Effects
* [com_hide_all_journal_elements_for_situation_effect](#effect-com_hide_all_journal_elements_for_situation_effect)
* [com_set_international_situation_start_date_today_effect](#effect-com_set_international_situation_start_date_today_effect)
* [com_set_international_situation_start_date_effect](#effect-com_set_international_situation_start_date_effect)

## Details

### Effect: `com_hide_all_journal_elements_for_situation_effect`
Sets the following [variables](#hiding-journal-entry-elements) on the journal:
- `com_hide_timeout`  to hide the journal timeout container
- `com_hide_scripted_buttons`  to hide the journal scripted buttons container
- `com_hide_journal_reason`  to hide the journal _reason
- `com_hide_involved_countries` to hide the involved countries
- `com_hide_complete_triggers` to the hide the journal completion triggers/effects
- `com_hide_fail_triggers` to the hide the journal failure triggers/effects
- `com_hide_modifiers` to the hide the journal modifiers
- `com_hide_status_desc` to the hide the status_desc

**Parameters:**
- None

### Effect: `com_set_international_situation_start_date_today_effect`
Sets the following variables on the journal:
- `com_situation_start_month_var` with the flag of the current in-game month
- `com_situation_start_year_var` with the value of the current in-game year
 
**Parameters:**
- None

### Effect: `com_set_international_situation_start_date_effect`
Allows for manually setting `com_situation_start_month_var` and `com_situation_start_year_var`

**Parameters:**
- `month` the localization key of the desired month
- `year` the integer value of the desired year