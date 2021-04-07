---
description: >-
  Learn how to install Chatterbox for Docker either from a Docker Hub install, or
  by building the image. Many thanks to Brian Hopkins (@btotharye) for this
  documentation.
---

# Docker

Chatterbox is available for `Docker`. You have two options for a `Docker` installation:

* Build Image from source  
* Pull Image from Docker Hub

## Prerequisites

This documentation assumes the following:

* You have already installed `Docker` on your machine based on the operating system you are running.

## Getting Started

### Installing from Docker Hub

The Chatterbox for Docker image is updated on [dockerhub](https://hub.docker.com/r/chatterboxai/docker-chatterbox/) and you can install it by running the command below:

```bash
docker pull chatterboxai/docker-chatterbox
```

Then follow the instructions below for running Chatterbox for Docker.

### Installing via building the Docker image

it pull this repository.

```bash
git clone https://github.com/ChatterboxAI/docker-chatterbox.git
```

Build the `Docker` image in the directory that you have checked out.

```bash
docker build -t chatterbox .
```

Follow the instructions for running Chatterbox for Docker below to continue.

## Running Chatterbox for Docker

To prevent having to register your instance with home.chatterbox.ai every time the container is started, and to have persistent data, you can map a local directory into the container. Just replace the `directory_on_local_machine` with the path you want the container mapped to on your local machine \(eg. `/home/user/chatterbox`\).

Sounds can be played in the `Docker` container using `pulseaudio`, without modifying any config files

* Set [PULSE\_SERVER](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Network/#directconnection) `env` variable  
* Share pulseaudio's [cookie](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Network/#authorization)

Run the following to start up Chatterbox for Docker:

\_NOTE: You don't need the -e PULSE\_SERVER or any of the other pulse related variables if you only want to use text via a websocket to chatterbox for example using this container.

```bash
docker run -d  
-v directory_on_local_machine:/root/.chatterbox  
--device /dev/snd  
-e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native  
-v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native  
-v ~/.config/pulse/cookie:/root/.config/pulse/cookie  
-p 8181:8181  
--name chatterbox chatterboxai/docker-chatterbox
```

Confirm via `docker ps` that your container is up and serving port 8181:

```bash
docker ps  
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES  
692219e23bf2 chatterbox "/chatterbox/ai/mycro..." 3 seconds ago Up 1 second 0.0.0.0:8181->8181/tcp chatterbox
```

You should now have a running instance of Chatterbox for Docker that you can interact with via the command line.

### Pairing Chatterbox for Docker

After the container has been started you can watch the logs and look for the line that says "Pairing Code" and use this to pair at [https://home.chatterbox.ai](https://home.chatterbox.ai).

You can view the logs with:

```bash
docker logs -f chatterbox
```

## Interacting With Chatterbox on Docker

### Accessing Chatterbox Logs

At any time you can watch the logs simply by running the bellow command:

```bash
docker logs -f chatterbox
```

You can exit out of this `docker log` command by hitting Ctrl + C. The `--follow` turns it into a real `tail` instead of a `cat` of the log.

## CLI Access

### Accessing Chatterbox CLI

You can interact with the CLI of the container by running the following command. This will connect you to the running container via `bash`:

```bash
docker exec -it chatterbox /bin/bash
```

Once in the container you can do `./start-chatterbox.sh cli` to get a interactive CLI to interact with Chatterbox for Docker if needed.

You can type Ctrl + C to exit the cli.

### Installing Skills on Docker Chatterbox

You can install **Skills** into the container by running the following:

```bash
docker exec -it chatterbox /opt/chatterbox/msm/msm install github_url
```

So to install the Hello World Skill:

```bash
docker exec -it chatterbox /opt/chatterbox/msm/msm install https://github.com/ChatterboxAI/skill-hello-world
```

### Removing Skills on Docker Chatterbox

You can also uninstall a **Skill** using MSM with:

```bash
docker exec -it chatterbox /opt/chatterbox/msm/msm remove skill-hello-world
```

## Troubleshooting

### Text-to-speech not working

There have been reports that `mimic` may not be properly added to the PATH. Restarting Chatterbox within the Docker container can resolve this.

### Getting help

Chatterbox for Docker is community-supported. You are welcome to join the [Chatterbox Chat Docker channel](https://chat.chatterbox.ai/community/channels/docker).

