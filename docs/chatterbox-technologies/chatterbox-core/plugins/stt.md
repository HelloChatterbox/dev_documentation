---
Description: STT plugins handle converting Speech to Text.
---

# STT Plugins

All Chatterbox STT Plugins need to provide a class derived from the STT base class in `chatterbox.stt`.

When the `__init__()` method of the base class is run the config for that module will be loaded and available through `self.config`. Chatterbox's selected language will also be available through `self.lang`.

For example, the following [Chatterbox configuration](https://github.com/HelloChatterbox/dev_documentation/tree/fa8dd19ece396fdac40a643e544472fe7433b789/docs/using-chatterbox-ai/customizations/config-manager.md):

```javascript
  "stt": {
    "module": "example_stt",
    "example_stt": {
      "server": "https://my_server.com",
      "samplerate": 16000
    }
  }
```

will load the `"example_stt"` structure from the `"stt"` section and provide that in `self.config`.

## execute\(\)

Each STT plugin class needs to define the `execute()` method taking two arguments:

* `audio` \([AudioData](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#audiodataframe_data-bytes-sample_rate-int-sample_width-int---audiodata) object\) - the audio data to be transcribed.  
* `lang` \(str\) - _optional_ - the BCP-47 language code \(currently not used in core\).

The bare minimum STT class will look something like

```python
class MySTT(STT):
    def execute(audio, language=None):
        # Handle audio data and return transcribed text
        [...]
        return text
```

## STT base class

The STT system has a couple of base classes specified.

### `STT`

The base STT, this handles the audio in "batch mode" taking a complete audio file, and returning the complete transcription.

### `StreamingSTT`

A more advanced STT class for streaming data to the STT. This will receive chunks of audio data as they become available and they are streamed to an STT engine.

The plugin author needs to implement the `create_streaming_thread()` method creating a thread for handling data sent through `self.queue`. The thread this method creates should be based on the [StreamThread class](https://github.com/ChatterboxAI/chatterbox-core/blob/dev/chatterbox/stt/__init__.py#L325). `handle_audio_data()` method also needs to be implemented.

## Entry point

To make the class detectable as an STT plugin, the package needs to provide an entry point under the `chatterbox.plugin.stt` namespace.

```python
setup([...],
      entry_points = {'chatterbox.plugin.stt': 'example_stt = my_stt:mySTT'}
      )
```

Where `example_stt` is is the STT module name for the plugin, my\_stt is the Python module and mySTT is the class in the module to return.

