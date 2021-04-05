---
description: >-
  Pairing makes information available to your Device to personalise your
  experience, such as which units of measurement you prefer, and your general
  location.
---

# Pairing Your Device

Each of your Chatterbox **Device\(s\)** must be **Paired** with your [home.chatterbox.ai](https://home.chatterbox.ai) account.

Pairing makes information available to your Device to personalise your experience, such as which units of measurement you prefer, and your general location.

Pairing is also used for services that require API authentication, such as

* Wolfram Alpha
* Google Speech to Text
* Weather Skill API and OpenWeather

## Adding a Device

To add a Device to your home.chatterbox.ai account, you will need a 6-character **Registration Code**. The Registration Code is provided in different ways depending on which **Device** you have.

### Getting a Registration Code

After your device has connected to the internet, Chatterbox will speak a unique six character code. For the Registration Code CKAMP7, Chatterbox would say:

```text
I'm connected to the internet and need to be registered. Go to home.chatterbox.ai and use the Registration Code
C for Charlie
K for Kilo
A for Apple
M for Mike
P for Pa
number 7
```

Your pairing code will be different.

#### Picroft

After you have connected your Picroft to Wifi, Chatterbox will speak a 6-character **Registration Code**.

If you're stuck connecting to Wifi, please read the [Picroft documentation](http://chatterbox.ai/documentation/picroft/).

### Pairing your Device\(s\) to your home.chatterbox.ai account

Once you have your Registration Code, you can then go to home.chatterbox.ai -&gt; Add Device.

Use your Pairing Code, and provide a meaningful name and location for the Device. This will help you in the future if you have multiple devices. All other options will be pre-filled from your [default device settings](pairing-your-device.md#defaults), but can be changed for each individual device.

![Adding a new Device](https://chatterbox.ai/wp-content/uploads/2019/06/Add-device.png)

Once complete, click 'NEXT' to pair the Device. Wait a few seconds, and then you'll be taken to a new screen confirming your Pairing has been successfully completed.

Congratulations! Your Chatterbox Device is now paired, and is ready to start accepting your commands.

### Where is my identity information stored in the Chatterbox code?

Once you have paired your Chatterbox Device, pairing information is stored in:

`~/.chatterbox/identity/identity2.json`

DO NOT SHARE THIS INFORMATION WITH OTHERS - IT IS YOUR CHATTERBOX IDENTITY

You may be asked for this information by Chatterbox support staff while troubleshooting Device and/or Pairing issues.

## Device Settings

Settings available:

* **Name** - a unique name for your device.
* **Placement** - location of your device e.g. Kitchen, Bedroom or Office. This is in place for location based utterances such as "turn off the light" which should only turn off lights in the current location, not all lights connected to your account.
* **Geographical Location** - your devices approximate geographical location, used for queries such as the local weather and time.
* **Voice** - By default, Chatterbox will use the `American Male` voice, however you are free to choose other voices.
* **Wake Word** - By default, Chatterbox will listen for "Hey Chatterbox" to activate. A number of other pre-trained Wake Words are available. Additional configuration options are available through [advanced settings](pairing-your-device.md#advanced-settings) or by training your own [Precise](https://chatterbox.ai/documentation/precise) Wake Word model.

### Preferences

These allow you to choose your preferred:

* Units of measurement

  \(_NOTE: choosing Miles instead of Kilometers will also switch your temperature format to Fahrenheit instead of Celsius_\)

* Time format
* Date format

All your Chatterbox devices will use this information to tailor your experience.

### Defaults

The Device Default settings define your base configuration and will be used for any new device being added to your account. These may then be modified for each device.

### Advanced settings

Advanced users may configure additional options using an on-device configuration file. This includes setting an alternative speech-to-text engine, text-to-speech engine, or wake word listener. See the [`chatterbox.conf` documentation](https://chatterbox.ai/documentation/chatterbox-conf/) for more detail.
