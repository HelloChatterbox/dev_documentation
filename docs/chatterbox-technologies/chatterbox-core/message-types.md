---
description: >-
  Messages are used to communicate information between Chatterbox services and
  other components. This list of Message types outlines the details and provides
  sample code for each.
---

# Message Types

Each Message type listed contains a description outlining it's meaning or purpose. Where relevant, the Message type will also list the specific JSON data packets expected to be emitted with that Message, and the most common producers and consumers of the Message.

See the [MessageBus documentation](services/message-bus.md) for further information on this service and examples of using Messages.

## General

### speak

Request to speak utterance

**Data:**

```javascript
{
    "utterance": <words to be spoken>,
    "lang": <language code, e.g. en-us>
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('speak',
                   self.handler_speak)

def handler_speak(self, message):
    # code to excecute when speak message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('speak',
                              {"utterance": <words to be spoken>,
                               "lang": <language code, e.g. en-us>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'speak' '{ "utterance": <words to be spoken>, "lang": <language code, e.g. en-us>}'
```
{% endtab %}
{% endtabs %}

### chatterbox.internet.connected

Internet connection is now available \(only generated on initial connection\)

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.internet.connected',
                   self.handler_chatterbox_internet_connected)

def handler_chatterbox_internet_connected(self, message):
    # code to excecute when chatterbox.internet.connected message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.internet.connected'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.internet.connected'
```
{% endtab %}
{% endtabs %}

### chatterbox.ready

Sent by start-up sequence when everything is ready for user interaction

| Producer | Consumer |
| :--- | :--- |
| `skills/padatious_service.py` | Pairing Skill |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.ready',
                   self.handler_chatterbox_ready)

def handler_chatterbox_ready(self, message):
    # code to excecute when chatterbox.ready message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.ready'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.ready'
```
{% endtab %}
{% endtabs %}

### chatterbox.stop

Stop command \(e.g. button pressed\)

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.stop',
                   self.handler_chatterbox_stop)

def handler_chatterbox_stop(self, message):
    # code to excecute when chatterbox.stop message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.stop'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.stop'
```
{% endtab %}
{% endtabs %}

### chatterbox.not.paired

Start the pairing process when this event is emitted.

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p>Pairing Skill</p>
        <p>Weather Skill</p>
        <p>Wolfram Alpha Skill</p>
      </th>
      <th style="text-align:left">Pairing Skill</th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.not.paired',
                   self.handler_chatterbox_not_paired)

def handler_chatterbox_not_paired(self, message):
    # code to excecute when chatterbox.not.paired message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.not.paired'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.not.paired'
```
{% endtab %}
{% endtabs %}

### chatterbox.paired

Pairing has completed

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">Pairing Skill</th>
      <th style="text-align:left">
        <p><code>skills/skill_manager.py</code>
        </p>
        <p><code>enclosure/mark1/__init__.py</code>
        </p>
        <p><code>enclosure/generic/__init__.py</code>
        </p>
        <p><code>client/speech/__main__.py</code>
        </p>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.paired',
                   self.handler_chatterbox_paired)

def handler_chatterbox_paired(self, message):
    # code to excecute when chatterbox.paired message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.paired'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.paired'
```
{% endtab %}
{% endtabs %}

### chatterbox.awoken

Has come out of sleep mode

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.awoken',
                   self.handler_chatterbox_awoken)

def handler_chatterbox_awoken(self, message):
    # code to excecute when chatterbox.awoken message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.awoken'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.awoken'
```
{% endtab %}
{% endtabs %}

### chatterbox.debug.log

log level can be: "CRITICAL" "ERROR" "WARNING" "INFO" "DEBUG" These correspond to the Python logging object.

The "bus" parameter allows turning the logging of all bus messages on/off.

**Data:**

```javascript
{
   "level" : <log level>,
   "bus": <True/False>
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.debug.log',
                   self.handler_chatterbox_debug_log)

def handler_chatterbox_debug_log(self, message):
    # code to excecute when chatterbox.debug.log message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.debug.log',
                              {
   "level" : <log level>,
   "bus": <True/False>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.debug.log' '{   "level" : <log level>,   "bus": <True/False>}'
```
{% endtab %}
{% endtabs %}

### complete\_intent\_failure

Intent processing failed

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('complete_intent_failure',
                   self.handler_complete_intent_failure)

def handler_complete_intent_failure(self, message):
    # code to excecute when complete_intent_failure message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('complete_intent_failure'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'complete_intent_failure'
```
{% endtab %}
{% endtabs %}

### configuration.updated

Notification to services that the configuration has changed and needs reloaded

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('configuration.updated',
                   self.handler_configuration_updated)

def handler_configuration_updated(self, message):
    # code to excecute when configuration.updated message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('configuration.updated'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'configuration.updated'
```
{% endtab %}
{% endtabs %}

## Recognizer

### recognizer\_loop:wakeword

Wakeword was heard

**Data:**

```javascript
{
    "utterance": <wakeword heard>,
    "session": <session ID>,
}
```

| Producer | Consumer |
| :--- | :--- |
| `client/speech/main.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:wakeword',
                   self.handler_wakeword)

def handler_wakeword(self, message):
    # code to excecute when recognizer_loop:wakeword message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('recognizer_loop:wakeword',
                              {"utterance": <wakeword heard>,
                               "session": <session ID>,}
))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'recognizer_loop:wakeword' '{ "utterance": <wakeword heard>, "session": <session ID>,}'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:record\_begin

Recording has started

| Producer | Consumer |
| :--- | :--- |
| `client/speech/main.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:record_begin',
                   self.handler_record_begin)

def handler_record_begin(self, message):
    # code to excecute when recognizer_loop:record_begin message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('recognizer_loop:record_begin'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'recognizer_loop:record_begin'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:record\_end

Recording has ended

| Producer | Consumer |
| :--- | :--- |
| `client/speech/main.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:record_end',
                   self.handler_record_end)

def handler_record_end(self, message):
    # code to excecute when recognizer_loop:record_end message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('recognizer_loop:record_end'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'recognizer_loop:record_end'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:utterance

STT has detected the given text or text was injected as an utterance via the CLI.

**Data:**

```javascript
{
    "utterances": [text],
    "lang": self.stt.lang,
    "session": session_id
}
```

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>client/speech/__main__.py</code>
        </p>
        <p><code>client/speech/listener.py</code>
        </p>
        <p><code>client/text/text_client.py</code>
        </p>
        <p><code>skills/__main__.py</code>
        </p>
      </th>
      <th style="text-align:left">
        <p><code>client/text/text_client.py</code>
        </p>
        <p><code>messagebus/client/client.py</code>
        </p>
        <p><code>skills/intent_service.py</code>
        </p>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:utterance',
                   self.handler_utterance)

def handler_utterance(self, message):
    # code to excecute when recognizer_loop:utterance message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('recognizer_loop:utterance',
                              {"utterances": [text],
                               "lang": self.stt.lang,
                               "session": session_id}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'recognizer_loop:utterance' '{ "utterances": [text], "lang": self.stt.lang, "session": session_id}'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:audio\_output\_start

Text output \(TTS\) has begun

| Producer | Consumer |
| :--- | :--- |
| `audio/speech.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:audio_output_start',
                   self.handler_audio_output_start)

def handler_audio_output_start(self, message):
    # code to excecute when recognizer_loop:audio_output_start message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('recognizer_loop:audio_output_start'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'recognizer_loop:audio_output_start'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:audio\_output\_end

Text output \(TTS\) has ended

| Producer | Consumer |
| :--- | :--- |
| `audio/speech.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:audio_output_end',
                   self.handler_audio_output_end)

def handler_audio_output_end(self, message):
    # code to excecute when recognizer_loop:audio_output_end message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('recognizer_loop:audio_output_end'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'recognizer_loop:audio_output_end'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:sleep

Go into "sleep" mode. Everything except "Hey Chatterbox, wake up" will be ignored.

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:sleep',
                   self.handler_sleep)

def handler_sleep(self, message):
    # code to excecute when recognizer_loop:sleep message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('recognizer_loop:sleep'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'recognizer_loop:sleep'
```
{% endtab %}
{% endtabs %}

### recognizer\_loop:wake\_up

Come out of "sleep" mode.

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('recognizer_loop:wake_up',
                   self.handler_wake_up)

def handler_wake_up(self, message):
    # code to excecute when recognizer_loop:wake_up message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('recognizer_loop:wake_up'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'recognizer_loop:wake_up'
```
{% endtab %}
{% endtabs %}

## Enclosure

### enclosure.notify.no\_internet

Detected a connection error during STT

| Producer | Consumer |
| :--- | :--- |
| `audio/speech.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('enclosure.notify.no_internet',
                   self.handler_enclosure_notify_no_internet)

def handler_enclosure_notify_no_internet(self, message):
    # code to excecute when enclosure.notify.no_internet message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('enclosure.notify.no_internet'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'enclosure.notify.no_internet'
```
{% endtab %}
{% endtabs %}

### enclosure.mouth.viseme\_list

start: timestamp for audio starts \(unix epoch\) END\_TIME: time in seconds from "start" until the end of the viseme CODE can be 0 = shape for sounds like 'y' or 'aa' 1 = shape for sounds like 'aw' 2 = shape for sounds like 'uh' or 'r' 3 = shape for sounds like 'th' or 'sh' 4 = neutral shape for no sound 5 = shape for sounds like 'f' or 'v' 6 = shape for sounds like 'oy' or 'ao'

**Data:**

```javascript
{
  "start": timestamp,
  "visemes": [[CODE,END_TIME],...]
}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('enclosure.mouth.viseme_list',
                   self.handler_enclosure_mouth_viseme_list)

def handler_enclosure_mouth_viseme_list(self, message):
    # code to excecute when enclosure.mouth.viseme_list message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('enclosure.mouth.viseme_list',
                              {
  "start": timestamp,
  "visemes": [[CODE,END_TIME],...]}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'enclosure.mouth.viseme_list' '{  "start": timestamp,  "visemes": [[CODE,END_TIME],...]}'
```
{% endtab %}
{% endtabs %}

### chatterbox.eyes.default

Change eyes to default color

| Producer | Consumer |
| :--- | :--- |
|  | chatterbox-mark-1 |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.eyes.default',
                   self.handler_chatterbox_eyes_default)

def handler_chatterbox_eyes_default(self, message):
    # code to excecute when chatterbox.eyes.default message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.eyes.default'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.eyes.default'
```
{% endtab %}
{% endtabs %}

## Microphone Behavior

### chatterbox.mic.listen

Begin recording for STT processing

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.mic.listen',
                   self.handler_chatterbox_mic_listen)

def handler_chatterbox_mic_listen(self, message):
    # code to excecute when chatterbox.mic.listen message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.mic.listen'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.mic.listen'
```
{% endtab %}
{% endtabs %}

### chatterbox.mic.mute

Turn off the mic \(no wakeword or STT processing\)

| Producer | Consumer |
| :--- | :--- |
| Pairing Skill | `client/speech/main.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.mic.mute',
                   self.handler_chatterbox_mic_mute)

def handler_chatterbox_mic_mute(self, message):
    # code to excecute when chatterbox.mic.mute message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.mic.mute'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.mic.mute'
```
{% endtab %}
{% endtabs %}

### chatterbox.mic.unmute

Turn on the mic \(enable wakeword and STT processing\)

| Producer | Consumer |
| :--- | :--- |
| Pairing Skill | `client/speech/main.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.mic.unmute',
                   self.handler_chatterbox_mic_unmute)

def handler_chatterbox_mic_unmute(self, message):
    # code to excecute when chatterbox.mic.unmute message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.mic.unmute'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.mic.unmute'
```
{% endtab %}
{% endtabs %}

## Audio Playback

### chatterbox.audio.service.play

Start playback of tracklist

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.play',
                   self.handler_chatterbox_audio_service_play)

def handler_chatterbox_audio_service_play(self, message):
    # code to excecute when chatterbox.audio.service.play message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.play'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.play'
```
{% endtab %}
{% endtabs %}

### chatterbox.audio.service.stop

Stop playback

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.stop',
                   self.handler_chatterbox_audio_service_stop)

def handler_chatterbox_audio_service_stop(self, message):
    # code to excecute when chatterbox.audio.service.stop message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.stop'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.stop'
```
{% endtab %}
{% endtabs %}

### chatterbox.audio.service.pause

Pause playback \(if supported\)

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.pause',
                   self.handler_chatterbox_audio_service_pause)

def handler_chatterbox_audio_service_pause(self, message):
    # code to excecute when chatterbox.audio.service.pause message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.pause'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.pause'
```
{% endtab %}
{% endtabs %}

### chatterbox.audio.service.resume

Resume playback \(if supported by backend\)

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.resume',
                   self.handler_chatterbox_audio_service_resume)

def handler_chatterbox_audio_service_resume(self, message):
    # code to excecute when chatterbox.audio.service.resume message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.resume'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.resume'
```
{% endtab %}
{% endtabs %}

### chatterbox.audio.service.next

Skip to next track

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.next',
                   self.handler_chatterbox_audio_service_next)

def handler_chatterbox_audio_service_next(self, message):
    # code to excecute when chatterbox.audio.service.next message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.next'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.next'
```
{% endtab %}
{% endtabs %}

### chatterbox.audio.service.prev

Skip to previous track

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.prev',
                   self.handler_chatterbox_audio_service_prev)

def handler_chatterbox_audio_service_prev(self, message):
    # code to excecute when chatterbox.audio.service.prev message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.prev'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.prev'
```
{% endtab %}
{% endtabs %}

### chatterbox.audio.service.track\_info

Request track info from audio service

| Producer | Consumer |
| :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">
        <p><code>skills/audioservice.py</code>
        </p>
        <p>playback-control</p>
      </th>
      <th style="text-align:left"><code>audio/main.py</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.track_info',
                   self.handler_chatterbox_audio_service_track_info)

def handler_chatterbox_audio_service_track_info(self, message):
    # code to excecute when chatterbox.audio.service.track_info message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.track_info'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.track_info'
```
{% endtab %}
{% endtabs %}

### chatterbox.audio.service.track\_info\_reply

Reply to track info request

| Producer | Consumer |
| :--- | :--- |
| `audio/main.py` | `skills/audioservice.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.track_info_reply',
                   self.handler_chatterbox_audio_service_track_info_reply)

def handler_chatterbox_audio_service_track_info_reply(self, message):
    # code to excecute when chatterbox.audio.service.track_info_reply message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.track_info_reply'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.track_info_reply'
```
{% endtab %}
{% endtabs %}

### chatterbox.audio.service.list\_backends

Returns list of available backends.

| Producer | Consumer |
| :--- | :--- |
| `skills/audioservice.py` | `audio/main.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.audio.service.list_backends',
                   self.handler_chatterbox_audio_service_list_backends)

def handler_chatterbox_audio_service_list_backends(self, message):
    # code to excecute when chatterbox.audio.service.list_backends message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.audio.service.list_backends'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.audio.service.list_backends'
```
{% endtab %}
{% endtabs %}

## Volume Control

### chatterbox.volume.increase

Enclosure Volume up

**Data:**

```javascript
{"play_sound": True}
```

| Producer | Consumer |
| :--- | :--- |
| `client/enclosure/__init__.py` | Volume Skill |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.increase',
                   self.handler_chatterbox_volume_increase)

def handler_chatterbox_volume_increase(self, message):
    # code to excecute when chatterbox.volume.increase message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.increase',
                              {"play_sound": True}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.increase' '{"play_sound": True}'
```
{% endtab %}
{% endtabs %}

### chatterbox.volume.decrease

Enclosure Volume down

**Data:**

```javascript
{"play_sound": True}
```

| Producer | Consumer |
| :--- | :--- |
| `client/enclosure/__init__.py` | Volume Skill |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.decrease',
                   self.handler_chatterbox_volume_decrease)

def handler_chatterbox_volume_decrease(self, message):
    # code to excecute when chatterbox.volume.decrease message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.decrease',
                              {"play_sound": True}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.decrease' '{"play_sound": True}'
```
{% endtab %}
{% endtabs %}

### chatterbox.volume.mute

Enclosure Volume muted

**Data:**

```javascript
{"speak_message": True}
```

| Producer | Consumer |
| :--- | :--- |
| skill-naptime | Volume Skill |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.mute',
                   self.handler_chatterbox_volume_mute)

def handler_chatterbox_volume_mute(self, message):
    # code to excecute when chatterbox.volume.mute message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.mute',
                              {"speak_message": True}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.mute' '{"speak_message": True}'
```
{% endtab %}
{% endtabs %}

### chatterbox.volume.unmute

Enclosure Volume unmuted

**Data:**

```javascript
{"speak_message": True}
```

| Producer | Consumer |
| :--- | :--- |
| skill-naptime | Volume Skill |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.unmute',
                   self.handler_chatterbox_volume_unmute)

def handler_chatterbox_volume_unmute(self, message):
    # code to excecute when chatterbox.volume.unmute message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.unmute',
                              {"speak_message": True}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.unmute' '{"speak_message": True}'
```
{% endtab %}
{% endtabs %}

### chatterbox.volume.set

Set enclosure volume \(0.0 = no output, 1.0 = loudest possible\)

**Data:**

```javascript
{"percent": float}
```

| Producer | Consumer |
| :--- | :--- |
|  | Volume Skill |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.set',
                   self.handler_chatterbox_volume_set)

def handler_chatterbox_volume_set(self, message):
    # code to excecute when chatterbox.volume.set message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.set',
                              {"percent": float}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.set' '{"percent": float}'
```
{% endtab %}
{% endtabs %}

### chatterbox.volume.get

Request volume level

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.get',
                   self.handler_chatterbox_volume_get)

def handler_chatterbox_volume_get(self, message):
    # code to excecute when chatterbox.volume.get message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.get'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.get'
```
{% endtab %}
{% endtabs %}

### chatterbox.volume.get.response

**Data:**

```javascript
{
    "percent": <volume percentage>,
    "muted": <true/false>
}
```

| Producer | Consumer |
| :--- | :--- |
|  | Enclosure \(skill-mark-2\) |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.get.response',
                   self.handler_chatterbox_volume_get_response)

def handler_chatterbox_volume_get_response(self, message):
    # code to excecute when chatterbox.volume.get.response message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.get.response',
                              {"percent": <volume percentage>,
                               "muted": <true/false>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.get.response' '{ "percent": <volume percentage>, "muted": <true/false>}'
```
{% endtab %}
{% endtabs %}

### chatterbox.volume.duck

Reduce the volume level temporarily

| Producer | Consumer |
| :--- | :--- |
|  | Enclosure \(skill-mark-2\) |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.duck',
                   self.handler_chatterbox_volume_duck)

def handler_chatterbox_volume_duck(self, message):
    # code to excecute when chatterbox.volume.duck message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.duck'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.duck'
```
{% endtab %}
{% endtabs %}

### chatterbox.volume.unduck

Restore the volume level

| Producer | Consumer |
| :--- | :--- |
|  | Enclosure \(skill-mark-2\) |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.volume.unduck',
                   self.handler_chatterbox_volume_unduck)

def handler_chatterbox_volume_unduck(self, message):
    # code to excecute when chatterbox.volume.unduck message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.volume.unduck'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.volume.unduck'
```
{% endtab %}
{% endtabs %}

## Chatterbox Skill Core

### chatterbox.skill.handler.start

**Data:**

```javascript
{handler: class/function name}
```

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skill.handler.start',
                   self.handler_chatterbox_skill_handler_start)

def handler_chatterbox_skill_handler_start(self, message):
    # code to excecute when chatterbox.skill.handler.start message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skill.handler.start',
                              {handler: class/function name}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skill.handler.start' '{handler: class/function name}'
```
{% endtab %}
{% endtabs %}

### chatterbox.skill.handler.complete

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skill.handler.complete',
                   self.handler_chatterbox_skill_handler_complete)

def handler_chatterbox_skill_handler_complete(self, message):
    # code to excecute when chatterbox.skill.handler.complete message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skill.handler.complete'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skill.handler.complete'
```
{% endtab %}
{% endtabs %}

### chatterbox.skill.enable\_intent

Enable disabled intent

**Data:**

```javascript
{"intent_name": "name"}
```

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox/skills/core.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skill.enable_intent',
                   self.handler_chatterbox_skill_enable_intent)

def handler_chatterbox_skill_enable_intent(self, message):
    # code to excecute when chatterbox.skill.enable_intent message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skill.enable_intent',
                              {"intent_name": "name"}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skill.enable_intent' '{"intent_name": "name"}'
```
{% endtab %}
{% endtabs %}

### chatterbox.skill.disable\_intent

Disable intent

**Data:**

```javascript
{"intent_name": "name"}
```

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox/skills/core.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skill.disable_intent',
                   self.handler_chatterbox_skill_disable_intent)

def handler_chatterbox_skill_disable_intent(self, message):
    # code to excecute when chatterbox.skill.disable_intent message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skill.disable_intent',
                              {"intent_name": "name"}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skill.disable_intent' '{"intent_name": "name"}'
```
{% endtab %}
{% endtabs %}

### chatterbox.skills.loaded

A Skill has been loaded

**Data:**

```javascript
{
    "id": <skill ID>,
    "name": <skill name>,
    "path": <skill directory>,
    "modified": <modified time>
}
```

| Producer | Consumer |
| :--- | :--- |
| `skills/main.py` | `chatterbox/skills/intent_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skills.loaded',
                   self.handler_chatterbox_skills_loaded)

def handler_chatterbox_skills_loaded(self, message):
    # code to excecute when chatterbox.skills.loaded message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skills.loaded',
                              {"id": <skill ID>,
                               "name": <skill name>,
                               "folder": <skill directory>,
                               "modified": <modified time>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skills.loaded' '{ "id": <skill ID>, "name": <skill name>, "folder": <skill directory>, "modified": <modified time>}'
```
{% endtab %}
{% endtabs %}

### chatterbox.skills.loading\_failure

A Skill has failed to load

**Data:**

```javascript
{
    "id": <skill ID>,
    "folder": <skill directory>
}
```

| Producer | Consumer |
| :--- | :--- |
| `skills/main.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skills.loading_failure',
                   self.handler_chatterbox_skills_loading_failure)

def handler_chatterbox_skills_loading_failure(self, message):
    # code to excecute when chatterbox.skills.loading_failure message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skills.loading_failure',
                              {"id": <skill ID>,
                               "folder": <skill directory>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skills.loading_failure' '{ "id": <skill ID>, "folder": <skill directory>}'
```
{% endtab %}
{% endtabs %}

### chatterbox.skills.shutdown

A Skill has shutdown

**Data:**

```javascript
{
    "id": <skill ID>,
    "folder": <skill directory>
}
```

| Producer | Consumer |
| :--- | :--- |
| `skills/main.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skills.shutdown',
                   self.handler_chatterbox_skills_shutdown)

def handler_chatterbox_skills_shutdown(self, message):
    # code to excecute when chatterbox.skills.shutdown message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skills.shutdown',
                              {"id": <skill ID>,
                               "folder": <skill directory>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skills.shutdown' '{ "id": <skill ID>, "folder": <skill directory>}'
```
{% endtab %}
{% endtabs %}

### chatterbox.skills.initialized

Upon startup, all skills have been loaded

| Producer | Consumer |
| :--- | :--- |
| `chatterbox/skills/skill_manager.py` | `chatterbox/skills/padatious_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skills.initialized',
                   self.handler_chatterbox_skills_initialized)

def handler_chatterbox_skills_initialized(self, message):
    # code to excecute when chatterbox.skills.initialized message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skills.initialized'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skills.initialized'
```
{% endtab %}
{% endtabs %}

### chatterbox.skills.list

List of loaded skills \(response to 'skillmanager.list'\)

**Data:**

```javascript
{"skills": [<list of skill IDs>] }
```

| Producer | Consumer |
| :--- | :--- |
| `skills/main.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skills.list',
                   self.handler_chatterbox_skills_list)

def handler_chatterbox_skills_list(self, message):
    # code to excecute when chatterbox.skills.list message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skills.list',
                              {"skills": [<list of skill IDs>] }))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skills.list' '{"skills": [<list of skill IDs>] }'
```
{% endtab %}
{% endtabs %}

### chatterbox.skills.settings.update

Pull new skill settings from the server

| Producer | Consumer |
| :--- | :--- |
| Configuration Skill | `chatterbox/skills/settings.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('chatterbox.skills.settings.update',
                   self.handler_chatterbox_skills_settings_update)

def handler_chatterbox_skills_settings_update(self, message):
    # code to excecute when chatterbox.skills.settings.update message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('chatterbox.skills.settings.update'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'chatterbox.skills.settings.update'
```
{% endtab %}
{% endtabs %}

## Skill Manager

### skillmanager.deactivate

Deactivate a skill. Activate by typing ":deactivate " in the CLI

**Data:**

```javascript
{'skill': <skill directory name>}
```

| Producer | Consumer |
| :--- | :--- |
| CLI \(`client/text/main.py`\) | `skills/skill_manager.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('skillmanager.deactivate',
                   self.handler_skillmanager_deactivate)

def handler_skillmanager_deactivate(self, message):
    # code to excecute when skillmanager.deactivate message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('skillmanager.deactivate',
                              {'skill': <skill directory name>}))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'skillmanager.deactivate' '{'skill': <skill directory name>}'
```
{% endtab %}
{% endtabs %}

### skillmanager.list

List installed skills. Activate by typing ":list" in the CLI

| Producer | Consumer |
| :--- | :--- |
| CLI \(`client/text/main.py`\) | `skills/skill_manager.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('skillmanager.list',
                   self.handler_skillmanager_list)

def handler_skillmanager_list(self, message):
    # code to excecute when skillmanager.list message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('skillmanager.list'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'skillmanager.list'
```
{% endtab %}
{% endtabs %}

### skillmanager.update

Request immediate update of all skills

| Producer | Consumer |
| :--- | :--- |
|  | `skills/main.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('skillmanager.update',
                   self.handler_skillmanager_update)

def handler_skillmanager_update(self, message):
    # code to excecute when skillmanager.update message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('skillmanager.update'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'skillmanager.update'
```
{% endtab %}
{% endtabs %}

## Messagebus Connection

### open

websocket connection has closed

| Producer | Consumer |
| :--- | :--- |
| `messagebus\client\ws.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('open',
                   self.handler_open)

def handler_open(self, message):
    # code to excecute when open message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('open'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'open'
```
{% endtab %}
{% endtabs %}

### close

websocket connection was lost, reconnecting

| Producer | Consumer |
| :--- | :--- |
| `messagebus\client\ws.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('close',
                   self.handler_close)

def handler_close(self, message):
    # code to excecute when close message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('close'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'close'
```
{% endtab %}
{% endtabs %}

### reconnecting

websocket connection has opened

| Producer | Consumer |
| :--- | :--- |
| `messagebus\client\ws.py` |  |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('reconnecting',
                   self.handler_reconnecting)

def handler_reconnecting(self, message):
    # code to excecute when reconnecting message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('reconnecting'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'reconnecting'
```
{% endtab %}
{% endtabs %}

## System Administrative Actions

### system.wifi.setup

Kick off a a wifi-setup session

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox-wifi-setup: chatterbox_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('system.wifi.setup',
                   self.handler_system_wifi_setup)

def handler_system_wifi_setup(self, message):
    # code to excecute when system.wifi.setup message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.wifi.setup'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'system.wifi.setup'
```
{% endtab %}
{% endtabs %}

### system.wifi.reset

Clear the saved wifi settings

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox-wifi-setup: chatterbox_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('system.wifi.reset',
                   self.handler_system_wifi_reset)

def handler_system_wifi_reset(self, message):
    # code to excecute when system.wifi.reset message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.wifi.reset'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'system.wifi.reset'
```
{% endtab %}
{% endtabs %}

### system.ntp.sync

Force the system clock to synchronize with NTP servers

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox-wifi-setup: chatterbox_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('system.ntp.sync',
                   self.handler_system_ntp_sync)

def handler_system_ntp_sync(self, message):
    # code to excecute when system.ntp.sync message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.ntp.sync'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'system.ntp.sync'
```
{% endtab %}
{% endtabs %}

### system.ssh.enable

Configure system to allow SSH connections

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox-wifi-setup: chatterbox_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('system.ssh.enable',
                   self.handler_system_ssh_enable)

def handler_system_ssh_enable(self, message):
    # code to excecute when system.ssh.enable message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.ssh.enable'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'system.ssh.enable'
```
{% endtab %}
{% endtabs %}

### system.ssh.disable

Configure system to block SSH connections

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox-wifi-setup: chatterbox_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('system.ssh.disable',
                   self.handler_system_ssh_disable)

def handler_system_ssh_disable(self, message):
    # code to excecute when system.ssh.disable message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.ssh.disable'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'system.ssh.disable'
```
{% endtab %}
{% endtabs %}

### system.reboot

Force a Linux reboot

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox-wifi-setup: chatterbox_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('system.reboot',
                   self.handler_system_reboot)

def handler_system_reboot(self, message):
    # code to excecute when system.reboot message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.reboot'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'system.reboot'
```
{% endtab %}
{% endtabs %}

### system.shutdown

Force a Linux shutdown

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox-wifi-setup: chatterbox_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('system.shutdown',
                   self.handler_system_shutdown)

def handler_system_shutdown(self, message):
    # code to excecute when system.shutdown message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.shutdown'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'system.shutdown'
```
{% endtab %}
{% endtabs %}

### system.update

Force an apt-get update on 'chatterbox-mark-1' or 'chatterbox-picroft' package \(as appropriate\)

| Producer | Consumer |
| :--- | :--- |
|  | `chatterbox-wifi-setup: chatterbox_admin_service.py` |

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('system.update',
                   self.handler_system_update)

def handler_system_update(self, message):
    # code to excecute when system.update message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('system.update'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'system.update'
```
{% endtab %}
{% endtabs %}

## Proposed namespaces for devs

### skill.namespace.\*

e.g. "skill.chatterbox.noftify.alarm\_changed" or "skill.jaguar.notify.car\_stopped"

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('skill.namespace.*',
                   self.handler_skill_namespace_*)

def handler_skill_namespace_*(self, message):
    # code to excecute when skill.namespace.* message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('skill.namespace.*'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'skill.namespace.*'
```
{% endtab %}
{% endtabs %}

### private.github\_username.\*

for private \(not intended to be used by anyone else\)

**Usage:**

{% tabs %}
{% tab title="Message handler in ChatterboxSkill" %}
```python
...
def initialize(self):
    self.add_event('private.github_username.*',
                   self.handler_private_github_username_*)

def handler_private_github_username_*(self, message):
    # code to excecute when private.github_username.* message detected...
...
```
{% endtab %}

{% tab title="Generating Message from ChatterboxSkill" %}
```python
...
def some_method(self):
    self.bus.emit(Message('private.github_username.*'))
...
```
{% endtab %}

{% tab title="Command line invocation" %}
```bash
python3 -m chatterbox.messagebus.send 'private.github_username.*'
```
{% endtab %}
{% endtabs %}

