---
description: >-
  Explore the fundamental building blocks of a Skill, and the knowledge required
  to create meaningful and engaging voice interactions.
---

# Development Setup

Chatterbox Skills are the voice applications that provide different functionality for users. To create a Skill requires at least basic technical experience, a Chatterbox installation or device, and an idea of what your Skill will do, and how people will use it.

## Technical Requirements

### Python programming language

Skills for Chatterbox are written using the [Python programming language](https://www.python.org/). A simple Skill can be a great way for new developers to try Python out in a real project, whilst experienced programmers will quickly see the powerful possibilities available in a well crafted Skill.

If you aren't familiar with the basics of Python, check out our [list of Python tutorials and resources](python-resources.md) to get you started. If you've programmed in other object-oriented languages, like Javascript or C\#, then you'll be able to pick it up, but if you're totally new to programming, you might want to look at an [introductory programming course](https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-11).

### Github account

Skills are hosted on [Github](https://github.com), so you will need to create an account there if you don't already have one. It is good to have an understanding of the [GitHub basics](https://guides.github.com/activities/hello-world/).

### Running Chatterbox

To test your Skill out, you will need to [set up a Chatterbox device](https://github.com/HelloChatterbox/dev_documentation/tree/fa8dd19ece396fdac40a643e544472fe7433b789/docs/using-chatterbox-ai/get-chatterbox/README.md).

If you aren't yet familiar with how Chatterbox works, check out the [overview of Chatterbox components](http://chatterbox.ai/documentation/chatterbox-software-hardware/) to understand the many technologies that come together to provide an intelligent voice assistant.

## What makes a good Skill?

### Fulfilling a need the user has

Good Skills meet one or more of the user's needs. Popular Skills are popular because people use them frequently - for instance, to set alarms, reminders, or to identify the time in other time zones. On the other hand, a Skill that, say, recites π to 100 digits might be pretty cool, but when was the last time you needed to know π to 100 digits? Contrast that with the last time you set a reminder on your phone.

### Having an easy to use voice interface

Just like a web page with a thoughtfully-designed interface is much more pleasant to use, a Skill with a well designed voice interface is a delight, not a chore, to use. You should anticipate the task the user is trying to accomplish, and how to make that as straightforward as possible.

If you haven't already, be sure to read our Voice User Interface Design Guidelines:

{% page-ref page="../voice-user-interface-design-guidelines/" %}

## Skill terminology

You'll notice some new terms as you start to develop Skills.

* **utterance** - An utterance is a phrase spoken by the User, after the User says the Wake Word. `what's the weather like in Toronto?` is an utterance.
* **dialog** - A dialog is a phrase that is spoken by Chatterbox. Different Skills will have different dialogs, depending on what the Skill does. For example, in a _weather_ Skill, a dialog might be `the.maximum.temperature.is.dialog`.
* **intent** - Chatterbox matches utterances that a User speaks with a Skill by determining an intent from the utterance. For example, if a User speaks `Hey Chatterbox, what's the weather like in Toronto?` then the intent will be identified as _weather_ and matched with the _Weather Skill_. When you develop new Skills, you need to define new intents.

If you encounter anything else you're not familiar with, checkout the [Chatterbox Glossary](https://github.com/HelloChatterbox/dev_documentation/tree/fa8dd19ece396fdac40a643e544472fe7433b789/docs/about-chatterbox-ai/glossary.md).

