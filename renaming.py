import os
from os.path import dirname, join

replaces = {"mycroft": "chatterbox", "Mycroft": "Chatterbox", "MYCROFT":
    "CHATTERBOX"}

for root, folders, files in os.walk(dirname(__file__)):
    for f in files:
        if not f.endswith(".md"):
            continue
        path = join(root, f)
        print(path)
        with open(path, "r") as _:
            original = _.read()
        for k, v in replaces.items():
            original = original.replace(k, v)
        with open(path, "w") as _:
            _.write(original)

