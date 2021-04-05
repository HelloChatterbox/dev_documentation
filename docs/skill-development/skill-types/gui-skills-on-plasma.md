---
description: >-

---

# Chatterbox for Plasma

This is a general installation and user guide for Plasma Chatterbox on the [KDE Plasma Desktop platform](https://www.kde.org/plasma-desktop).

## Getting started

### Distribution packages

Check your Linux distribution for `chatterbox-core` and `plasma-chatterbox` packages.

### KDE Neon git unstable

_NOTE: KDE Neon only provides `plasma-chatterbox` packages for the [Git Unstable Edition](https://neon.kde.org/download). This installation method requires that `chatterbox-core` be installed in your home folder following the [guide here](https://chatterbox.ai/documentation/linux/)_.

``` sudo apt install plasma-chatterbox ```

## Chatterbox for Plasma installer

|Supported Distributions|
|---|
|Debian Testing|
|KDE Neon Xenial, Bionic|
|Kubuntu 17.10, 18.04|
|Fedora 27, 28|

Download The Latest Installer AppImage From: https://github.com/AIIX/chatterbox-installer/releases

_NOTE: This installer also provides support for installing `chatterbox-core` and `plasma-chatterbox` on Arm64 and ArmHF architecture._

### Chatterbox for Plasma installer scripts

Installation scripts are available at https://github.com/ChatterboxAI/installers

### Chatterbox for Plasma manual installation

_NOTE: This installation method requires `chatterbox-core` to be installed in your home folder following the [guide available here](https://chatterbox.ai/documentation/linux/).

```
git clone https://anongit.kde.org/plasma-chatterbox.git
cd plasma-chatterbox
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DKDE_INSTALL_LIBDIR=lib -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
sudo make install
sudo chmod +x /usr/share/plasma/plasmoids/org.kde.plasma.chatterboxplasmoid/contents/code/startservice.sh
sudo chmod +x /usr/share/plasma/plasmoids/org.kde.plasma.chatterboxplasmoid/contents/code/stopservice.sh
sudo chmod +x /usr/share/plasma/plasmoids/org.kde.plasma.chatterboxplasmoid/contents/code/pkgstartservice.sh
sudo chmod +x /usr/share/plasma/plasmoids/org.kde.plasma.chatterboxplasmoid/contents/code/pkgstopservice.sh

```

## The Chatterbox for Plasma interface

![Plasma Chatterbox Screenshot](https://chatterbox.ai/wp-content/uploads/2018/06/plasmoid-gs1.png)

## Troubleshooting Chatterbox for Plasma

### Debugging connection errors

Follow these steps to debug connection errors.

* First, check that your `chatterbox-core` location is correctly set in your Chatterbox for Plasma settings. By default, Chatterbox for Plasma searches for `chatterbox-core` in your `$HOME` path - ie. `/home/$USER/chatterbox-core`.
* Next, check if `chatterbox-core` is able to start manually using the `debug` console - `./start-chatterbox.sh debug`
* Next, check to see if your firewall is blocking incoming connections to the `chatterbox-core` websocket address. By default, `chatterbox-core` listens on port 8181.
* Next, check the `chatterbox-bus.log` file to see if there are any errors blocking your connection. [See here for more information on the location of log files on Linux](https://chatterbox.ai/documentation/troubleshooting/#linux).
* Next, check to see if the Chatterbox for Plasma start and stop scripts have 'execute' filesystem permissions. They are located at:

* `/usr/share/plasma/plasmoids/org.kde.plasma.chatterboxplasmoid/contents/code/startservice.sh` (start)
* `/usr/share/plasma/plasmoids/org.kde.plasma.chatterboxplasmoid/contents/code/stopservice.sh` (stop)

## The visual display

The Chatterbox for Plasma desktop `enclosure` provides Skill Authors with a visual display platform to showcase **Skill** results and data in the form of interactive visual cards that can be created by the Skill Authors using popular UI/UX technologies such as `html` and `QML`.

### HTML-based visual Skill generation

#### Wikipedia Skill HTML Example

First, create a `html` folder inside your **Skill** folder. Next, we map the path to the folder.

```{.XML}
class WikipediaSkill(ChatterboxSkill):
def __init__(self):
....
self.html_index = dirname(__file__) + '/html/' # Location where the html files will be generated
self.css_index = dirname(__file__) + '/html/wiki.css'# Location of your main.css file
```

Next, we create a `__genwebview()` function. This function is used to generate the `html` page within the **Skill**.

```
{.XML}
def __genwebview(self, sm, imagemain, title):
simg = imagemain # Image url received from wikipedia api
smry = sm.encode('utf-8') # Summary received from wikipedia api encoded to utf8
stitle = title.encode('utf-8') # Article title encoded to utf8
fname = self.html_index + stitle + 'wikiresult.html' # Path of html folder location + name of html file that will be generated
scss = self.css_index # Path of your main css file which you have manually created
f = open(fname,'w')
wrapper = """
<div id="imgPlace">
<h1><strong>{2}</strong></h1>
</div>
<div id="wikisummary">
<p id="paratext">{3}</p>

</div>
""".format(scss, simg,
stitle, smry) # The wrapper is where you define your basic html layout for the skill
and using the format function pass variables to the html that will be used at
the time of generation. Writing complex JS and CSS in the wrapper should be
avoided and should be placed in the HTML folder as external files. Example JS
inclusion would have a self.js_index which could be passed to  insidef.write(wrapper) f.close()
```

Next, we call the `__genwebview(self)` function from `handle_intent()`.

```
{.XML}
def handle_intent(self, message):
try:
....
sm = wiki.summary(results[0],sentences = 20); # Summary to be sent to
__genwebvie(self) func spage = wiki.page(title); # Article title to be sent to
__genwebvie(self) func imagemain = spage.images[1] # Page Image to be sent to
__genwebvie(self) func self.__genwebview(sm, imagemain, title) # Calling the function to generate the HTML page after data is
available
....
```

Next, we send the URL to the `enclosure` for handling via the `self_enclosure.ws.emit()` function.

```
{.XML}
# Requires import: from chatterbox.messagebus.message import Message
def handle_intent(self, message):
try:
....
self.__genwebview(sm, imagemain, title)
self.enclosure.ws.emit(Message("data", {'desktop': {'url': self.html_index + title + 'wikiresult.html'}})) # This function emits metadata and url of generated html over websockets to
the desktop clients. This can include extra meta data also apart from URL like for example weather data variables. This function can be called before or after self.speak(summary) depending on where you like to position your webview
self.speak(summary)
....
# Format for desktop enclosure: self.enclosure.emit(Message{“data”, {“desktop”: {‘ any’: ‘any data’}}))
```

#### CSS file

The CSS file should be manually generated by the Skill Author.

```
{.XML}
html, body { margin: 0; padding: 0 } # Important to include in your css to avoid whitespace borders

# CSS for your view should be responsive, Fixed sizes and non responsive layouts will break on different screen sizes.
```

## QML based visual Skill generation

### Wikipedia Skill QML Example

First, create a `qml` folder inside your **Skill** folder and then map the path to the folder.

```
{.XML}

class WikipediaSkill(ChatterboxSkill):
def __init__(self):
....
self.qml_index = dirname(__file__) + '/qml/' # Location where the qml files will be generated
```

Next, create a `__genvisualobjecttemplate()` function. This function is used to generate the QML visual object within the **Skill**.

```
{.XML}
def __genvisualobjecttemplate(self, sm, imagemain, title):
simg = imagemain # Image url received from wikipedia api
smry = sm.encode('utf-8') # Summary received from wikipedia api encoded to utf8
stitle = title.encode('utf-8') # Article title encoded to utf8
fname = self.visualobject_index + stitle + "Wikiresult.qml" # Path of QML folder location + name of QML file that will be generated
f = open(fname,'w')
wrapper = """import QtQuick 2.9 # All import libs and dependencies can be installed using the Requirements.sh file distributed with the skills
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

Rectangle {{ # As we are building the qml code write into the python function we need to use double brackets for all QML objects to escape characters
id: bgRect
width: 500; height: 100
color: "#222"

Rectangle {{
id: mainRect
anchors.fill: parent
color: "#222"

Image {{
id: mainTopImage
anchors.top: parent.top
source: "{0}"
height: parent.height
width: parent.width
}}
}}
}}""".format(simg)

""".format(scss, simg, stitle, smry)
f.write(wrapper) # The wrapper is where you define your basic QM layout for the skill
f.close()
```

Next, call the `__genvisualobjecttemplate(self)` function from the `handle_intent()` function.

```
{.XML}
def handle_intent(self, message):
try:
....
sm = wiki.summary(results[0],sentences = 20); #Summary to be sent to __genwebvie(self) func
spage = wiki.page(title); #Article title to be sent to __genwebvie(self) func
imagemain = spage.images[1] #Page Image to be sent to __genwebvie(self) func
self.__genbvisualobjecttemplate(sm, imagemain, title) # Calling the function to generate the QML page after data is available
....

```

Next, send the QML file location to the `enclosure` for handling via the `self_enclosure.ws.emit()` function.

```
{.XML}
#Requires import: from chatterbox.messagebus.message import Message

def handle_intent(self, message):
try:
....
self.enclosure.ws.emit(Message("visualObject", {'desktop': {'url': self.visualobject_index + title + 'Wikiresult.qml'}}))
# This function emits the visual object and qml location to the loader functiion in the chatterbox plasmoid. This function can be called before or after self.speak(summary) depending on where you like to position your qml visualobject
self.speak(summary)
....
```

## Chatterbox for Plasma native visual Skill

The Chatterbox for Plasma `enclosure` also provides Skill Authors the ability to natively implement visual design for their **Skill** by providing a simple Object to the plasmoid.

First, create a custom visual object, and emit it to the plasmoid.

```
def handle_intent(self, message):
....
self.enclosure.ws.emit(Message("yourCustomObjectName", {'desktop': {'Your Custom Data Objects'}}))
....
```

Once added to your **Skill**, you can reach out to the Chatterbox for Plasma maintainer to discuss the design and implementation of your **Skill**. The best way to do this is to join the [Desktop Channel on Chatterbox Chat](https://chat.chatterbox.ai/community/channels/desktop).
