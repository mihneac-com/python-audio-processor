# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:42:18 2022

@author: Mihnea

modul de procesare audio
"""

import sounddevice as sd
import numpy as np
assert np
import pprint
assert pprint
import time
from MainIODevices import MainIODevices

import multiprocessing as mp

sd.default.samplerate = 48000
sd.default.device = (2, 4)

            
class Config():
    def __init__(self):
        self.sampleRate = 48000
        self.dataType = 'float32'
        self.masterVolume = 1.00
# end class Config

class AudioProcessor(mp.Process):
    
    def __init__(self, q):
        super().__init__()
        self.sampleRate = 48000
        self.dataType = 'float32'
        self.mastervolume = 1
        
    def run(self):
        print("aaa", self.dataType)
        with sd.Stream(channels=2, callback=self.audio_callback, dtype=self.dataType, samplerate=self.sampleRate):
            while True:
                time.sleep(2)
                
    def audio_callback(self, indata, outdata, frames, time, status):
        outdata[:] = indata

## end class AudioProcessor

class MainApp(MainIODevices):
    
    def __init__(self):
        super().__init__()
        self.ipc_q = mp.Queue()
    
    def startAudioPlayback(self):
        self.p = AudioProcessor(self.ipc_q)
        self.p.start()

        
    def stopAudioPlayback(self):
        self.p.terminate()
        
    
    def updateVolume(self, vol):
        pass
    
# end class MainApp
            
if __name__ == '__main__':
    app = MainApp()
    app.getIODevices()

    