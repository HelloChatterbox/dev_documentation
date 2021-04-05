---
description: >-
  Now that your Chatterbox Device is Paired with home.chatterbox.ai, you may begin
  issuing commands. Try these to get started.
---

# Basic Commands

You issue a command to Chatterbox by Speaking the **Wake Word** \(e.g. "Hey Chatterbox"\), awaiting acknowledgement from Chatterbox, and then Speaking the command itself \(aka the **utterance**\).

When you issue a command, you _intend_ for Chatterbox to react in a certain way. Your **utterance** contains an **Intent**. Chatterbox uses natural language processing to compare the words in your **utterance** to expected phrases or keywords as supplied by the installed **Skills**. When Chatterbox determines that there is a _match_ between your **utterance** and a specific expectation \(the phrases/keywords\), the **Skill** that supplied the matching expectation is notified so that it can respond to your command.

Chatterbox comes with a collection of **Skills** installed by default. Each **Skill** supplies a set of **Intents**, and each **Intent** has a set of expected phrases or keywords. Each of the default **Skills** is introduced below with a brief description, followed by a sampling of expected **utterances** \(usually grouped by **Intent**\). Additional **Skills** may be added to your Chatterbox Device; please see [Installing New Skills](https://chatterbox-ai.gitbook.io/docs/using-chatterbox-ai/installing-new-skills).

Have fun exploring natural language processing by trying these commands with variations to the wording and phrasing.

## The Default **Skills**

### Alarm

Manages a collection of alarms. Weekly repetition is supported.

**Set an alarm**

> Hey Chatterbox, wake me in two hours   
> Hey Chatterbox, wake me up at 10:23pm   
> Hey Chatterbox, set an alarm for two hours   
> Hey Chatterbox, set an alarm for 3pm   
> Hey Chatterbox, add an alarm for Monday at 8:20   
> Hey Chatterbox, create alarms for every weekday at 6   
> Hey Chatterbox, start a repeating alarm for Fridays at 9:30pm   
> Hey Chatterbox, set an alarm _&lt;- - - - - Chatterbox will ask WHEN_

**Snooze the active alarm**

> Hey Chatterbox, snooze _&lt;- - - - - Defaults to 9 minutes_   
> Hey Chatterbox, snooze for 15 minutes   
> Hey Chatterbox, give me 2 more hours

**Delete/stop/cancel/dismiss/remove**

> Hey Chatterbox, stop the alarm   
> Hey Chatterbox, delete the Tuesday alarm for 9   
> Hey Chatterbox, remove all alarms

**Query alarms**

> Hey Chatterbox, when is the next alarm?   
> Hey Chatterbox, what are the alarms for today?

**Change alarm sound**

> Hey Chatterbox, change the sound of the alarm

### Audio Record

Captures audio to a file that can be played back. The file can be deleted.

**Record**

Duration is 60-seconds unless overridden. The new duration value is used until it is overridden.

> Hey Chatterbox, record   
> Hey Chatterbox, record audio   
> Hey Chatterbox, start recording   
> Hey Chatterbox, record me for 6 seconds

**Playback**

> Hey Chatterbox, play record   
> Hey Chatterbox, play back the audio   
> Hey Chatterbox, playback recording

**Delete the file**

> Hey Chatterbox, delete audio   
> Hey Chatterbox, erase recording   
> Hey Chatterbox, record clear

### Configuration

Interacts with the Device configuration both locally and at home.chatterbox.ai.

**Query the registered name of this Chatterbox Device**

> Hey Chatterbox, what is your name?

**Query the registered location of this Chatterbox Device**

> Hey Chatterbox, where are you?   
> Hey Chatterbox, tell me your state

**Query which listener is being used to detect the Wake Word**

> Hey Chatterbox, tell me the wake word listener   
> Hey Chatterbox, what is the listener?

**Command Chatterbox to update the configuration both locally and at home.chatterbox.ai**

> Hey Chatterbox, configuration update  
> Hey Chatterbox, update config

**For developers: Select which listener to use**

> Hey Chatterbox, set the listener to precise  
> Hey Chatterbox, set the listener to default

**For developers: Enable or disable the development version of Precise listener**

> Hey Chatterbox, enable the precise dev model   
> Hey Chatterbox, disable the new precise model

### Date & Time

Chatterbox answers inquiries about Dates \(specific dates, relative dates, holidays, leap year, weekends, etc.\) and Time \(future or current, local or other location\).  Chatterbox's response to a Date inquiry attempts to supply the 'missing information' and selectively includes: day-of-week, the calendar date, and the quantity of days from now. When answering inquiries about Time, Chatterbox may optionally take advantage of the display on the enclosure.

#### Query current time \(in location\)

> Hey Chatterbox, the time now please  
> Hey Chatterbox, what time is it in Paris?

#### Query future time \(in location\)

> Hey Chatterbox, what time will it be in 2 hours?  
> Hey Chatterbox, tell me the time 6 hours from now in Paris?

#### On some enclosures: Display the time \(in location\)

> Hey Chatterbox, display the time  
> Hey Chatterbox, display the time in Paris

#### Query a holiday

> Hey Chatterbox, when is Labor Day?  
> Hey  Chatterbox, what day is Christmas in 2025?

#### Query next leap year

> Hey Chatterbox, when is the next leap year?

#### Query a specific date

> Hey Chatterbox, when in July 1st?

#### Query a relative date

> Hey Chatterbox, what is today's date?  
> Hey Chatterbox, what is today?  
> Hey Chatterbox, when is next Tuesday?  
> Hey Chatterbox, what is 6 days from now?  
> Hey Chatterbox, when in next Friday?

#### Query weekend dates

> Hey Chatterbox, what was last weekend?  
> Hey Chatterbox, what were the days last weekend?  
> Hey Chatterbox, what are the dates this weekend?  
> Hey Chatterbox, what are the days for next weekend?

### Hello World

Hello World is a well-documented **Skill** that serves as a starting point for code development. Pleasantries with Chatterbox are used as examples.

> Hey Chatterbox, greetings   
> Hey Chatterbox, hello world
>
> Hey Chatterbox, thank you
>
> Hey Chatterbox, how are you doing?   
> Hey Chatterbox, how was your day?

### IP

Query the SSID or the IP Address \(aka the network address\) of the Chatterbox Device.

**Query the IP address**

> Hey Chatterbox, what is your IP address?   
> Hey Chatterbox, tell me your network address   
> Hey Chatterbox, what network are you connected to?

**Query the SSID**

> Hey Chatterbox, what SSID are you on?   
> Hey Chatterbox, what wifi network are you using?   
> Hey Chatterbox, what network are you connected to?

### Jokes

Chatterbox uses pyjokes as the source of jokes to tell.

> Hey Chatterbox, tell me a joke   
> Hey Chatterbox, make me laugh   
> Hey Chatterbox, brighten my day with a Chuck Norris joke   
> Hey Chatterbox, tell me a non-offensive joke

### Naptime

While 'napping' Chatterbox will ignore utterances other than "Wake up".

**Begin nap**

> Hey Chatterbox, go to sleep   
> Hey Chatterbox, nap time

**End nap**

> Hey Chatterbox, wake up

### NPR News

Plays the RSS audio feed for the requested station. If no station is specified or if the request is unknown, a default station is selected based on Device location. Stations include: ABC \(Australia\), AP, BBC, CBC, DLF, Ekot, FOX, GPB, NPR, PBS, RDP, RNE, TSF, OE3, VRT, WDR, YLE.

**Play the news**

> Hey Chatterbox, what's the news?   
> Hey Chatterbox, play the BBC news   
> Hey Chatterbox, what are the headlines?

**Restart the broadcast**

> Hey Chatterbox, start over   
> Hey Chatterbox, restart news

**Stop playing the news**

> Hey Chatterbox, stop

### Personal

Ask about the "birth" and parentage of Chatterbox, and get a taste of the community fostering this open source artificial intelligence.

> Hey Chatterbox, who are you?   
> Hey Chatterbox, when were you created?   
> Hey Chatterbox, what are you?   
> Hey Chatterbox, where were you born?   
> Hey Chatterbox, who made you?   
> Hey Chatterbox, do you even rhyme?   
> Hey Chatterbox, do you dream?

### Playback Control

Common commands for controlling a music service.

**Pause the music**

> Hey Chatterbox, pause   
> Hey Chatterbox, pause the song

**Resume the paused music**

> Hey Chatterbox, resume song   
> Hey Chatterbox, resume play

**Next track**

> Hey Chatterbox, next track

**Previous track**

> Hey Chatterbox, previous track

**Play**

User provides a genre/artist/title/playlist/service. Depending on the music service, a dialog may be initiated.

> Hey Chatterbox, play my summer playlist   
> Hey Chatterbox, play Pandora   
> Hey Chatterbox, play something by hermitude   
> Hey Chatterbox, play uptown funk on youtube

### Reminder

Manages a collection of reminders. A Reminder is similar to an Alarm but instead of a beep Chatterbox speaks the User specified words.

**Set a reminder**

> Hey Chatterbox, remind me to **turn off the oven** in **5 minutes**   
> Hey Chatterbox, add a reminder to **let the dog out** at **3pm**   
> Hey Chatterbox, remind me to **take out the trash** _&lt;- - - Chatterbox will ask WHEN_  
> Hey Chatterbox, remind me at **5pm** _&lt;- - - - - - - - - Chatterbox will ask FOR WHAT_   
> Hey Chatterbox, set a reminder for me _&lt;- - - Chatterbox will ask WHEN and FOR WHAT_

**Snooze the active reminder**

> Hey Chatterbox, snooze the reminder   
> Hey Chatterbox, remind me later

**Cancel the active reminder**

> Hey Chatterbox, okay, stop the reminder

**Get reminders for a specific day**

> Hey Chatterbox, what are my reminders for today?   
> Hey Chatterbox, do I have any reminders tomorrow?

**Get next reminder**

> Hey Chatterbox, what is my next reminder?

**Delete all reminders for a specific day**

> Hey Chatterbox, cancel today's reminders   
> Hey Chatterbox, cancel all reminders for tomorrow

**Delete all reminders**

> Hey Chatterbox, delete all reminders

### Singing

Chatterbox will speak the lyrics to a random pop music song.

> Hey Chatterbox, sing   
> Hey Chatterbox, sing me a song

### Speak

Speak a phrase and have Chatterbox repeat it.

> Hey Chatterbox, speak **Mary had a little lamb**   
> Hey Chatterbox, say **yada yada yada**   
> Hey Chatterbox, repeat **hey good looking**

### Spelling

Chatterbox will spell any word that is understood by the Speech-To-Text system.

> Hey Chatterbox, spell **aardvark**   
> Hey Chatterbox, what is the spelling of **aardvark**?   
> Hey Chatterbox, how do you spell word **aardvark**?

### Stock

This Skill has been disabled.

### Stop

Tell Chatterbox to STOP doing whatever it is doing. Should work with all **Skills**.

> Hey Chatterbox, stop   
> Hey Chatterbox, silence   
> Hey Chatterbox, shut up

### Support Helper

Captures troubleshooting information from the Chatterbox Device and stores it on the [0x0.st](https://0x0.st) storage service. This information is useful for your own debugging and for communicating with Support. A link to the information is emailed to the address registered at home.chatterbox.ai.

> Hey Chatterbox, contact support   
> Hey Chatterbox, create a support ticket   
> Hey Chatterbox, troubleshoot my device   
> Hey Chatterbox, create a troubleshoot request

### Timer

Manages a collection of timers. Timers are requested with a duration expressed in hours, minutes, and/or seconds. A timer may optionally be given a name. The name is useful in queries, subsequent commands, and for display purposes. All timers beep.

* If you wish to command a specific expiration time \(e.g. 'at 3:05pm'\), please use either an Alarm or a Reminder.  
* Timers have a duration of less than 24-hours.  When a Timer is requested with a duration greater than 24-hours, an Alarm is set instead.  
* Chatterbox refers to a timer by it's original duration and the optional User supplied name. 
* When there is more than one timer with the same duration, Chatterbox may include an ordinal \(e.g. the second timer for 5-minutes\). 
* The User may refer to an individual timer by its name or by the ordinal of its position in the list of timers \(e.g. the third timer\).

**Start a timer**

> Hey Chatterbox, I need a timer named **turkey** for **15 minutes**   
> Hey Chatterbox, start a **10-minute** timer called **time to go**   
> Hey Chatterbox, set a timer to **take out the trash** _&lt;- - - Chatterbox will ask for the DURATION_   
> Hey Chatterbox, ping me in 2 hours _&lt;- - - - - - - - - No NAME is associated with this timer_   
> Hey Chatterbox, Start a timer _&lt;- - - - - - - - Chatterbox will ask for the DURATION but not a NAME_   
> Hey Chatterbox, Begin timer

**Query a timer**

> Hey Chatterbox, how's my **turkey** timer?   
> Hey Chatterbox, how much time is left?

**Cancel the beeping timer**

> Hey Chatterbox, cancel the timer

**Cancel a timer in the list of timers**

> Hey Chatterbox, cancel the first timer   
> Hey Chatterbox, delete the fourth timer   
> Hey Chatterbox, remove the **potatoes** timer   
> Hey Chatterbox, kill the **turkey** timer

**Cancel all timers**

When no timers are beeping, this command removes all timers from the list. If any timers are beeping, this command stops all of the beeping timers. 

> Hey Chatterbox, cancel all timers   
> Hey Chatterbox, delete all timers

**Mute timer**

Muting stops the beep but leaves the timer in the list so that expired timers can be displayed. 

> Hey Chatterbox, mute the timer   
> Hey Chatterbox, silence the timer

### Version Checker

Check the version of the software. If an update exists, Chatterbox will ask if the User wishes to update. To keep up-to-date, Chatterbox automatically performs these checks on a daily basis.

**Query the Chatterbox software version \(chatterbox-core\)**

> Hey Chatterbox, check version   
> Hey Chatterbox, what is code?

**Query the platform \(e.g. Picroft, Mark 1\) build version**

> Hey Chatterbox, find platform version   
> Hey Chatterbox, what is platform build?

### Volume

Manages Chatterbox's volume level.

**Query volume level**

> Hey Chatterbox, what is the volume?   
> Hey Chatterbox, how loud?

**Set volume to a numeric level \(0 to 10\)**

In a tribute to Spinal Tap, a level of '11' is accepted \(equivalent to level 10\). 

> Hey Chatterbox, increase volume to 8   
> Hey Chatterbox, set sound to NORMAL _&lt;- - - Keyword options: NORMAL=6, QUIET=3, LOUD=9_

**Set volume to a percentage \(0 to 100%\)**

> Hey Chatterbox, set audio to 75 percent   
> Hey Chatterbox, decrease volume to 50 percent

**Set to maximum volume**

> Hey Chatterbox, crank it all the way up   
> Hey Chatterbox, set audio to max

**Increase volume by one numeric level**

> Hey Chatterbox, raise the sound  
> Hey Chatterbox, make it higher  
> Hey Chatterbox, louder

**Decrease volume by one numeric level**

> Hey Chatterbox, lower the sound  
> Hey Chatterbox, make it quieter  
> Hey Chatterbox, softer

**Mute**

> Hey Chatterbox, mute the volume   
> Hey Chatterbox, silence the audio

**Unmute**

> Hey Chatterbox, unmute the speaker   
> Hey Chatterbox, restore the sound

### Weather

An interface to OpenWeatherMap.org that supports an extensive set of queries.

> Hey Chatterbox, what is the weather?   
> Hey Chatterbox, what is the forecast tomorrow?   
> Hey Chatterbox, what is the weather going to be like Tuesday?   
> Hey Chatterbox, what is the weather in Houston?   
> Hey Chatterbox, when will it rain next?   
> Hey Chatterbox, how windy is it?   
> Hey Chatterbox, what's the humidity?   
> Hey Chatterbox, is it going to snow?   
> Hey Chatterbox, what's the temperature?

### Wiki

Interfaces to Wikipedia.org

**Query Wikipedia**

> Hey Chatterbox, what does Wikipedia say about chocolate?   
> Hey Chatterbox, tell me about artificial intelligence   
> Hey Chatterbox, search Grace Hopper

**Ask Wikipedia for more details on same subject**

> Hey Chatterbox, tell me more   
> Hey Chatterbox, please continue

**Let Wikipedia select the subject**

> Hey Chatterbox, teach me something   
> Hey Chatterbox, tell me a random thing

## The Fallback Handlers

Chatterbox has two _fallback_ handlers for the situation where the natural language processing fails to match a specific **Intent** and **Skill**; one for queries and one for unknowns.

By default, Chatterbox has access to two general purpose search engines: Duck Duck Go and Wolfram Alpha. When the **utterance** is a query, Chatterbox sends it to all of these Common Query search engines simultaneously. The first engine to reply successfully is the search engine selected by Chatterbox to reply to the User.

If no search engine provides a successful answer to the query, or if the **utterance** was not a query, then Chatterbox activates the Unknown Handler that responds with a variety of phrases explaining that Chatterbox cannot handle the **utterance**.

### Common Query

Sent to all _fallback_ Common Query search engines.

> Hey Chatterbox, what is Frankenstein?   
> Hey Chatterbox, who is Kathryn Johnson?   
> Hey Chatterbox, how high is Mount Everest?   
> Hey Chatterbox, how many inches in a meter?

### Subsequent Commands to a Common Query

A Common Query search engine may optionally support subsequent commands \(e.g. "send me details"\) that are processed if that search engine handled the initial query.

#### Subsequent commands for Wolfram Alpha:

**Have more details of last query emailed to User**

> Hey Chatterbox, send me details on that   
> Hey Chatterbox, email sources to me

## More information on Skills

For more information on Skills, please see the [Skills section](http://chatterbox.ai/documentation/skills/)

