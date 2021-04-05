---
description: Troubleshooting tips and tricks
---

# General Troubleshooting

This section is grouped by Device to help you quickly find the information you need.

## All Devices

### I've made changes to my settings on home.chatterbox.ai, but these are not reflected on my device

Your Chatterbox device will sync settings with the home.chatterbox.ai server regularly. In normal circumstances any change should be reflected on the device within 1-2 minutes.

You can also instruct your device to pull down the latest configuration, by saying:

> Hey Chatterbox, update configuration

Chatterbox will respond in one of two ways:

* If your configuration was out of date, and has been pulled down again, Chatterbox will respond:

> Configuration updated

* If your configuration was the same on your device as on home.chatterbox.ai, Chatterbox will respond:

> Your device has been configured

### Check settings on my device

To see the settings that your device is using requires access to the devices shell \(terminal\). You can do this by SSHing into your device, or connecting a keyboard and monitor.

The configuration values in use by the system can be obtained using the Configuration Managers `get` command.

{% page-ref page="../customizations/config-manager.md" %}

The settings values that have been retrieved from home.chatterbox.ai can also be read directly from `/var/tmp/chatterbox_web_cache.json`. See [chatterbox.conf](../customizations/chatterbox-conf.md) for more details.

{% page-ref page="../customizations/chatterbox-conf.md" %}

### Find the IP address of my device

To obtain your devices IP address you can say:

> Hey Chatterbox, what is your IP?

Alternatively you can get the IP address from your router, or by scanning the network using a tool like nmap. Running `nmap` with the no port scan flag `-sn` returns the IP and MAC addresses, as well as the vendor name. A Mark 1 will display as "Raspberry Pi Foundation".

