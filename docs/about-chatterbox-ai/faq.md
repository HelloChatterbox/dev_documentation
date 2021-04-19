---
description: Questions that we frequently receive about Chatterbox and our technologies.
---

# FAQ

## Can Chatterbox run completely offline? Can I self-host everything?

As a privacy focused project and community, many people are interested in fully offline or self-hosted options. Chatterbox has intentionally been built in a modular fashion, so this is possible however is not easy and is unlikely to provide an equivalent user experience.

To achieve this we need to look at three key technologies: backend services provided by [hellochatterbox.net](https://hellochatterbox.net); speech recognition or speech-to-text \(STT\); and speech-synthesis or text-to-speech \(TTS\).

You can choose to run your own STT service such as [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech/releases) or [Kaldi](https://kaldi-asr.org/), however in our opinion these do not yet provide sufficient accuracy for mainstream usage.

If you are running your own services, your Chatterbox installation can be directed to use those using the [chatterbox.conf file](../using-chatterbox-ai/customizations/chatterbox-conf.md).

The chatterbox backend is needed to provide APIs used by some [~~extension~~s]() and to [build skills](), these components can not be self hosted

## How fast can Chatterbox respond?

By default, to answer a request Chatterbox:

1. Detects the button press
2. Records 3 - 10 seconds of audio 
3. Sends this audio to a cloud-based speech-to-text \(STT\) service 
4. Transcribes the audio and returns the text transcription 
5. Parses the text to understand the intent 
6. Sends the text to the intent handler with the highest confidence 
7. Allows the Skill to perform some action and provide the text to be spoken 
8. Synthesizes audio from the given text, either locally or remotely, depending on the text-to-speech \(TTS\) engine in use 
9. Plays the synthesized spoken audio.

Through this process there are a number of factors that can affect the perceived speed of Chatterbox's responses:

* System resources - more processing power and memory never hurts!
* Network latency - as it is not yet possible to perform everything on device, network latency and connection speed can play a significant role in slowing down response times.
* Streaming STT - we have been experimenting with the use of streaming services. This transcribes audio as it's received rather than waiting for the entire utterance to be finished and sending the resulting audio file to a server to be processed in its entirety. It is possible to switch to a streaming STT service however at present this is not available by default and requires a paid 3rd party service. See [Switching STT Engines](../using-chatterbox-ai/customizations/stt-engine.md) for a list of options available.
* Dialog structure - a long sentence will always take more time to synthesize than a short one. For this reason Chatterbox breaks up longer dialog into chunks and returns one to speak whilst the next is being generated. Skill developers can help provide quicker response times by considering the structure of their dialog and breaking that dialog up using punctuation in appropriate places.
* TTS Caching - synthesized audio is cached meaning common recently generated phrases don't need to be generated, they can be returned immediately.

