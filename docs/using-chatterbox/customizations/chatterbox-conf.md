---
description: A configuration file that contains the device and service settings.
---

# chatterbox.conf

{% hint style="info" %}
See a [list of all variables available within `chatterbox.conf`](https://github.com/ChatterboxAI/chatterbox-core/blob/master/chatterbox/configuration/chatterbox.conf)
{% endhint %}

## What is `chatterbox.conf`?

`chatterbox.conf` is a [JSON](https://www.json.org/)-formatted file that is saved locally on your Chatterbox Device, such as Picroft or Mark 1. `chatterbox-conf` contains information about the Device itself, like what type of Device and Enclosure it is, as well as information about user preferences. If you haven't specified preferences, then `chatterbox.conf` will contain some default values. Your Device, and Skills installed on your Device, use `chatterbox.conf` to provide additional functionality.

## Where are the `chatterbox.conf` files stored?

The `chatterbox.conf` files are stored in four possible locations:

1. Default - chatterbox-core/chatterbox/configuration/chatterbox.conf
2. System - /etc/chatterbox/chatterbox.conf
3. User - $HOME/.chatterbox/chatterbox.conf

Chatterbox implements an order of precedence; settings defined at a User level override those at a System level. If the file does not exist, Chatterbox moves to the following level.

## A look at the inside of `chatterbox.conf`

Here is an example System level `chatterbox.conf` from a Mark 1 Device:

```text
pi@mark_1:/etc/chatterbox $ cat chatterbox.conf
{
  "enclosure": {
    "platform": "chatterhat"
  }
}
```

{% hint style="info" %}
See a [list of all variables available within `chatterbox.conf`](https://github.com/ChatterboxAI/chatterbox-core/blob/master/chatterbox/configuration/chatterbox.conf)\`\`
{% endhint %}
