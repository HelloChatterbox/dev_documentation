---
description: Exploring the foundational components of a basic Chatterbox Skill.
---

# Skill Structure

## Folder structure

Each skill repo needs to follow this structure:

* repo\_name
  * `__init__.py`
  * locale
    * en-us
      * say\_this.dialog
      * hear\_this.intent
  * readme.md        \(optional\)
  * manifest.yaml   \(optional\)
  * skill\_meta.json  \(optional\)

The `locale` directory contains subdirectories for each spoken language the skill supports. The subdirectories are named using the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) for the language. For example, Portuguese is 'pt-pt', German is 'de-de', and Australian English is 'en-au'.

By default, your new Skill should contain one subdirectory for United States English - 'en-us'. If more languages were supported, then there would be additional language directories.

#### Dialog files

There will be one `.dialog` file in the language subdirectory \(ie. `en-us`\) for each type of dialog the Skill will use. 

When instructed to use a particular dialog, Chatterbox will choose one of these lines at random. This is closer to natural speech. That is, many similar phrases mean the same thing.

For example, how do you say 'goodbye' to someone?

* Bye for now
* See you round
* Catch you later
* Goodbye
* See ya!

#### Intent files

Each Skill defines one or more Intents. Adapt Intents are defined using  `.voc` files. Padatious Intents are defined using `.intent` files

We will learn about Intents in more detail shortly. For now, we can see that within the `locale` directory you may find multiple types of files:

* `.intent` files used for defining Padatious Intents
* `.voc` files define keywords primarily used in Adapt Intent

### \_\_init\_\_.py

The `__init__.py` file is where most of the Skill is defined using Python code. We will learn more about the contents of this file in the next section.

Let's take a look:

#### Importing libraries

```python
from adapt.intent import IntentBuilder
from chatterbox import ChatterboxSkill, intent_handler
```

This section of code imports the required _libraries_. Some libraries will be required on every Skill, and your skill may need to import additional libraries.

#### Class definition

The `class` definition extends the `ChatterboxSkill` class:

```python
class HelloWorldSkill(ChatterboxSkill):
```

The class should be named logically, for example "TimeSkill", "WeatherSkill", "NewsSkill", "IPaddressSkill". If you would like guidance on what to call your Skill, please join the [~skills Channel on Chatterbox Chat](https://chat.chatterbox.ai/community/channels/skills).

Inside the class, methods are then defined.

#### \_\_init\_\_\(\)

This method is the _constructor_. It is called when the Skill is first constructed. It is often used to declare state variables or perform setup actions, however it cannot utilise ChatterboxSkill methods as the class does not yet exist. You don't have to include the constructor.

An example `__init__` method might be:

```python
def __init__(self):
    super().__init__()
    self.already_said_hello = False
    self.be_friendly = True
```

#### initialize\(\)

Perform any final setup needed for the skill here. This function is invoked after the skill is fully constructed and registered with the system. Intents will be registered and Skill settings will be available.

```python
def initialize(self):
    my_setting = self.settings.get('my_setting')
```

#### Intent handlers

Previously the `initialize` function was used to register intents, however our new `@intent_handler` decorator is a cleaner way to achieve this. We will learn all about the different [Intents](https://github.com/ChatterboxAI/documentation/tree/6d83da34d06c9587d90bf7d68a42ab842c4835fe/docs/skill-development/intents.md) shortly. You may also see the `@intent_file_handler` decorator used in Skills. This has been deprecated and you can now replace any instance of this with the simpler `@intent_handler` decorator.

In our current HelloWorldSkill we can see two different styles.

1. An Adapt handler, triggered by a keyword defined in a `ThankYouKeyword.voc` file.

   ```python
   @intent_handler(IntentBuilder('ThankYouIntent').require('ThankYouKeyword'))
   def handle_thank_you_intent(self, message):
       self.speak_dialog("welcome")
   ```

2. A Padatious intent handler, triggered using a list of sample phrases.

   ```python
   @intent_handler('HowAreYou.intent')
   def handle_how_are_you_intent(self, message):
    self.speak_dialog("how.are.you")
   ```

In both cases, the function receives two _parameters_:

* `self` - a reference to the HelloWorldSkill object itself
* `message` - an incoming message from the `messagebus`.

Both intents call the `self.speak_dialog()` method, passing the name of a dialog file to it. In this case `welcome.dialog` and `how.are.you.dialog`.

#### stop\(\)

You will usually also have a `stop()` method.

This tells Chatterbox what your Skill should do if a stop intent is detected.

```python
def stop(self):
    pass
```

In the above code block, the [`pass` statement](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement) is used as a placeholder; it doesn't actually have any function. However, if the Skill had any active functionality, the stop\(\) method would terminate the functionality, leaving the Skill in a known good state.

#### create\_skill\(\)

The final code block in our Skill is the `create_skill` function that returns our new Skill:

```python
def create_skill():
    return HelloWorldSkill()
```

This is required by Chatterbox and is responsible for actually creating an instance of your Skill that Chatterbox can load.

_Please note that this function is not scoped within your Skills class. It should not be indented to the same level as the methods discussed above._

### LICENSE

This file contains the full text of the license your Skill is being distributed under.

### README.md

The README file contains human readable information about your Skill.

## What have we learned

You have now successfully created a new Skill and have an understanding of the basic components that make up a Chatterbox Skill.

