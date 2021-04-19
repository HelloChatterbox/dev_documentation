---
description: Different strategies can be used for intent matching
---

# Multi Intent Support

### Single Intent

CONS:

* restricted to 1 utterance, 1 intent
* mixes up conflicting orders into a single one

#### Adapt

MAX: 1 intent

```text
UTTERANCE: turn off the lights and turn on the tv
{'conf': 0.5,
 'intent_type': 'lights_on',
 'entities': {'lights': 'lights', 'on': 'on'}}
_______________________________

UTTERANCE: tell me a joke and the weather
{'conf': 0.6666666666666666,
 'intent_type': 'weather',
 'entities': {'say': 'tell', 'weather': 'weather'}}
```

#### Padatious

MAX: 1 intent

```text
UTTERANCE: tell me a joke order some pizza
{'conf': 0.5230809565835034, 'entities': {}, 'name': 'joke'}    
```

### Main and Secondary intents

calculate an intent, remove entities from utterance, calculate intent in utterance remainer

PROS:

* 1 utterance, 2 intents
* does not depend on segmentation

CONS:

* loses context of keywords consumed in first intent
* it's not very smart joining keywords
* limited number of intents

#### Adapt

adapt is keyword based so this works great, there always is an utterance remainder unless every word was consumed

MAX: 2 intents

```text
UTTERANCE: turn off the lights turn on the tv
{'main_intent': {'conf': 0.5,
                 'intent_type': 'lights_on',
                 'entities': {'lights': 'lights', 'on': 'on'}},
 'remainder_intent': {'conf': 1.0,
                      'intent_type': 'tv_off',
                      'entities': {'tv': 'tv', 'off': 'off'}},
 'utterance': 'turn off the lights turn on the tv',
 'utterance_remainder': 'turn off the   the tv'}
______________________________
UTTERANCE: turn on the lights close the door
{'main_intent': {'conf': 0.5,
                 'intent_type': 'lights_on',
                 'entities': {'lights': 'lights', 'on': 'on'}},
 'remainder_intent': {'conf': 1.0,
                      'intent_type': 'door_close',
                      'entities': {'door': 'door', 'off': 'close'}},
 'utterance': 'turn on the lights close the door',
 'utterance_remainder': 'turn  the  close the door'}
```

padatious is examples based, there is no utterance remainder to use in this method

### Segmentation + Intent

works great in general

PROS:

* uses segmentation to split utterances logically
* 1 utterance, unlimited intents

CONS:

* context is lost in segmentation

#### Adapt

MAX: number of utterance chunks after segmentation

```text
UTTERANCE: turn off the lights and open the door
{' open the door': {'conf': 1.0,
                    'intent_type': 'door_open',
                    'entities': {'door': 'door', 'on': 'open'}},
 'turn off the lights': {'conf': 1.0,
                         'intent_type': 'lights_off',
                         'entities': {'lights': 'lights', 'off': 'off'}}}
```

#### Padatious

MAX: number of utterance chunks after segmentation

```text
UTTERANCE: tell me a joke and order some pizza and turn on the lights and close the door and play some songs
{'close the door': {'conf': 1.0, 'entities': {}, 'name': 'door_close'},
 'order some pizza': None,
 'play some songs': {'conf': 1.0, 'entities': {}, 'name': 'play_music'},
 'tell me a joke': {'conf': 1.0, 'entities': {}, 'name': 'joke'},
 'turn on the lights': {'conf': 1.0, 'entities': {}, 'name': 'lights_on'}}
_______________________________
```

### Segmentation + Main and Secondary Intents

same as above, works great in adapt but not usually in padatious

PROS:

* compensates for failures in segmentation

#### Adapt

MAX: 2\* number of utterance chunks after segmentation

```text
UTTERANCE: close the pod bay doors play some music
{'close the pod bay doors play some music': {'main_intent': {'conf': 0.5,
                                                             'intent_type': 'door_close',
                                                             'entities': {'door': 'doors',
                                                                         'off': 'close'}},
                                             'remainder_intent': {'conf': 1.0,
                                                                  'intent_type': 'play_music',
                                                                  'entities': {'music': 'music',
                                                                              'play': 'play'}},
                                             'utterance': 'close the pod bay '
                                                          'doors play some '
                                                          'music',
                                             'utterance_remainder': ' the pod '
                                                                    'bay  play '
                                                                    'some '
                                                                    'music'}} 
```

