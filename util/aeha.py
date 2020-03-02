#!/usr/bin/python3

def toCode(T, byte, interval):
    code = []
    i = 0
    # byte[ 0, 1, 2 ]
    for i in range(len(byte)):
        c = byte[i]
        code.extend((int(T*8), int(T*4)))

        # byte[ 0:[0, 1, ....] ]
        for j in range(len(c)):
            for k in range(8):
                #code.append(int(T))
                if (c[j] & (1 << k)) != 0:
                    code.extend((int(T), int(T*3)))
                    #code.append(int(T*3))

                else:
                    code.extend((int(T), int(T)))
                    #code.append(int(T))

        code.append(int(T))

        if i < len(byte) - 1:
            code.append(int(interval))

    return code
