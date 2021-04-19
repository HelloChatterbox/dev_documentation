---
description: >-
  An intent is the task the user intends to accomplish when they say something.
  The role of the intent parser is to extract from the user's speech key data
  elements that specify their intent.
---

# Intents

A user can accomplish the same task by expressing their intent in multiple ways. The role of the intent parser is to extract from the user's speech key data elements that specify their intent in more detail. This data can then be passed to other services, such as Skills to help the user accomplish their intended task.

_Example_: Julie wants to know about today's weather in her current location, which is Melbourne, Australia.

> "hey chatterbox, what's today's weather like?"
>
> "hey chatterbox, what's the weather like in Melbourne?"
>
> "hey chatterbox, weather"

Even though these are three different expressions, for most of us they probably have roughly the same meaning. In each case we would assume the user expects Chatterbox to respond with today's weather for their current location. The role of an intent parser is to determine what this intent is.

In the example above, we might extract data elements like:

* **weather** - we know that Julie wants to know about the weather, but she has not been specific about the type of weather, such as _wind_, _precipitation_, _snowfall_ or the risk of _fire danger_ from bushfires. Melbourne, Australia rarely experiences snowfall, but falls under bushfire risk every summer.
* **location** - Julie has stipulated her location as Melbourne, but she does not state that she means Melbourne, Australia. How do we distinguish this from Melbourne, Florida, United States?
* **date** - Julie has been specific about the _timeframe_ she wants weather data for - today. But how do we know what today means in Julie's timezone. Melbourne, Australia is between 14-18 hours ahead of the United States. We don't want to give Julie yesterday's weather, particularly as Melbourne is renowned for having changeable weather.

