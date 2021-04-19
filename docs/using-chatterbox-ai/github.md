---
description: >-
  Skills are like apps for a voice assistant. They give Chatterbox access to new
  information and new abilities.
---

# Installing New Skills

To install a skill you first need to publish it in github

This is intended for developer skills written in python

* Mycroft skills are supported
* skills without `blocks.xml` can not be loaded in the skill builder
* skills only with `blocks.xml` file need to be deployed in the skill builder after the install step

{% hint style="info" %}
For regular chatterbox skills we recommend copy-pasting the xml directly into the skill builder and clicking the deploy button
{% endhint %}

## Repository structure

Each skill repo needs to follow this structure:

* repo\_name
  * `__init__.py`
  * locale
    * en-us
      * say\_this.dialog
      * hear\_this.intent
  * readme.md        \(optional\)
  * manifest.yaml    \(optional\)
  * skill\_meta.json  \(optional\)

## Deploying from github

to deploy a skill to your chatterbox you need to use the chat interface

```text
/install https://github.com/HelloChatterbox/hello-world-test-skill/
```

you can also install skills from a specific branch/release/tag

```text
/install https://github.com/HelloChatterbox/hello-world-test-skill/tree/dev
```

or install skills from a pinned commit

```text
/install https://github.com/HelloChatterbox/hello-world-test-skill/commit/5491658ee22573c848b1a65d73ebb2f2310cf053
```

installing from private repositories is not currently supported

## Updating skills

to update a skill simply install it again, the old skill will be replaced

this also works for changing between branches

## Deleting skills

the skills will show in the skills cards together with regular chatterbox skills, you can enable/disable and delete skills as usual

