# Documentation
## Effects
* [create_com_situation_journal_entry](#effect-create_com_situation_journal_entry)
* [create_ongoing_com_situation_journal_entry](#effect-create_ongoing_com_situation_journal_entry)

### Effect: `create_com_situation_journal_entry`
Add journal entry to the scoped country
and add a newly created situation to that journal.

**Parameters:**
- `journal` journal entry key
- `situation_id` id of the new situation
- `icon` icon ideology key for the situation
- `side_leader_country_left` country scope for the left side leader of the situation
- `side_name_left` name localization key for the left side leader of the situation
- `side_desc_left` description/tooltip localization key for the left side leader of the situation
- `side_leader_country_right` country scope for the right side leader of the situation
- `side_name_right` name localization key for the right side leader of the situation
- `side_desc_right` description/tooltip localization key for the right side leader of the situation

### Effect: `create_ongoing_com_situation_journal_entry`
Add journal entry to the scoped country
and add an already ongoing situation to that journal entry.

**Parameters:**
- `journal` journal entry key
- `situation_id` id of the ongoing situation