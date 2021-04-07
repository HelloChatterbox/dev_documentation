---
description: >-
  Speech-To-Text (STT) is the process of converting audio of spoken words into
  strings of text. Chatterbox supports a range of Speech-To-Text engines.
---

# Speech-To-Text

Many users want to use a specific STT engine rather than the default. Like most of Chatterbox's technology stack, this too can be customized.

## Default Engine

For a voice assistant like Chatterbox, speech recognition must be performed very quickly and with a high degree of accuracy. For this reason, Chatterbox by default uses Google's STT engine.

In order to provide an additional layer of privacy for our users, we proxy all STT requests through Chatterbox's servers. This prevents Google's service from profiling Chatterbox users or connecting voice recordings to their identities. Only the voice recording is sent to Google, no other identifying information is included in the request. Therefore Google's STT service does not know if an individual person is making thousands of requests, or if thousands of people are making a small number of requests each.

By supporting Mozilla's DeepSpeech project we are aiming to provide a competitive open source alternative. The accuracy of DeepSpeech is not yet sufficient to provide a quality experience for Chatterbox users. However we will be switching to DeepSpeech by default as soon as we have achieved an acceptable level of accuracy.

The following are some of the available STT options. Each provides details on how to get setup, and how to configure Chatterbox.

### Community Support


## Mozilla DeepSpeech

Mozilla's DeepSpeech, an open Speech-to-Text technology based on Baidu’s Deep Speech architecture and implemented with Google’s TensorFlow framework.
Being open source means that if you have the hardware, it can be run within your own network providing additional privacy and control for you and your family.

### Server Setup

You can test DeepSpeech using their pre-trained model by following the instructions on the [DeepSpeech Github repository](https://github.com/mozilla/DeepSpeech#project-deepspeech).

To setup a DeepSpeech server that Chatterbox can use, try the [deepspeech-server project on PyPI](https://pypi.org/project/deepspeech-server/). Once you have this up and running, we can configure Chatterbox to use this server.

### Chatterbox Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `chatterbox.conf` file

To our existing configuration values we will add the following:

```javascript
  "stt": {
    "deepspeech_server": {
      "uri": "http://localhost:8080/stt"
    },
    "module": "deepspeech_server"
  }
```

### Community Support

If you are interested in the continued development of the DeepSpeech STT engine, please join our the [DeepSpeech channel on Chatterbox Chat](https://chat.chatterbox.ai/community/channels/deepspeech-stt).

## Kaldi

[Kaldi](http://kaldi-asr.org/) is described as a toolkit for speech recognition written in C++ and licensed under the Apache License v2.0. It is intended for use by speech recognition researchers.

Kaldi can be run on a Linux cluster or an individual machine, making it another option for those wanting local network speech-to-text.

### Server Setup

First be sure to read the [system requirements in the Kaldi documentation](https://kaldi-asr.org/doc/dependencies.html).

The latest installation instructions can be found on the [Kaldi Github repository](https://github.com/kaldi-asr/kaldi#kaldi-speech-recognition-toolkit).

### Chatterbox Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `chatterbox.conf` file

To our existing configuration values we will add the following:

```javascript
  "stt": {
    "kaldi": {
      "uri": "http://localhost:8080/client/dynamic/recognize"
    },
    "module": "kaldi"
  }
```

## Google Cloud

The standard [Google Cloud Speech-To-Text API](https://cloud.google.com/speech-to-text/).

### Account Setup

A [Google Cloud account](https://cloud.google.com/) with active billing is required. 
Please carefully consider the [financial cost of using this service](https://cloud.google.com/speech-to-text/pricing).

To obtain the required credential JSON data, you must create a Google API Console project. To do this:

* Select or create a GCP project in the [Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager)
* Make sure that billing is enabled for your project - [see documentation](https://cloud.google.com/billing/docs/how-to/modify-project)
* Enable the Cloud Text-to-Speech API from your [GCP Console](https://console.cloud.google.com/apis/dashboard)
* Set up authentication:
  * Go to the [Create service account key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey) in the GCP Console
  * From the Service account drop-down list, select New service account.
  * Enter a name into the Service account name field.
  * Don't select a value from the Role drop-down list. No role is required to access this service.
  * Click Create. A note appears, warning that this service account has no role.
  * Click Create without role. A JSON file that contains your key downloads to your computer.

Remember to activate the API in the [GCP Console](https://console.developers.google.com/apis/library/speech.googleapis.com?)

### Chatterbox Configuration

Using the [Configuration Manager](config-manager.md) we can edit the `chatterbox.conf` file 
To our existing configuration values we will add the following:

```javascript
"stt": {
  "google_cloud": {
    "lang": "hi-in",
    "credential": {
      "json": {
        "type": "service_account",
        "project_id": "xxxxxxxxxx",
        "private_key_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "private_key": "-----BEGIN PRIVATE KEY-----nxxxxxxxxxxxxxxxxn-----END PRIVATE KEY-----n",
        "client_email": "xxxx@xxxx.iam.gserviceaccount.com",
        "client_id": "xxxxxxxxxxxxxxxxxxxxx",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/xxxxxx.iam.gserviceaccount.com"
      }
    }
  },
  "module": "google_cloud"
},
```

## Google Cloud Streaming STT

A streaming STT interface for the Google Cloud Speech-To-Text API.

### Account Setup

A [Google Cloud account](https://cloud.google.com/) with active billing is required.
Please carefully consider the [financial cost of using this service](https://cloud.google.com/speech-to-text/pricing).

### Chatterbox Configuration

Install `google-cloud-speech` in the Chatterbox Virtual environment using:

```text
/pip install google-cloud-speech
```

Then, using the [Configuration Manager](config-manager.md) we can edit the `chatterbox.conf` file

To our existing configuration values we will add the following:

```javascript
"stt": {
  "google_cloud_streaming": {
    "credential": {
      "json": # Paste Google API key JSON here
    }
  },
  "module": "google_cloud_streaming"
}
```