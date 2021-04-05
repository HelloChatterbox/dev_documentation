---
description: >-
  A Message Bus is mechanism for independent systems to communicate with each
  other using a set of Messages for common commands or notifiers. In the Chatterbox
  ecosystem, the Messagebus is a websocket.
---

# MessageBus

## What is a Message Bus?

A Message Bus is mechanism for independent systems to communicate with each other using a set of _messages_ for common commands or notifiers.
In the Chatterbox ecosystem, the Messagebus is a websocket and the messages contain a message type with an optional JSON data packet. 
Some messages trigger actions and have side effects; some are simple notifiers of actions that either have occurred or are about to occur. 
The Messagebus connects the `chatterbox-core` processes and the **Skills**, and can also be joined by outside systems such as the CLI.

See all the Message types that are currently used by the MessageBus.

{% page-ref page="message-types.md" %}

Messages can be sent from the _producers_ and acted upon by [Skills](https://chatterbox.ai/documentation/skills) or other _consumers_ within `chatterbox-core`. The producers and consumers listed are examples and some messages might be generated or handled by other processes or advanced **Skills**.

The base [ChatterboxSkill API](http://chatterbox-core.readthedocs.io/en/stable/) handles most of the Messagebus usage automatically. 
For example, the `chatterbox.stop` message is caught by the skill framework, invoking an overridden `ChatterboxSkills.stop()` method within a **Skill**. 
Similarly, the `ChatterboxSkill.speak()` and `ChatterboxSkill.speak_dialog()` methods generate `speak` messages to be conveyed to the text-to-speech \(TTS\) and audio systems.

You will really only need to know about the Chatterbox Messagebus if you are developing advanced **Skills**. 
The `ChatterboxSkill.add_event()` method allows you to attach a handler which will be triggered when the message is seen on the Messagebus.

## ChatterboxSkill Interaction

### Connecting Message handlers

```python
from chatterbox import ChatterboxSkill

class ListenForMessageSkill(ChatterboxSkill):
  def initialize(self):  
      self.add_event('recognizer_loop:record_begin',  
                    self.handle_listener_started)  
      self.add_event('recognizer_loop:record_end',  
                    self.handle_listener_ended)

  def handle_listener_started(self, message):  
      # code to execute when active listening begins...

  def handle_listener_ended(self, message):  
      # code to execute when active listening ends...  

def create_skill():
    return ListenForMessageSkill()
```

### Generating Messages

```python
from chatterbox import ChatterboxSkill
from chatterbox.messagebus import Message

class GenerateMessageSkill(ChatterboxSkill):
  def some_method(self):  
    self.bus.emit(Message("recognizer_loop:utterance",  
                          {'utterances': ["the injected utterance"],  
                            'lang': 'en-us'}))  

def create_skill():
    return GenerateMessageSkill()
```

## Guidelines for Message Usage

Private messages can be placed on the Messagebus following these naming conventions:  
`subsystem.message` or `skill.skillname.message`

* Messages MUST use verbs for requests - such as;  
  * `mic.mute`  
  * `mic.unmute`  
  * `skill.chatterboxtimer.cancel.all`
* Messages MUST use the future tense for pre-action notifications - such as;  
  * `mic.muting`  
  * `mic.unmuting`
* Messages MUST use the past tense for post-action notifications - such as;  
  * `mic.muted`  
  * `mic.unmuted`  
  * `skill.chatterboxtimer.expired`

See all the Message types that are currently used by the MessageBus.

{% page-ref page="message-types.md" %}

## Additional Support

If you have further questions, then the best place to ask them is our [Community Forum](https://community.chatterbox.ai) or in the [~dev Channel](https://chat.chatterbox.ai/community/channels/dev) on Chatterbox Chat.

