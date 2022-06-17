import decimal
import random
from decimal import *

import numpy as np


def rndFloat(min, max, decimals, size, addchars=""):
    # Reference: https://stackoverflow.com/questions/2891790/how-to-pretty-print-a-numpy-array-without-scientific-notation-and-with-given-pre
    decimals = "{: 0." + str(decimals) + "f}"
    result = np.random.random(size) * (max - min) + min  # (math min-max formula)
    np.set_printoptions(formatter={"float": decimals.format}, suppress=True)
    if not addchars:
        return result
    else:
        result = [str(arr) + str(addchars) for arr in result]
        return result


def rndChoice(chars, size=1):
    return np.random.choice(chars, size=size, replace=True)
