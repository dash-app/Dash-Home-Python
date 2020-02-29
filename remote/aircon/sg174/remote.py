#!/usr/bin/env python3

signal = [
    [0x23, 0xCB, 0x26, 0x01, 0x00],
    [0x23, 0xCB, 0x26, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00]
]

def generate(e):
    if e['operation']:
        signal[1][5] = 0x20

    if e['mode'] == "cool":
        signal[1][6] = 0x58
    elif e['mode'] == "dry":
        signal[1][6] = 0x51
    elif e['mode'] == "heat":
        signal[1][6] = 0x48
    elif e['mode'] == "fan":
        signal[1][6] = 0x38

    #signal[1][7] =
    t = int(e['temp']) - 16
    if e['temp'] % 1 == 0.5:
        t += 16
    signal[1][7] = t

    vv = 0x00
    if e['vertical_vane'] == "swing":
        vv = 0xF8
    else:
        vv = int(e['vertical_vane']) * 16

    signal[1][8] = vv

    hv = 0xC0
    if e['horizontal_vane'] == "swing":
        hv += 0xF8
    elif e['horizontal_vane'] != "auto":
        hv += 0x08 * int(e['horizontal_vane'])

    signal[1][9] = hv

    if e['fan'] == "silent":
        signal[1][9] += 0x05
    elif e['fan'] == "low":
        signal[1][9] += 0x01
    elif e['fan'] == "mid":
        signal[1][9] += 0x02
    elif e['fan'] == "high":
        signal[1][9] += 0x03
    elif e['fan'] == "long":
        signal[1][9] += 0x03
        signal[1][15] += 0x10

    signal[1][10] = 0x80

    #print("0x{:02X}".format(sum(signal[1])))
    signal[1][len(signal[1])-1] = sum(signal[1])

    return signal

