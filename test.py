#!/usr/bin/env python3

import numpy as np
from remote.light.hitachi.ir_a03h import remote


# TODO: delete here (move to controller)
entry = {
    "operation": False,
    "mode": "a", # full, nightlight, a, b, c, d
}
r = remote.generate(entry)

np.set_printoptions(formatter={'int': '{:02x}'.format})
print(r)

#for i in r:
#    for j in i:
#        print("{:02X}, ".format(j), end="")
#    print("")
