---
description: >-
  Logging is useful during Skill development, as well as to help end-users
  diagnose problems in the future.
---

# Logging

To track events and data within your Skill we can use logging. If you are new to programming, this is a way to output a message that can tell you the state of your Skill at a particular point in time, details about an error that has occured, or simply noting that a program reached a particular point in the code.

## Basic Usage

A logger is available through the `ChatterboxSkill` base class. This means that you can use it within a Skill without needing to import the `logging` package. You can simply call `self.log` from within the class of your Skill.

Here is a quick example of an `info` level message used in a Skill. We will learn more about different levels shortly.

```python
from adapt.intent import IntentBuilder
from chatterbox import ChatterboxSkill, intent_handler

class LoggingSkill(ChatterboxSkill):

    @intent_handler(IntentBuilder('HelloWorldIntent')
                    .require('HelloWorld'))
    def handle_hello_world_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        self.log.info("This is an info level log message.")
        self.speak_dialog("hello.world")

def create_skill():
    return LoggingSkill()
```

## Logging Levels

There are five types of log messages available that are used for different purposes.

### Debug

```python
self.log.debug
```

Debug messages are used for information that will help to diagnose problems. These are particularly useful if there is anything that has the potential to break in the future.

By default these messages will not be logged unless the User has explicitly turned on debug level logging.

### Info

```python
self.log.info
```

Info messages provide general information when the Skill is running as expected. These messages will always be logged so are useful when actively developing a Skill, but should be used sparingly once a Skill is published for other people to use.

### Warning

```python
self.log.warning
```

Warning messages are used to indicate that something has gone wrong, but the Skill will continue to function.

### Error

```python
self.log.error
```

Error messages indicate that a serious problem has occured and the Skill will not be able to function. In the Chatterbox CLI these messages are shown in red to make them highly visible.

### Exception

```python
self.log.exception
```

Exception messages are an extended form of the `error` level message. These messages include a stack trace and should only be called from an exception handler. For example:

```python
try:
    1/0
except ZeroDivisionError as e:
    self.log.exception("Cannot divide by zero")
```

## Where do these messages get logged?

Log messages from a Skill are written to the `skills.log` file located at: `/var/log/chatterbox/skills.log`

## Using the logger outside the Skill class

As the logger is provided by the ChatterboxSkill class, it is only available within that scope. If you need to log messages from outside of this class, you can import the logger manually.

```python
from chatterbox.util import LOG
```

This can then be used outside your Skill's class. Extending our first example:

```python
from adapt.intent import IntentBuilder
from chatterbox import ChatterboxSkill, intent_handler
from chatterbox.util import LOG

LOG.info("This is a logged info level message outside of the ChatterboxSkill class scope")

def my_special_function():
  LOG.info("Another usage of LOG.")

class LoggingSkill(ChatterboxSkill):

    @intent_handler(IntentBuilder('HelloWorldIntent')
                    .require('HelloWorld'))
    def handle_hello_world_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        self.log.info("This is an info level log message.")
        self.speak_dialog("hello.world")
        my_special_function()

def create_skill():
    return LoggingSkill()
```

