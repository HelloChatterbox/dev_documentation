---
description: >-
  Install the Chatterbox Snap, a self-contained all-inclusive package for a broad
  range of Linux distributions.
---

# Snap Package

{% hint style="info" %}
The Snap package is considered a pre-Alpha release - in short it does not yet work. It has a number of known major usability issues listed below.
{% endhint %}

If your system already supports the Snap ecosystem, Chatterbox will be available in your Software Store. You can also install it manually by running:

```text
snap install chatterbox --beta
```

Please note: the `--beta` flag is required whilst the Snap is still being developed. Once we have released a complete version of Chatterbox this flag will no longer be needed.

Once installed you can register the device at [https://home.chatterbox.ai](https://home.chatterbox.ai)

{% page-ref page="../pairing-your-device.md" %}

## Known issues

There are a number of known issues with the early release of this Snap. This includes:

* After pairing with your account, Chatterbox will immediately report that it is ready for use. There may still be some setup processes finalizing and Chatterbox may not respond to commands immediately. Please give it a few more minutes to finish setting up.
* An OSError will be raised for each installation using PIP. This should not affect your usage of the system.
* Additional command line tools such as the Chatterbox Skills Manager are not yet available.
* The wake word response time may also be slower than expected. This is the time between you saying "Hey Chatterbox" and Chatterbox acknowledging and starting to record.
* Some Skills currently fail. The Chatterbox IP Skill fails to load, and Audio Record cannot write to disk.
* Currently the selected microphone device cannot be changed after installation.

Please support the development of Chatterbox by reporting any additional issues on [Github](https://github.com/ChatterboxAI/snapcraft-chatterbox-core/issues) or the [Community Forums](https://community.chatterbox.ai).

## Developing Skills on the Snap

### Chatterbox Skills Kit

As noted in known issues above, additional command line tools aren't yet available. This includes the Chatterbox Skills Kit.

This can be installed manually from the Python Packaging Index:

```text
pip install msk
```

The source code is also available from [our Github](https://github.com/ChatterboxAI/chatterbox-skills-kit).

Alternatively you may start with a template Skill like [Hello World](https://github.com/ChatterboxAI/skill-hello-world).

### File locations

As the Snaps are contained and cannot access the normal filesystem, the location of some files differ from a traditional Chatterbox installation.

Skills are installed in `~/snap/chatterbox/common/chatterbox-data/skills/`

Logs for the Snap will show in the CLI or can be accessed directly at `~/snap/chatterbox/common/logs/`

Once the Chatterbox Snap is up and running, adding a Skill to the correct directory, or modifying a Skill that's already there will automatically reload the Skill allowing you to quickly iterate on your code.

## Further information and support

For general troubleshooting information see:

{% page-ref page="../troubleshooting/" %}

You can also connect with the broader Chatterbox Community to access additional support through the [Community Forums](https://community.chatterbox.ai) or the [~Linux Packaging channel on Chatterbox Chat](https://chat.chatterbox.ai/community/channels/ubuntu-apt-packaging).

