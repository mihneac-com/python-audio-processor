# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:05:26 2022

@author: Mihnea
"""

import sounddevice as sd
import numpy as np
assert np
import sys
assert sys

sd.default.samplerate = 48000
duration = 5.5  # seconds

# input None = default
sd.default.device = (2, 4)

print(sd.default.device)
print(sd.default.blocksize)

gain = 1;

#sys.exit()

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata * gain
 #   print(np.sum(indata[0]))

with sd.Stream(channels=2, callback=callback, dtype='float32'):
    #sd.sleep(int(duration * 1000))
    while(1):
        print("Commands:")
        print("q - quit")
        print("1 - gain = 1")
        print("2 - gain = 2")
        cmd = input("Enter command: ")
        if (cmd == "1"):
            gain = 1;
        elif cmd == "2":
            gain = 2;
        else:
            break;