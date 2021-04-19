---
description: >-
  Information on the different log files Chatterbox uses, where the logs files
  are located on a Chatterbox Device, the sort of data that you will find in
  them, and some common commands to use to aid dia
---

# Log Files

If you request Support from Chatterbox, through the [Chatterbox Forum](https://community.chatterbox.ai), through [Chatterbox Chat](https://chat.chatterbox.ai) or by [contacting us](https://chatterbox.ai/contact/), it is likely we will ask you for _logs_ to help us diagnose the problem.

The [Support Skill](https://market.chatterbox.ai/skill/chatterbox-support-helper) automatically generates links to log files - so if you prefer a less detailed approach, then please use the Support Skill.

## About the Chatterbox logs

The Chatterbox logs each follow a standard format, being:

* A timestamp
* The function or action that was called
* The **level** of the error, which can be one of:
  * DEBUG - incidental information used for debugging purposes
  * INFO - informational log entries which do not indicate an error  
  * WARNING - an error occurred, but it did not stop execution of the **Skill** or process
  * ERROR - an error occurred, and it stopped execution of a **Skill** or other process
  * CRITICAL - a significant error occurred, and it halted execution of the Chatterbox functionality itself

### How to find the Chatterbox logs

The logs on all **Devices** are held at `/var/log/chatterbox/`.

To access the logs enter `/logs` in the chatterbox chat and follow the link

