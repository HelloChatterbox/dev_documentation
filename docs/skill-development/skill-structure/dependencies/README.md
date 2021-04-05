---
description: >-
  Chatterbox Skills are powerful because we can make use of external packages and
  applications, or add voice interfaces to existing tools.
---

# Dependencies

There are three main categories of dependencies:

* Python packages sourced from [PyPI](https://pypi.org/).
* Linux system packages sourced from the repositories available on the Chatterbox device.
* Installed Chatterbox Skills

Some of these may already be installed on a Users device, however some may not. 
To make sure a system has everything that your Skill needs, we can define the dependencies or requirements of the Skill. 
During installation the Chatterbox Skills Manager will then check that they are installed, and if not attempt to do so.


`manifest.yml` is the default method.

{% page-ref page="manifest-yml.md" %}


## Manual installation

The file outlined above ensure that dependencies are available on devices when a Skill is being installed by the Chatterbox Skills Manager. 
If you are developing the Skill you may need to install these dependencies manually.

Requirements can be installed using chat commands, for example:

System packages
```bash
/apt install system-package-name
```

Python packages
```bash
/pip install python-package-name
```

Chatterbox Skills
```bash
/install https://github.com/HelloChatterbox/hello-world-test-skill
```
