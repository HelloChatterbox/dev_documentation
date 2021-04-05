---
description: >-
  A Skill's `manifest.yml` file is the default method for defining the
  dependencies of a Chatterbox Skill.
---

# Manifest.yml

In this file we can include Python packages, Linux applications or other Chatterbox skills that are required for our own Skill to function properly.

{% hint style="info" %}
[YAML](https://en.wikipedia.org/wiki/YAML) is a language commonly used for configuration files.
It uses indentation rather than brackets or parentheses to define the structure or hierarchy of its contents.
{% endhint %}

## File contents

We start the `manifest.yml` by defining a top-level key of `dependencies` and the type of dependency we want to include.

```yaml
dependencies:
  python:
```

### Python Packages

Here we can see a simple example that defines the `requests` and `gensim` Python packages as required dependencies.

```yaml
dependencies:
  python:
    - requests
    - gensim
```

When a Skill with this `manifest.yml` file is being installed, Chatterbox would check for, and if required install, both packages from [PyPI](https://pypi.org/) using the PIP installer.

There is no limit to the number of packages you can install

### Linux System Packages

Linux packages are defined under the `system` key. 

```yaml
dependencies:
  system:
    apt-get: fortune
```


### Other Chatterbox Skills

A Skill may even require that other Chatterbox Skills are installed rather than duplicate functionality. 

```yaml
dependencies:
  skill:
    - https://github.com/JarbasSkills/skill-wolfie
```

## Example files

A complete `manifest.yml` example can be found in the [official Template Skill on Github](https://github.com/ChatterboxAI/chatterbox-skills/blob/19.08/00__skill_template/manifest.yml).

A simple example from a real Skill can be found in the [Desktop Launcher Skill](https://github.com/ChatterboxAI/skill-desktop-launcher/blob/19.08/manifest.yml).

