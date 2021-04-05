---
description: >-
  An intent is how the User starts an interaction with Chatterbox. It represents
  the job they are trying to accomplish.
---

# Intents

Let's start with an example. A user in Melbourne, Australia might want to know about the weather. 
To ask for this information, they might say:

> "Hey Chatterbox, what's today's weather like?" 
>
> "Hey Chatterbox, what's the weather like in Melbourne?" 
>
> "Hey Chatterbox, weather"

Even though these are three different expressions, for most of us they probably have roughly the same meaning.
In each case we would assume the user expects Chatterbox to respond with today's weather for their current location. 

It is up us as Skill creators to teach Chatterbox the variety of ways that a user might express the same intent. 
This is a key part of the design process. It is the key difference between a Skill that kind of works if you know what to say, and a Skill that feels intuitive and natural to talk to.

This is handled by an intent parser whose job it is to learn from your Skill what intents it can handle, and extract from the user's speech and key information that might be useful for your Skill. 
In this case it might include the specified date and location.

For technical details on using Intents in your Chatterbox Skill, see:

{% page-ref page="intents.md" %}



