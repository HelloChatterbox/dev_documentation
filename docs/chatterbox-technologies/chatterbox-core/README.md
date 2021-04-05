---
description: >-
  Chatterbox Core sits at the centre of all Chatterbox installations. The code itself
  includes anything that is generic to all instances of Chatterbox.
---

# Chatterbox Core

## Chatterbox Services

Chatterbox Core includes four or more distinct Services:

* [MessageBus](message-bus.md)
* [Skills](https://github.com/ChatterboxAI/documentation/tree/4a8ffa3702e64c9411fb0ba4239a61d1cca506ab/docs/chatterbox-technologies/chatterbox-core/skills-service.md)
* [Audio](services/audio-service.md)
* [Voice](https://github.com/ChatterboxAI/documentation/tree/4a8ffa3702e64c9411fb0ba4239a61d1cca506ab/docs/chatterbox-technologies/chatterbox-core/voice-service.md)
* [Enclosure](https://github.com/ChatterboxAI/documentation/tree/4a8ffa3702e64c9411fb0ba4239a61d1cca506ab/docs/chatterbox-technologies/chatterbox-core/enclosures.md)

Each of these is started in it's own process, and communicates with other processes by emitting and listening to messages on the MessageBus.
