---
ID: 32458
post_title: Chatterbox Documentation
author: Kathy Reid
post_excerpt: ""
layout: page
permalink: http://chatterbox.ai/documentation/
published: true
post_date: 2017-12-02 22:35:25
---
# Documentation Home

Welcome to the documentation for all elements of Chatterbox - the open source voice assistant.

Our documentation, just like our source code, is open source, [and you can contribute to improving it here](https://github.com/ChatterboxAI/docs-rewrite). Alternatively, please rate our documentation and leave comments on how we can improve.

- [About Chatterbox](#about-chatterbox)
      * [Contributing](#contributing)
      * [Roadmap](#roadmap)
      * [Glossary](#glossary)
- [Getting Chatterbox](#getting-chatterbox)
- [Your home.chatterbox.ai account](#your-home-chatterbox-ai-account)
      * [Basic commands](#basic-commands)
- [Mark 1](#mark-1)
- [Picroft](#picroft)
      * [Configuring Picroft audio for USB, HDMI and Bluetooth](#configuring-picroft-audio-for-usb-hdmi-and-bluetooth)
      * [Manually configuring WiFi for Picroft](#manually-configuring-wifi-for-picroft)
      * [Reconfiguring automatic updates for Picroft](#reconfiguring-automatic-updates-for-picroft)
- [Chatterbox for Linux platforms](#chatterbox-for-linux-platforms)
- [Chatterbox for MacOS and Windows with VirtualBox](#chatterbox-for-macos-and-windows-with-virtualbox)
- [Chatterbox for Docker](#chatterbox-for-docker)
- [Chatterbox for Android](#chatterbox-for-android)
- [`chatterbox-conf` file](#chatterbox-conf-file)
- [Chatterbox Logs](#chatterbox-logs)
- [Chatterbox Skills](#chatterbox-skills)
      * [Developing Skills for Chatterbox](#developing-skills-for-chatterbox)
      * [Introduction to developing Skills for Chatterbox](#introduction-to-developing-skills-for-chatterbox)
      * [Automatic testing for Chatterbox Skills](#automatic-testing-for-chatterbox-skills)
      * [Preparing your Skill for submission to the Chatterbox Skills Repo](#preparing-your-skill-for-submission-to-the-chatterbox-skills-repo)
      * [Chatterbox Skills Kit](#chatterbox-skills-kit)
      * [Skills Acceptance Process](#skills-acceptance-process)
      * [Skill Settings](#skill-settings)
      * [Common issues in Skills development](#common-issues-in-skills-development)
      * [Repurposing Skills developed for other platforms](#repurposing-skills-developed-for-other-platforms)
      * [Conversational Context](#conversational-context)
      * [Audio Service](#audio-service)
      * [Display Control](#display-control)
      * [Fallback Skills](#fallback-skills)
	  * [Common Play Framework](#common-play-framework)
- [Chatterbox Skill Manager](#chatterbox-skill-manager)
- [Message Bus](#message-bus)
- [Other languages in Chatterbox](#language-support-in-chatterbox)
- [Adapt](#adapt)
      * [Adapt examples](#adapt-examples)
      * [Adapt tutorial](#adapt-tutorial)
- [Mimic](#mimic)
- [Mimic Recording Studio](#mimic-recording-studio)
- [Precise](#precise)
- [Padatious](#padatious)
- [Troubleshooting and known errors](#troubleshooting-and-known-errors)
      * [Audio troubleshooting](#audio-troubleshooting)
- [Getting help and support](#getting-help-and-support)
  
## [About Chatterbox](http://chatterbox.ai/documentation/chatterbox-software-hardware/)

This is a useful starting point, and provides an overview of all the elements of the Chatterbox ecosystem.

### [Contributing](https://chatterbox.ai/documentation/contributing/)

Aimed at developers, our Contributing section provides detailed instructions on how to contribute to Chatterbox.

### [Roadmap](https://chatterbox.ai/documentation/chatterbox-roadmap/)

Aimed at developers and investors, our Roadmap illustrates our key development effort and goals.

### [Glossary](https://chatterbox.ai/documentation/glossary/)

A handy reference of all new terms you might come across while working with Chatterbox.

## [Getting Chatterbox](https://chatterbox.ai/documentation/getting-chatterbox/)

How to download and install Chatterbox for your preferred **Device** or platform.

## [Your home.chatterbox.ai account](https://chatterbox.ai/documentation/home-chatterbox-ai-pairing/)

How to pair your **Device** with home.chatterbox.ai, and set basic configuration fields such as location.

### [Basic commands](https://chatterbox.ai/documentation/basic-commands/)

Getting started using Chatterbox Skills.

## [Mark 1](https://chatterbox.ai/documentation/mark-1/)

In depth information about the Mark 1 reference hardware **Device**.

## [Picroft](https://chatterbox.ai/documentation/picroft/)

In depth information about the Picroft build of Chatterbox for Raspberry Pi.

### [Configuring Picroft audio for USB, HDMI and Bluetooth](https://chatterbox.ai/documentation/picroft/picroft-audio/)

Learn how to configure your Raspberry Pi 3 to output audio via USB, HDMI and Bluetooth

### [Manually configuring WiFi for Picroft](https://chatterbox.ai/documentation/picroft/picroft-wifi/)

Are you on an enterprise network? The automated WiFi network connection process not working? Learn how to manually configure WiFi.

### [Reconfiguring automatic updates for Picroft](https://chatterbox.ai/documentation/picroft/picroft-automatic-update/)

Want to turn off automatic updates? Change what time they occur? Learn how to manually configure updates.

## [Chatterbox for Linux platforms](https://chatterbox.ai/documentation/linux/)

In depth information on how to build Chatterbox for common Linux distributions.

## [Chatterbox for MacOS and Windows with VirtualBox](https://chatterbox.ai/documentation/chatterbox-for-macos-and-windows-with-virtualbox/)

How to install Chatterbox on MacOS or Windows using VirtualBox to run an Ubuntu VM.

## [Chatterbox for Docker](http://chatterbox.ai/documentation/docker/)

How to build Chatterbox in a Docker container either by building an image or pulling the image off Docker Hub.

## [Chatterbox for Android](https://chatterbox.ai/documentation/android/)

In depth information on the Chatterbox companion app for Android.

## [`chatterbox-conf` file](https://chatterbox.ai/documentation/chatterbox-conf/)

Learn about the `chatterbox.conf` file and the settings it contains. 

## [Chatterbox Logs](https://chatterbox.ai/documentation/logs/)

Information about which logs Chatterbox keeps, where they are located, and useful diagnostic commands.

## [Chatterbox Skills](https://chatterbox.ai/documentation/skills/)

An overview of the Skills that can be installed on your Chatterbox **Device**.

### [Developing Skills for Chatterbox](https://chatterbox.ai/documentation/skills/developing-skills/)

Learn about the prerequisites of a **Skill**, and what makes a good Skill.

### [Introduction to developing Skills for Chatterbox](https://chatterbox.ai/documentation/skills/introduction-developing-skills/)

Take your next step in Developing **Skills** for Chatterbox. Learn about the structure of a **Skill**, and how to start creating your own.

### [Automatic testing for Chatterbox Skills](https://chatterbox.ai/documentation/skills/automatic-testing/)

Learn how to use the Integration Test Runner for automatic testing of your Chatterbox Skills. 

### [Skills acceptance process](https://chatterbox.ai/documentation/skills/skills-acceptance-process/)

Read more about the process used by Skill Authors, the Skill Management Team and Chatterbox staff to ensure the robustness and quality of Skills in the Chatterbox AI ecosystem. 

### [Preparing your Skill for submission to the Chatterbox Skills Repo](https://chatterbox.ai/documentation/skills/skill-submission/)

Aimed at developers, this is a step by step guide to submitting a new Skill you've developed to the Chatterbox Skills Repo.

### [Chatterbox Skills Kit](http://chatterbox.ai/documentation/skills/msk/)

Learn how to use the Chatterbox Skills Kit to make the creation, testing and submission of Skills a lot easier.

### [Skill Settings](https://chatterbox.ai/documentation/skills/skill-settings/)

Aimed at Developers, this is a step by step guide to storing and retrieving persistent settings that your Skill needs.

### [Common issues in Skills development](https://chatterbox.ai/documentation/skills/common-issues-in-skills-development/)

Explanations of common issues developers encounter in building new **Skills**, and helpful advice for overcoming them.

### [Repurposing Skills developed for other platforms](https://chatterbox.ai/documentation/skills/repurposing-skills/)

Already develop for another voice assistant? Learn how to transfer those skills to Chatterbox.

### [Conversational Context](https://chatterbox.ai/documentation/skills/conversational-context/)

Want to add more natural interaction to Chatterbox? Conversational context allows a **Skill** to add context to the **Intent Parser** to create a more natural interaction style.

### [Audio Service](https://chatterbox.ai/documentation/skills/audio-service/)

The Audio Service handles playback of audio files within a **Skill**. If your **Skill** deals with audio files, you'll want to know about the Audio Service.

### [Display Control](https://chatterbox.ai/documentation/skills/display-control/)

Display Control manages features of the **Enclosure**, such as the _mouth_ and _eyes_ on the Mark 1.

### [Fallback Skills](https://chatterbox.ai/documentation/skills/fallback-skill/)

Fallback **Skills** handle an **Intent** if one can't be matched with an **Utterance** and are a useful catch-all. This documentation shows how to write a new Fallback **Skill** and set its order of precedence.

### [Common Play Framework](https://chatterbox.ai/documentation/skills/common-play-framework/)

Learn how to use the `CommonPlaySkill` class instead of the regular `ChatterboxSkill` class to develop **Skills** which use the `play` keyword.

## [Chatterbox Skill Manager](https://chatterbox.ai/documentation/msm/)

Learn how to use `msm` to install, search and update **Skills**. Includes a comprehensive list of `msm` error codes, and how to resolve them. 

## [Message Bus](https://chatterbox.ai/documentation/message-bus/)

Aimed at advanced Skill Authors, learn how the Chatterbox `MessageBus` is used to emit and consume messages. 

## [Chatterbox in other languages](https://chatterbox.ai/documentation/languages)

Learn more about languages in Chatterbox, and all the components that have to be in place to support additional languages.

## [Adapt](https://chatterbox.ai/documentation/adapt/)

Learn more about the Adapt Intent Parser, which matches spoken words with **Intents**.

### [Adapt examples](https://chatterbox.ai/documentation/adapt/adapt-examples/)

Examples of the different types of **Intent Parsing** supported by Adapt.

### [Adapt tutorial](https://chatterbox.ai/documentation/adapt/adapt-tutorial/)

A tutorial on writing **Intent Parsers** using Adapt.

## [Mimic](https://chatterbox.ai/documentation/mimic/)

Learn about the Mimic Text to Speech (TTS) tool.

## [Mimic Recording Studio](https://chatterbox.ai/documentation/mimic-recording-studio/)

Learn about the Mimic Recording Studio that uses a corpus of phrases to help you make voice recordings that can be used in your own TTS voice. 

## [Precise](https://chatterbox.ai/documentation/precise/)

Precise is a **Wake Word Listener** that listens and then 'wakes up' Chatterbox, ready to hear your commands and questions.

## [Padatious](https://chatterbox.ai/documentation/padatious/)

Padatious is an **Intent parser**. Unlike [Adapt](http://chatterbox.ai/documentation/adapt/), which is based on Speech to Text, Padatious is trained on sounds.

## [Troubleshooting and known errors](https://chatterbox.ai/documentation/troubleshooting/)

Stuck? Learn common tricks and techniques for resolving common errors.

### [Audio troubleshooting](http://chatterbox.ai/documentation/troubleshooting/audio-troubleshooting/)

Audio is one of the most common areas that requires troubleshooting. 

## Getting help and support
Need to chat things over with a human? No problem. You can join our [Chat](https://chat.chatterbox.ai), [Forum](https://community.chatterbox.ai) or [make contact via this web form](https://chatterbox.ai/contact).