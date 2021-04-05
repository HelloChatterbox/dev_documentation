---
description: >-
  Chatterbox provides a range of easy to use methods to parse the contents of
  utterances from Users.
---

# Parsing Utterances

## Extracting data

### Datetime

Extracts date and time information from a sentence.

See [`extract_datetime()`](https://chatterbox-core.readthedocs.io/en/latest/source/chatterbox.util.parse.html#chatterbox.util.parse.extract_datetime)

### Duration

Convert an english phrase into a number of seconds.

See [`extract_duration()`](https://chatterbox-core.readthedocs.io/en/latest/source/chatterbox.util.parse.html#chatterbox.util.parse.extract_duration)

### Numbers

[`extract_number()`](https://chatterbox-core.readthedocs.io/en/latest/source/chatterbox.util.parse.html#chatterbox.util.parse.extract_number) takes in a string and extracts a single number.

[`extract_numbers()`](https://chatterbox-core.readthedocs.io/en/latest/source/chatterbox.util.parse.html#chatterbox.util.parse.extract_numbers) takes in a string and extracts a list of numbers.

## Matching

### Vocab Matching

[`voc_match()`](https://chatterbox-core.readthedocs.io/en/latest/source/chatterbox.html#chatterbox.ChatterboxSkill.voc_match) determines if the given utterance contains the vocabulary provided.

### Fuzzy Matching

[`fuzzy_match()`](https://chatterbox-core.readthedocs.io/en/latest/source/chatterbox.util.parse.html#chatterbox.util.parse.fuzzy_match) performs a ‘fuzzy’ comparison between two strings.

### Match One

[`match_one()`](https://chatterbox-core.readthedocs.io/en/latest/source/chatterbox.util.parse.html#chatterbox.util.parse.match_one) finds the best match from a list or dictionary given an input.

