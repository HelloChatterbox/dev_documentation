---
description: The audio service handles playback and queueing of tracks.
---

# Audio Service

The `chatterbox-core` distribution of Chatterbox includes a _Playback Skill_ which can be used to control playback after it has been started. This means that playback only needs to be started in the **Skill**. Controlling playback can then be done through the _Playback Skill_.

## How to set up the Audio Service

First, import the

`AudioService`

class.

```python
from chatterbox.skills.audioservice import AudioService
```

Then in the `initialize()` method of your **Skill**, instantiate an `AudioService` object:

```python
    def initialize(self):
        self.audio_service = AudioService(self.bus)

        #Other initialize code
        [...]
```

## Starting playback

Once the `AudioService` instance is created, you can start playback by simply calling the `play()` method with a track URI:

```python
        self.audio_service.play('file:///path/to/my/track.mp3')
```

or with a list of tracks

```python
        self.audio_service.play(['file:///path/to/my/track.mp3', 'http://tracks-online.com/my/track.mp3'])
```

see the [AudioServicePlugins](https://chatterbox-ai.gitbook.io/docs/chatterbox-technologies/chatterbox-core/plugins/audioservice#audiobackend) for information about configuring supported uris.

The play method has an optional second argument to further process the user's **Utterance**. 
Currently this can only be used to select backend \(where you want to send the audio\) but in the future it will be able to handle requests like

> Hey Chatterbox, play Hello Nasty by the Beastie Boys at half volume. We don't want to wake the neighbours

To use this feature the **Utterance** received from the intent service must be passed

```python
    def play_playlist_handler(self, message):
        self.audioservice.play(PLAYLIST, message.data['utterance'])
```

## More technical information

## The backends

* `VLC` a very general purpose media playe (Default)
* `simple` uses only common command line utilities (aplay, paplay, mpg123, ogg123...)

## AudioService Technical Documentation

More information on AudioService methods can be found in the [Chatterbox Technical Documentation](https://chatterbox-core.readthedocs.io/en/master/source/chatterbox.html#audioservice-class).

