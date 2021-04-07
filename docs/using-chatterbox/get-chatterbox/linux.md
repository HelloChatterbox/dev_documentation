---
description: >-
  Install Chatterbox on Linux, learn how to start and stop services, configure
  proxies, or remove Chatterbox from your system.
---

# Linux

## Prerequisites

This section of documentation assumes the following:

* That you already have Linux installed on your computer
* That your computer is already connected to the internet
* That you are comfortable issuing basic Linux commands from a **terminal** or **shell prompt**
* That your device has a built-in microphone and speakers, or, you have successfully connected microphone and speakers to your device.
* That your device already has `git` installed and working. If you don't already have `git` installed, [here is a great set of instructions](https://gist.github.com/derhuerst/1b15ff4652a867391f03).

### System Requirements

Whilst Chatterbox runs on a Raspberry Pi 3B or above, this is achieved through a custom release of Raspbian Lite significantly reducing the system overhead by not running a desktop environment and other unnecessary processes. Chatterbox will run on older hardware however your experience may vary significantly.

Our [Precise wake word engine](https://github.com/ChatterboxAI/chatterbox-precise#chatterbox-precise) also relies upon TensorFlow. For x86 Intel processors this requires the AVX \(Advanced Vector Extensions\) instruction set. To ensure your system supports AVX open a terminal and run: `grep avx /proc/cpuinfo`. AVX should be listed under the flags for each CPU core. If nothing is returned it is most likely that your system does not support AVX. Technical users may be able to build an older version of TensorFlow \(1.13\) from source using the [instructions provided on their website](https://www.tensorflow.org/install/source). Alternatively you may use Chatterbox with the PocketSphinx wake word engine; see \(Switching Wake Word Listeners\)\[../customizations/wake-word\#switching-wake-word-listeners\].

The ARM architecture has a similar requirement called SIMD \(Single Instruction, Multiple Data\). This has been available since ARMv7 which includes the Cortex A53 used by the RaspberryPi and the Cortex A7 from the OrangePi.

## Getting Started

There are multiple ways to install Chatterbox for Linux.

### Installing via git clone

The simplest way to install Chatterbox for Linux is to clone the `chatterbox-core` repo to your system and run a shell script, which will install all dependencies, and [Chatterbox components](http://chatterbox.ai/documentation/chatterbox-software-hardware/).

The `chatterbox-core` repo is at [https://github.com/ChatterboxAI/chatterbox-core](https://github.com/ChatterboxAI/chatterbox-core).

The instructions below will install Chatterbox in your HOME directory.

```text
cd ~/
git clone https://github.com/ChatterboxAI/chatterbox-core.git
cd chatterbox-core
bash dev_setup.sh
```

The `dev_setup.sh` script identifies, installs and configures dependencies that Chatterbox needs to run.

The script will also install and configure [virtualenv](https://virtualenv.pypa.io/en/stable/). `virtualenv` is a tool to create isolated Python environments. It is a way to isolate an application - in this case Chatterbox - from other applications. It helps to better manage both dependencies and security.

If you are running a Linux distribution other than Ubuntu, Debian, Arch or Fedora, you may need to manually install packages as instructed by `dev_setup.sh`.

## Running Chatterbox for Linux

The Chatterbox for Linux installation includes two scripts that you use to control Chatterbox services.

### start-chatterbox.sh

`start-chatterbox.sh` is used to start one, or all, Chatterbox services. This script uses the `virtualenv` created by `dev_setup.sh`.

The usage of `start-chatterbox.sh` is:

```text
usage: start-chatterbox.sh [command] [params]

Services:
  all                      runs core services: bus, audio, skills, voice
  debug                    runs core services, then starts the CLI

Services:
  audio                    the audio playback service
  bus                      the messagebus service
  skills                   the skill service
  voice                    voice capture service
  wifi                     wifi setup service
  enclosure                mark_1 enclosure service

Tools:
  cli                      the Command Line Interface
  unittest                 run chatterbox-core unit tests

Utils:
  skill_container <skill>  container for running a single skill
  audiotest                attempt simple audio validation
  audioaccuracytest        more complex audio validation
  sdkdoc                   generate sdk documentation

Examples:
  start-chatterbox.sh all
  start-chatterbox.sh cli
  start-chatterbox.sh unittest
```

#### To start all Chatterbox services at once

```text
$ ./start-chatterbox.sh all
Starting all chatterbox-core services
Initializing...
Starting background service bus
Starting background service skills
Starting background service audio
Starting background service voice
```

#### To start individual Chatterbox services

Services can also be started individually.

```text
$ ./start-chatterbox.sh audio
Initializing...
Starting background service audio
```

### Stopping Chatterbox services

```text
$ ./stop-chatterbox.sh
Stopping all chatterbox-core services
```

## Start Chatterbox on boot

You could create a chatterbox service to get Chatterbox automatic started on boot.

For this create a file named `/etc/systemd/system/chatterbox.service` with the following content:

```text
[Unit]
Description=Chatterbox AI
After=pulseaudio.service

[Service]
User=pi
WorkingDirectory=/home/pi/
ExecStart=/home/pi/chatterbox-core/bin/chatterbox-start all
ExecStop=/home/pi/chatterbox-core/bin/chatterbox-stop
Type=forking
Restart=no

[Install]
WantedBy=multi-user.target
```

Please modify `WorkingDirectory` and `User` to your needs. Reload the unit files with `sudo systemctl daemon-reload`and then, enable the new created service with `sudo systemctl enable chatterbox.service` . You could start Chatterbox by running `sudo systemctl start chatterbox.service` stop it by `sudo systemctl stop chatterbox.service` and get the status by typing `sudo systemctl status chatterbox.service`.

## Pairing Chatterbox for Linux

Once successfully installed, you will need to **pair** your Chatterbox for Linux **Device** with your [home.chatterbox.ai](https://home.chatterbox.ai) account.

Speak

> Hey Chatterbox, pair my device

Chatterbox will Speak `"I am connected to the internet and need to be paired. Your 6-digit Registration Code is XXXXXX"`

Use the **Registration Code** to pair your Chatterbox for Linux **Device** with home.chatterbox.ai.

[View the home.chatterbox.ai documentation to learn how to add your Device to home.chatterbox.ai](http://chatterbox.ai/documentation/home-chatterbox-ai-pairing/).

Once paired, you can then use [basic Skills](http://chatterbox.ai/documentation/basic-commands/).

## Using Chatterbox behind a proxy

Many schools, universities and workplaces run a `proxy` on their network. If you need to type in a username and password to access the external internet, then you are likely behind a `proxy`.

If you plan to use Chatterbox behind a proxy, then you will need to do an additional configuration step.

_NOTE: In order to complete this step, you will need to know the `hostname` and `port` for the proxy server. Your network administrator will be able to provide these details. Your network administrator may want information on what type of traffic Chatterbox will be using. We use `https` traffic on port `443`, primarily for accessing ReST-based APIs._

## Using Chatterbox behind a proxy without authentication

If you are using Chatterbox behind a proxy without authentication, add the following environment variables, changing the `proxy_hostname.com` and `proxy_port` for the values for your network. These commands are executed from the Linux command line interface \(CLI\).

```bash
$ export http_proxy=http://proxy_hostname.com:proxy_port
$ export https_port=http://proxy_hostname.com:proxy_port
$ export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com,0.0.0.0,::1"
```

## Using Chatterbox behind an authenticated proxy

If you are behind a proxy which requires authentication, add the following environment variables, changing the `proxy_hostname.com` and `proxy_port` for the values for your network. These commands are executed from the Linux command line interface \(CLI\).

```bash
$ export http_proxy=http://user:password@proxy_hostname.com:proxy_port
$ export https_port=http://user:password@proxy_hostname.com:proxy_port
$  export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com,0.0.0.0,::1"
```

### Keeping Chatterbox for Linux updated

Keeping your `chatterbox-core` installation up to date is simple.

1. Change to the directory where your `chatterbox-core` installation is. This is most likely at `~/chatterbox-core`
2. Type `git stash` - this preserves your Chatterbox configuration. `git` may prompt you to [set up an identity](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).
3. Type `git pull` to get the latest code. By default, using a `git` installation will bring down the `dev` branch of the repo. If you want to pull down another branch - for instance to test it - use `git pull origin BRANCH_NAME`.
4. Type `git stash pop` to return the configuration that was stashed with `git stash`
5. Type `./update_dev.sh` to update your `virtualenv` - it's a good idea to do this if you update your `chatterbox-core` installation.
6. Type `./start-chatterbox.sh all` to restart the services

## Removing Chatterbox for Linux from your system

If you have installed `chatterbox-core` using the `git-clone` method, you can remove all files and directories that have been created by Chatterbox using the `--clean` flag:

```bash
cd ~/chatterbox-core # or the path to your chatterbox-core installation
./dev_setup --clean
```

This does not remove the cloned `chatterbox-core` project directory. If cloned directly into the home directory, this can be removed with:

```text
rm -rf ~/chatterbox-core
```

{% hint style="danger" %}
**Warning: always be very careful when running `rm -rf` commands. Running this command on the wrong directory can delete your entire filesystem. Run `rm --help` for more details.**
{% endhint %}

Alternatively you can manually remove these files using the following commands:

```bash
sudo rm -rf /var/log/chatterbox # Log files
rm -f /var/tmp/chatterbox_web_cache.json # Configuration from Home.chatterbox.ai
rm -rf "${TMPDIR:-/tmp}/chatterbox" # Temp files
rm -rf "$HOME/.chatterbox" # User level configuration
sudo rm -rf /opt/chatterbox # Chatterbox Skills directory
rm -rf "$HOME/chatterbox-core" # Chatterbox-core installation
```

{% hint style="info" %}
Depending on your system, you may need to run the commands with `sudo`
{% endhint %}

## Snap Package

A pre-Alpha Snap package is available, with the aim to provide a simple and secure means of installing Chatterbox on a broad range of Linux distributions.

The Snap package currently has a number of major usability bugs that need to be addressed before it will be promoted to an installable channel. For now we recommend the git clone method above, but we welcome any help in improving Chatterbox as a Snap:

{% page-ref page="snap.md" %}

## Troubleshooting

{% page-ref page="../troubleshooting/" %}

