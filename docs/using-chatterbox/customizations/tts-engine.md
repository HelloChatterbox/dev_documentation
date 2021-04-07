---
description: >-
  Text-To-Speech (TTS) is the process of synthesizing audio from text.
---

# Text-To-Speech

## Amazon Polly

[Amazon Polly's](https://aws.amazon.com/polly/) text-to-speech service.

### Account Setup

[Create an AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) and add the Polly service.

You will need to take note of your private "Access Key ID" and "Secret Access Key".

### Chatterbox Configuration

First, check the [list of available voices and languages](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html). Note that Polly does not provide a separate `language` attribute like other TTS options. The language is determined by which voice is chosen.

Then, install the `boto3` python module in the Chatterbox virtual environment:

```bash
/pip install boto3
```

Finally, using the [Configuration Manager](config-manager.md) we can edit the `chatterbox.conf` file 

To our existing configuration values we will add the following:

```javascript
"tts": {
  "module": "polly",
  "polly": {
    "voice": "Matthew",
    "region": "us-east-1",
    "engine": "standard",
    "access_key_id": "YOUR_ACCESS_KEY_ID",
    "secret_access_key": "YOUR_SECRET_ACCESS_KEY"
  }
}
```

If the `voice`, `region`, and `engine` attributes are ommitted the defaults of `Matthew`, `us-east-1` and `standard` will be used. This is an English \(US\) voice.

## Google TTS

Google Translate's text-to-speech API.

## Mozilla TTS

### Server Setup

Instructions for setting up a Mozilla TTS server are [available on the projects wiki](https://github.com/mozilla/TTS/wiki/Build-instructions-for-server).

### Chatterbox Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `chatterbox.conf` file

To our existing configuration values we will add the following:

```javascript
"tts": {
  "module": "mozilla",
  "mozilla": {
    "url": "http://my-mozilla-tts-server/api/tts"
  }
}
```

By default the `url` is set to the localhost: [`http://0.0.0.0:5002/api/tts`](http://0.0.0.0:5002/api/tts) 
So if you are running the server on the same machine as your Chatterbox instance, only the `module` attribute needs to be set. 
