#!/usr/bin/env python3

from util import aeha
from sender import hexpi
from remote.light.hitachi.ir_a03h import remote

class Remote:
    remote = None

    def __init__(self, kind, vendor, model):
        if kind == "light" and vendor == "hitachi" and model == "ir-a03h":
            self.remote = remote


    def send(self, entry):
        hx = self.remote.generate(entry)
        signal = aeha.toCode(430, hx, 13300)
        hexpi.send(signal)
