# Documentation TODO

The objective of this file is to document the items flagged as @TODO as I go through the documentation so I come back to them and ensure they're resolved before the documentation is put live.


### About Chatterbox

- [ ] Release note - need to find a way to aggregate them from GitHub. This will need the GitHub API.
- [ ] Overview - put in a link to the Precise documentation when it is done.

### Your home.chatterbox.ai account

- [ ] Document where different settings are located - device vs Skills

### Updating 
- [ ] Add or update instructions on how to update each device

### Mark 1 Display
- [ ] Mark 1 - should the information on how to control the display for the Mark 1 Enclosure go under the Skills section instead?
- [ ] Mark 1 - how many characters can the Mark 1 display show before text has to scroll?
- [ ] Mark 1 - the mouth_display_png() optional parameters need to be checked - I've guess what each of them mean, but this needs to be checked.
- [ ] Mark 1 - the pieces about how to draw to the **Enclosure** - I think this needs an explanatory graphic.

### Picroft

- [ ] Picroft - how to keep updated - is burning a new disk image to SD card the best approach?

### Chatterbox for Linux

- [ ] Linux - should people be connecting headphones and microphones through USB or Bluetooth? Is there any difference or preference? Is this information the same as for Picroft?
- [ ] Linux - what are the other installation options for Chatterbox on Linux - there are the installers that @AIIX provided, and I think there's an `apt-get` package. Will need to clarify.
- [ ] Not sure what the easiest way is to keep Chatterbox for Linux updated - is it as simple as doing a `git pull` from the remote repo?
- [ ] What are the common issues with Chatterbox for Linux?

### Chatterbox for Android
- [ ] Registration code for Android - not sure how this works or how Android provides a Registration Code

### Padatious

- [ ] Why is having Intents independent of each other a benefit - what does this mean - need to explain it in a bit more detail

### Chatterbox Skills

- [ ] Need more documentation on `msm` - what it does, what commands are available, what **Skills** developers need to know about it.
- [ ] What are the common issues in **Skills** development - ie the common problems that Developers encounter - so we can address them.
- [ ] How are Skills developed for platforms like Alexa repurposed for Chatterbox?
- [ ] We need a guide or similar for `__init__.py` - that covers items like how to inherit from the `ChatterboxSkill` class, and the sorts of functions that are used. How are APIs used? What if your **Skill** needs to use another service?

### Chatterbox language support

- [ ] The introductory text is available in multiple languages - are there any key languages that I'm missing?
- [ ] If I find a STT engine in the language I want to support, what do I do with it? The documentation on the Languages wiki isn't clear how all the elements come together.

### Precise

NIL

### Adapt

- [ ] are there minimum requirements for installing Adapt - both software and hardware?

### Audio service

- [ ] what URI schemas are supported by the Playback **Skill**?
