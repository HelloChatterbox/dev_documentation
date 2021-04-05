---
description: >-
  IntentBox is an intent parser - meaning that it is a library for converting
  natural language into machine-readable data structures, such as JSON.
---

# intentBox

- [Usage](#usage)
  * [Adapt](#adapt-4)
  * [Padatious](#padatious-2)
  
# Usage

## Adapt

```python
from intentBox.adapt_extract import AdaptExtractor

from pprint import pprint

intents = AdaptExtractor()
# intents = AdaptExtractor(use_deepseg=True)

weather = ["weather"]
hello = ["hey", "hello", "hi", "greetings"]
name = ["name is"]
joke = ["joke"]
play = ["play"]
say = ["say", "tell"]
music = ["music", "jazz", "metal", "rock", "songs"]
door = ["door", "doors"]
light = ["light", "lights"]
on = ["activate", "on", "engage", "open"]
off = ["deactivate", "off", "disengage", "close"]


intents.register_entity("weather", weather) # name, samples
intents.register_entity("hello", hello)
intents.register_entity("name", name)
intents.register_entity("joke", joke)
intents.register_entity("door", door)
intents.register_entity("lights", light)
intents.register_entity("on", on)
intents.register_entity("off", off)
intents.register_entity("play", play)
intents.register_entity("music", music)
intents.register_entity("say", say)


intents.register_intent("weather", ["weather"], ["say"]) # name, required_kwords, optional_kwords
intents.register_intent("hello", ["hello"])
intents.register_intent("name", ["name"])
intents.register_intent("joke", ["joke"], ["say"])
intents.register_intent("lights_on", ["lights", "on"])
intents.register_intent("lights_off", ["lights", "off"])
intents.register_intent("door_open", ["door", "on"])
intents.register_intent("door_close", ["door", "off"])
intents.register_intent("play_music", ["play", "music"])

sentences = [
    "tell me a joke and say hello",
    "turn off the lights, open the door",
    "nice work! get me a beer",
    "Call mom tell her hello",
    "tell me a joke and the weather",
    "turn on the lights close the door",
    "close the door turn off the lights",
    "tell me a joke and order some pizza and turn on the lights and close the door and play some songs",
    "close the pod bay doors play some music"  # fail
]

print("# _______________________________")
print("# CALCULATE SINGLE INTENT")
print("# _______________________________")
for sent in sentences:
    print("UTTERANCE:", sent)
    pprint(intents.calc_intent(sent))
    print("_______________________________")

print("# _______________________________")
print("# CALCULATE MAIN AND SECONDARY INTENTS")
print("# _______________________________")
for sent in sentences:
    print("UTTERANCE:", sent)
    pprint(intents.intent_remainder(sent))
    print("_______________________________")

print("# _______________________________")
print("# SEGMENT AND CALCULATE BEST INTENTS")
print("# _______________________________")
for sent in sentences:
    print("UTTERANCE:", sent)
    pprint(intents.calc_intents(sent))
    print("_______________________________")

print("# _______________________________")
print("# SEGMENT AND CALCULATE MAIN AND SECONDARY INTENTS")
print("# _______________________________")
for sent in sentences:
    print("UTTERANCE:", sent)
    pprint(intents.intents_remainder(sent))
    print("_______________________________")

```
## Padatious


```python
from intentBox.padatious_extract import PadatiousExtractor

from pprint import pprint

intents = PadatiousExtractor()
# intents = PadatiousExtractor(use_deepseg=True) 


weather = ["weather"]
hello = ["hey", "hello", "hi", "greetings"]
name = ["my name is {name}"]
joke = ["tell me a joke", "i want a joke", "say a joke", "tell joke"]
lights_on = ["turn on the lights", "lights on", "turn lights on", "turn the lights on"]
lights_off = ["turn off the lights", "lights off", "turn lights off", "turn the lights off"]
door_on = ["open the door", "open door", "open the doors"]
door_off = ["close the door", "close door", "close the doors"]
music = ["play music", "play some songs", "play heavy metal", "play some jazz", "play rock"]

intents.register_intent("weather", weather)  # name, samples
intents.register_intent("hello", hello)
intents.register_intent("name", name)
intents.register_intent("joke", joke)
intents.register_intent("lights_on", lights_on)
intents.register_intent("lights_off", lights_off)
intents.register_intent("door_open", door_on)
intents.register_intent("door_close", door_off)
intents.register_intent("play_music", music)

sentences = [
    "tell me a joke and say hello",
    "turn off the lights, open the door",
    "nice work! get me a beer",
    "Call mom tell her hello",
    "tell me a joke and the weather",
    "turn on the lights close the door",
    "close the door turn off the lights",
    "tell me a joke and order some pizza and turn on the lights and close the door and play some songs",
    "close the pod bay doors play some music"  # fail
]

print("# _______________________________")
print("# CALCULATE SINGLE INTENT")
print("# _______________________________")
for sent in sentences:
    print("UTTERANCE:", sent)
    pprint(intents.calc_intent(sent))
    print("_______________________________")

print("# _______________________________")
print("# SEGMENT AND CALCULATE BEST INTENTS")
print("# _______________________________")
for sent in sentences:
    print("UTTERANCE:", sent)
    pprint(intents.calc_intents(sent))
    print("_______________________________")

```