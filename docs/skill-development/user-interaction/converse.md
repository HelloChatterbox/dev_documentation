---
description: >-
  Converse allows a recently active Skill to inspect utterances before the
  normal intent handling process.
---

# Converse

See the [`converse()` method documentation](https://developer.hellochatterbox.net/skill-development/skill-structure/lifecycle-methods#converse).


#### Purpose of converse method:

- allow skills to intercept an utterance before the intent stage (the skill is **conversing**)
- allow skills to parse utterances without using the intent parsers
- allow skills to prepare for follow up intent parsing (manage internal state)

converse method **does not** use regular intent parsing

#### Active skill list:

- `converse` is only called for currently active skills
- core manages active skills (permission to converse)
  - an active skill is a skill that `returned True in converse` method, `triggered an intent` or `returned True in a fallback query`
  - the active skill list is ordered by activation timestamp
  - a skill is deactivated if "activate" is not called for 5 minutes (user abandoned interaction)
- skills can request to be activated
- skills can request to be deactivated (missing feature)
- skills should be able to react to being (de)activated (missing feature)
- there is an official messagebus interface to retrieve the active skill list

