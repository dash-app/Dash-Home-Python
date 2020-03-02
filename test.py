#!/usr/bin/env python3

import numpy as np
from util import aeha
from sender import hexpi
from remote.light.hitachi.ir_a03h import remote

# TODO: delete here (move to controller)
entry = {
    "operation": True,
    "mode": "c", # full, nightlight, a, b, c, d
}
r = remote.generate(entry)

np.set_printoptions(formatter={'int': '0x{:02X}'.format})
print(r)
signal = aeha.toCode(430, r, 13300)
hexpi.send(signal)

#for i in r:
#    for j in i:
#        print("{:02X}, ".format(j), end="")
#    print("")

