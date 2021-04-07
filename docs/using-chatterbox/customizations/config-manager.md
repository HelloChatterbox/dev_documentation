---
description: >-
  The chatterbox settings UI simplifies management of the various configuration files that control Chatterbox. 
---

# Configuration Manager

## About Chatterbox Configurations

Chatterbox configurations are stored in [chatterbox.conf](chatterbox-conf.md) files. These exist in four locations:

* Default - chatterbox-core/chatterbox/configuration/chatterbox.conf
* Remote - Home.Chatterbox.ai
* System - /etc/chatterbox/chatterbox.conf
* User - $HOME/.chatterbox/chatterbox.conf

When the configuration loader starts, it looks in these locations in this order, and loads **all** configurations. 
Keys that exist in multiple configuration files will be overridden by the last file to contain the value.

The chatterbox settings UI simplifies management of the various configuration files that control Chatterbox.

## Further information

For more information on the configuration options available, continue to the [chatterbox.conf documentation](chatterbox-conf.md).

