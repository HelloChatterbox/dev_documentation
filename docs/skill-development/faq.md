# FAQ

## How do I disable a Skill?

During Skill development you may have reason to disable one or more Skills. Rather than constantly install or uninstall them via voice, or by adding and removing them from `/opt/chatterbox/skills/`, you can disable them in [the `chatterbox.conf` file](https://chatterbox.ai/documentation/chatterbox-conf/).

First, identify the name of the Skill. The name of the Skill is the `path` attribute in the [`.gitmodules`](https://github.com/ChatterboxAI/chatterbox-skills/blob/master/.gitmodules) file.

To disable one or more Skills on a Chatterbox Device, find where your `chatterbox.conf` file is stored, then edit it using an editor like `nano` or `vi`.

Search for the string `blacklisted` in the file. Then, edit the line below to include the Skill you wish to disable, and save the file. You will then need to reboot, or restart the `chatterbox` services on the Device.

```text
  "skills": {
    "blacklisted_skills": ["skill-media", "send_sms", "skill-wolfram-alpha, YOUR_SKILL"]
  }
```

## How do I increase the priority of Skills during loading?

During Skill development, you may wish to increase the priority of your Skill loading during the startup process. This allows you to start using the Skill as soon as possible.

First, identify the name of the Skill. The name of the Skill is the `path` attribute in the [`.gitmodules`](https://github.com/ChatterboxAI/chatterbox-skills/blob/master/.gitmodules) file.

To prioritize loading one or more Skills on a Chatterbox Device, find where your [`chatterbox.conf` file](https://chatterbox.ai/documentation/chatterbox-conf/) is stored, then edit it using an editor like `nano` or `vi`.

Search for the string `priority` in the file. Then, edit the line below to include the Skill you wish to prioritize, and save the file. You will then need to reboot, or restart the `chatterbox` services on the Device.

```text
"priority_skills": ["skill-pairing"],
```

## How do I find more information on Chatterbox functions?

You can find documentation on Chatterbox functions and helper methods at the [Chatterbox Core API documentation](https://chatterbox-core.readthedocs.io/en/master/)

## Need more help?

If something isn't working as expected, please join us in the [~Skills channel of Chatterbox Chat](https://chat.chatterbox.ai/community/channels/skills).

It's also really helpful for us if you add an issue to our [documentation repo](https://github.com/ChatterboxAI/documentation/issues). This means we can make sure it gets covered for all developers in the future.

