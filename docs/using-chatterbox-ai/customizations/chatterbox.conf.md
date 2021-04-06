# chatterbox.conf

{% hint style="info" %}
See a [list of all variables available within `chatterbox.conf`](https://github.com/ChatterboxAI/chatterbox-core/blob/master/chatterbox/configuration/chatterbox.conf)
{% endhint %}

### What is `chatterbox.conf`?

`chatterbox.conf` is a [JSON](https://www.json.org/)-formatted file that is saved locally on your Chatterbox Device, such as Picroft or Mark 1. `chatterbox-conf` contains information about the Device itself, like what type of Device and Enclosure it is, as well as information about user preferences. If you haven't specified preferences, then `chatterbox.conf` will contain some default values. Your Device, and Skills installed on your Device, use `chatterbox.conf` to provide additional functionality.

### Where are the `chatterbox.conf` files stored?

The `chatterbox.conf` files are stored in four possible locations:

1. Default - chatterbox-core/chatterbox/configuration/chatterbox.conf
2. Remote \(from Home.Chatterbox.ai\) - /var/tmp/chatterbox\_web\_cache.json
3. System - /etc/chatterbox/chatterbox.conf
4. User - $HOME/.chatterbox/chatterbox.conf

Chatterbox implements an order of precedence; settings defined at a User level override those at a System level. If the file does not exist, Chatterbox moves to the following level.

### A look at the inside of `chatterbox.conf`

Here is an example System level `chatterbox.conf` from a Mark 1 Device:

```text
pi@mark_1:/etc/chatterbox $ cat chatterbox.conf
{
  "enclosure": {
    "platform": "chatterbox_mark_1",
    "platform_build": 9,
    "port": "/dev/ttyAMA0",
    "rate": 9600,
    "timeout": 5,
    "update": true,
    "test": false
  },
  "VolumeSkill": {
    "default_level": 6,
    "min_volume": 0,
    "max_volume": 83
  }
}
```

{% hint style="info" %}
See a [list of all variables available within `chatterbox.conf`](https://github.com/ChatterboxAI/chatterbox-core/blob/master/chatterbox/configuration/chatterbox.conf)\`\`
{% endhint %}

### `chatterbox_web_cache.json`

`chatterbox_web_cache.json` is is a [JSON](https://www.json.org/)-formatted file that is saved locally on your Chatterbox Device, such as Picroft or Mark 1. `chatterbox_web_cache.json` is a cached copy of the settings on your [home.chatterbox.ai](https://home.chatterbox.ai) account, such as your _Location_ \(which determines _Time Zone_\), which _Voice_ you have selected and your preference for _Measurements_ such as temperature and distance.

Both of these files are regularly used in troubleshooting, so it's useful to know what information they hold, and where they are stored on your Device.

#### Where is the `chatterbox_web_cache.json` file stored?

This file is stored at:

`/var/tmp/chatterbox_web_cache.json`

on the Device.

#### How is `chatterbox_web_cache.json` updated?

When you update settings at [home.chatterbox.ai](https://home.chatterbox.ai), your Device will periodically pull them down. In normal circumstances any change should be reflected on the device within 1-2 minutes. You can also instruct your device to pull down the latest configuration, by saying:

> Hey Chatterbox, update configuration

Chatterbox will respond in one of two ways:

* If your configuration was out of date, and has been pulled down again, Chatterbox will respond:

> Configuration updated

* If your configuration was the same on your device as on home.chatterbox.ai, Chatterbox will respond:

> Your device has been configured

#### Reading values directly from `chatterbox_web_cache.json`

To see the city location value:

`jq ".location.city" < /var/tmp/chatterbox_web_cache.json`

To see the latitude and longitude coordinates of your location:

`jq ".location.coordinate" < /var/tmp/chatterbox_web_cache.json`

To see the timezone setting:

`jq ".location.timezone" < /var/tmp/chatterbox_web_cache.json`

To see the listener setting:

`jq ".listener" < /var/tmp/chatterbox_web_cache.json`

To see the Speech to Text \(STT\) settings:

`jq ".stt" < /var/tmp/chatterbox_web_cache.json`

To see the Text to Speech \(TTS\) settings:

`jq ".tts" < /var/tmp/chatterbox_web_cache.json`

#### A look at the inside of `chatterbox_web_cache.json`

Here is an example `chatterbox_web_cache.json`.  
_NOTE: Your settings will be different._

```javascript
{
  "date_format": "DMY",
  "tts": {
    "google": {
      "created_at": 1504481866992,
      "updated_at": 1514794901075
    },
    "module": "mimic",
    "fatts": {
      "created_at": 1504481866991,
      "updated_at": 1514794900939
    },
    "mimic": {
      "created_at": 1504481866989,
      "voice": "ap",
      "updated_at": 1514794900809
    },
    "espeak": {
      "created_at": 1504481866987,
      "updated_at": 1514794900679
    },
    "marytts": {
      "created_at": 1504481866986,
      "updated_at": 1514794900548
    }
  },
  "opt_in": true,
  "created_at": 1504481866955,
  "updated_at": 1514794898083,
  "listener": {
    "energy_ratio": 1.5,
    "created_at": 1504481866996,
    "updated_at": 1514794901398,
    "channels": 1,
    "sample_rate": 16000,
    "multiplier": 1,
    "threshold": 1e-90,
    "phonemes": "HH EY . M AY K R AO F T",
    "wake_word": "hey chatterbox"
  },
  "time_format": "full",
  "skills": {
    "directory": "~/.chatterbox/skills",
    "created_at": 1504481866994,
    "updated_at": 1514794901226,
    "stop_threshold": 2
  },
  "stt": {
    "google": {
      "credential": {
        "created_at": 1504481866970,
        "updated_at": 1514794899383
      },
      "created_at": 1504481866970,
      "updated_at": 1514794898989
    },
    "ibm": {
      "credential": {
        "created_at": 1504481866958,
        "updated_at": 1514794898334
      },
      "created_at": 1504481866958,
      "updated_at": 1514794898218
    },
    "chatterbox": {
      "credential": {
        "created_at": 1504481866965,
        "updated_at": 1514794898856
      },
      "created_at": 1504481866965,
      "updated_at": 1514794898469
    },
    "module": "chatterbox",
    "wit": {
      "credential": {
        "created_at": 1504481866981,
        "updated_at": 1514794900417
      },
      "created_at": 1504481866981,
      "updated_at": 1514794900031
    },
    "openstt": {
      "credential": {
        "created_at": 1504481866976,
        "updated_at": 1514794899900
      },
      "created_at": 1504481866976,
      "updated_at": 1514794899521
    }
  },
  "location": {
    "coordinate": {
      "latitude": -38.149918,
      "created_at": 1504500674753,
      "updated_at": 1504500674753,
      "longitude": 144.361719
    },
    "city": {
      "created_at": 1504500674710,
      "state": {
        "country": {
          "created_at": 1486125571309,
          "code": "AU",
          "name": "Australia",
          "updated_at": 1486125571309
        },
        "created_at": 1489950675941,
        "code": "VIC",
        "name": "Victoria",
        "updated_at": 1489950675941
      },
      "code": "Newtown",
      "name": "Newtown",
      "updated_at": 1504500674710
    },
    "created_at": 1504500674709,
    "updated_at": 1504500674709,
    "timezone": {
      "code": "Australia/Melbourne",
      "name": "Australian Eastern Standard Time (Victoria)",
      "dst_offset": 3600000,
      "created_at": 1489950676105,
      "updated_at": 1489950676105,
      "offset": 36000000
    }
  },
  "enclosure": {
    "created_at": 1504481866997,
    "rate": 9600,
    "updated_at": 1514794901541,
    "timeout": 5,
    "port": "/dev/ttyAMA0"
  },
  "system_unit": "metric"
}
```

