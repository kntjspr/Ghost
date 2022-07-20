import random
import decimal
import numpy as np
from decimal import *


def rndFloat(min, max, decimals, size, addchars=''):
    # Reference: https://stackoverflow.com/questions/2891790/how-to-pretty-print-a-numpy-array-without-scientific-notation-and-with-given-pre
    # size = number of iterations, addchars = covert float to string and concatenate
    # formatter={'float': {: 0." + str(decimals) + "f}.format}
    decimals = "{: 0." + str(decimals) + "f}"
    # (math min-max formula neural network)
    result = np.random.random(size) * (max - min) + min
    np.set_printoptions(formatter={'float': decimals.format}, suppress=True)
    if not addchars:
        return (result)
    else:
        result = [str(arr) + str(addchars) for arr in result]
        return result


def rndChoice(choice, size=1, addchars=""):
    result = np.random.choice(choice, size=size, replace=True)
    if not addchars:
        return result
    else:
        result = [str(arr) + str(addchars) for arr in result]
        return result


def generate(i=1):
    choice_words = ["grey", "relax", "punishment", "fold", "draconian", "straight", "telephone", "tree", "available", "puncture", "minister", "distinct", "massive", "zoom", "enchanted", "paper", "tray", "brainy", "zealous", "filthy", "chilly", "hideous", "deranged", "vacuous", "bless", "zipper", "weather", "tired", "week", "destruction", "gaudy", "furry", "absent", "irritate", "cycle", "plan", "serious", "momentous", "account", "dizzy", "vessel", "wriggle", "fragile", "yak", "kindhearted", "mourn", "change", "market",
                    "weigh", "basin", "spotless", "monkey", "lucky", "wrap", "curve", "error", "jittery", "important", "lake", "act", "male", "poke", "ritzy", "thick", "downtown", "crown", "noisy", "spiky", "trip", "expand", "ticket", "graceful", "tub", "pocket", "share", "rough", "inexpensive", "unruly", "admire", "appreciate", "uninterested", "treat", "scared", "blind", "mice", "kiss", "spotty", "women", "base", "permissible", "accessible", "office", "babies", "ban", "engine", "heartbreaking", "measly", "exotic", "worthless", "daffy"]
    choice_RAM = [2, 4, 6, 8]
    choice_CPU = [2, 4, 8, 16, 32]
    choice_mediaDevices = [1, 2, 3, 4]
    generated_noiseAudioContext = rndFloat(
        min=1, max=8, decimals=12, size=i, addchars="e-8")
    generated_canvasNoise = rndFloat(min=0, max=1, decimals=8, size=i)
    generated_ram = rndChoice(choice_RAM, i)
    generated_lat = ""
    generated_lon = ""
    generated_getClientRectNoise = rndFloat(min=3, max=9, decimals=5, size=i)
    generated_cpu = rndChoice(choice_CPU, size=i)
    generated_audioIn = rndChoice(choice_mediaDevices, size=i)
    generated_audioOut = rndChoice(choice_mediaDevices, size=i)
    generated_videoIn = rndChoice(choice_mediaDevices, size=i)
    generated_profileName = rndChoice(
        choice_words, size=i, addchars=f"-{random.randint(1,99)}{random.randint(1,999)}{random.randint(1,99999)}")
    generated_webglNoise = rndFloat(min=2, max=20, decimals=3, size=i)


def main():
    print(generate(1))
    print("coming soon")


if __name__ == "__main__":
    main()
