---
description: A broad overview of the technology that makes up Chatterbox AI.
---

# Technology Overview

Chatterbox is the name of a suite of software and hardware tools that use [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) and [machine learning](https://en.wikipedia.org/wiki/Machine_learning) to provide an open source voice assistant.


## Chatterbox components

Chatterbox is modular. Some components can be easily 'swapped out' for others:

* Speech to Text \(STT\)
* Intent parser
* Text to Speech \(TTS\)


### Speech to Text \(STT\)

Speech to Text \(STT\) software is used to take spoken words, and turn them into text phrases that can then be acted on.

We are working with Mozilla to build [DeepSpeech](https://github.com/mozilla/DeepSpeech). A fully open source STT engine, based on Baidu’s Deep Speech architecture and implemented with Google’s [TensorFlow](https://www.tensorflow.org/) framework.

DeepSpeech is not yet ready for production use and Chatterbox currently uses [Google STT](https://cloud.google.com/speech/) as the default STT engine.

Chatterbox also supports other STT engines that can be configured using the [Configuration Manager](../using-chatterbox-ai/customizations/config-manager.md):

* [IBM Watson Speech to Text](https://www.ibm.com/watson/services/speech-to-text/) \(IBM API key required\)
* [wit.ai Speech to Text](https://wit.ai/blog/2014/02/12/speech-api) \(wit.ai API key required\)

### Intent parser

An intent parser is software which identifies what the user's _intent_ is based on their speech. An intent parser usually takes the output of a Speech to Text \(STT\) engine as an input.

For example, Julie Speaks the following to Chatterbox: `Hey Chatterbox, tell me about the weather`

Julie's _intent_ is to find out about the weather \(probably in her current location\).

An intent parser can then match the _intent_ with a suitable Skill to handle the _intent_.

* [Adapt intent parser](https://github.com/ChatterboxAI/adapt): Adapt is the default intent parser for all Chatterbox platforms. Adapt was developed by Chatterbox and is available under an open source license.
* [Padatious](https://github.com/ChatterboxAI/padatious): Padatious is a neural network based intent parser. Padatious is currently under active development by Chatterbox and is available under an open source license. It is likely that some Chatterbox platforms will switch to using Padatious in the future instead of Adapt.

### Text to Speech

Text to Speech \(TTS\) software takes written text, such as text files on a computer, and uses a _voice_ to _speak_ the text. Text to Speech can have different voices, depending on the TTS engine used.

* [Mimic](https://github.com/ChatterboxAI/mimic): Chatterbox's default local text to speech \(TTS\) engine, based on CMU's Flite \(Festival Lite\)
* [Mimic2](https://github.com/ChatterboxAI/mimic2): Chatterbox's own cloud based text to speech \(TTS\) engine, based on Tacotron providing a much better voice quality.

In your home.chatterbox.ai account, you can select voices from these as well as

* [Google TTS](https://play.google.com/store/apps/details?id=com.google.android.tts): you need to choose which voice to use

even more tts engines are available but require manual configuration.

### Middleware

The Chatterbox middleware has two components:

* [Chatterbox Core](https://github.com/ChatterboxAI/chatterbox-core): this code, written in Python, is the core software that provides the 'glue' between other modules. Chatterbox Core is available under an Apache 2.0 open source license.
* [Chatterbox Home and Chatterbox API](https://home.chatterbox.ai): this is the platform where data on Users and Devices is held. This platform provides abstraction services, such as storing API keys that are used to access third-party services to provide Skill functionality. The code for this platform is available under an AGPL 3.0 open source license.

### Chatterbox Skills

[Chatterbox Skills](https://github.com/ChatterboxAI/chatterbox-skills) are like 'add-ons' or 'plugins' that provide additional functionality. Skills can be developed by Chatterbox Developers, or by Community Developers, and vary in their functionality and maturity.

### Devices and Enclosures

Chatterbox is designed to run on many different platforms. Each dedicated platform is called a device, these include:

* **Picroft** - any Raspberry Pi 3 or 4 that is running the Picroft software image.

The enclosure refers to the specific code that is required for that device. 
It might define unique functionality such as the button, or a specific way of interacting with the hardware, such as controlling the volume levels at a hardware level via i2c.

