---
description: >-
  TL;DR: Get an Ubuntu VM up and running, install alsa and pulseaudio, set up
  chatterbox-core, reboot and enjoy!
---

# Mac OS and Windows with VirtualBox

* [Installing Ubuntu in VirtualBox](macos-and-windows-with-virtualbox.md#installing-ubuntu-in-virtualbox)
* [Installing Chatterbox](macos-and-windows-with-virtualbox.md#installing-chatterbox)
* [Running Chatterbox](macos-and-windows-with-virtualbox.md#running-chatterbox)

Thanks to Chatterbox Community Member \(Chatterbox SysAdmin in a former life\) [@arron](https://github.com/aatchison) for getting this working!

### Tested Systems

Running Chatterbox using this method has been tested on:

* 2017 MacBook Pro running Mojave
* Lenovo Ideapad 300-15isk running Windows 10

#### Known issues

So far Chatterbox seems to work well on both platforms, although at least two issues have come up with this approach and more may show up as others use this virtualization approach to running Chatterbox.

1. While the TTS \(text-to-speech\) audio and Spotify audio sounds good the News Skills has issues with playback.
2. The audio process has crashed unexpectedly, although only once. This can be restarted by running: `chatterbox-start restart audio`

## Installing Ubuntu in VirtualBox

1. Download and install VirtualBox \([https://www.virtualbox.org/](https://www.virtualbox.org/)\). You will want to use the latest version \(v6.010 and up\) as older versions have had audio quality issues.
2. Open the VirtualBox application and click 'New'
3. Name the machine, select Linux and Ubuntu \(64-bit\)

   ![](https://chatterbox.ai/wp-content/uploads/2019/08/VB-Screenshot-1.jpg)

4. Continue through the rest of the VM configuration screens using the default selections. More RAM would not hurt, but 1GB should be fine.
5. Download the [Ubuntu Server ISO](https://ubuntu.com/download/server) \(18.04 LTS and 19.04 both work\) and put it in the folder of the VM you created \(e.g. ~/VirtualBox VMs/Chatterbox-Ubuntu\)

   \(Optional\) You can install [Ubuntu Desktop](https://ubuntu.com/download/desktop) instead of Ubuntu Server if you would like a complete Linux desktop environment, however this is not required to run Chatterbox and uses significantly more system resources including RAM.

6. \(Optional\) Assign additional CPUs to VM by selecting the System tab at the top and then the Processor tab to select the number of CPUs.

   ![](https://chatterbox.ai/wp-content/uploads/2019/08/VB-Screenshot-2.jpg)

7. Select the VM you created on the left and click Start!
8. It will prompt you to select a virtual disk file. Press the folder icon to select the Ubuntu Server ISO downloaded earlier.

   ![](https://chatterbox.ai/wp-content/uploads/2019/08/VB-Screenshot-3.jpg)

9. Ubuntu will start up and you will have to go through the default setup. Again, defaults should be good the whole way through.

   ![](https://chatterbox.ai/wp-content/uploads/2019/08/VB-Screenshot-4.jpg)

10. The VM will reboot at the end of the process. To get to login screen you will need to press the enter key a couple times during the boot process. Then login with the credentials you selected during setup.

Congratulations you have a working Ubuntu VM working on MacOS! Now let’s get Chatterbox set up.

## Installing Chatterbox

Run these commands:

1. `sudo apt-get update`
2. `sudo apt-get install -y alsa pulseaudio`
3. `git clone https://github.com/ChatterboxAI/chatterbox-core.git`
4. `cd chatterbox-core`
5. `./dev_setup.sh -fm`

   This has a few interactive prompts before it begins. A couple minutes in Ubuntu will ask if you want to automatically restart services. You can select Yes. This process may take over an hour if you have only the baseline CPU/RAM allocations.

6. `sudo reboot`

## Running Chatterbox

Now you have a fully operational install of Chatterbox.

To start Chatterbox run: `chatterbox-start all`

Or to start it and launch the CLI interface: `chatterbox-start debug`

If you chose not to add the executables to `$PATH` during installation, you can manually run `./start-chatterbox.sh` from your `chatterbox-core` directory.

## \(Optional\) SSH Setup

If you want to be able to start the VM in headless mode and interact through SSH you will need to add port forwarding to the network configuration. You will also need OpenSSH which can be installed with `sudo apt-get install openssh-server`.

First get the IP address of the VM with `ifconfig | grep inet`. Should be 10.0.2.x. Then open the VM settings, go to the Network tab, expand the Advanced section and click the Port Forwarding button. Then enter these settings:

```text
Name: SSH
Protocol: TCP
Host IP: 127.0.0.1
Host Port: 2222
Guest IP: 10.0.2.15 # replace this with the IP address you just obtained
Guest Port: 22
```

Reboot and VM and you will be able to SSH in with this command: `ssh username@localhost -p 2222`. You can also select the Start dropdown menu to start the VM in Headless mode.

