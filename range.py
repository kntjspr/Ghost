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


test = rndFloat(min=1, max=5, decimals=3, size=4)
print(test[0], test[1], test[2])
f = open("demofile2.txt", "a")
f.write(str(test))
f.close()
