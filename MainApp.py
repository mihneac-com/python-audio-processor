# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:42:18 2022

@author: Mihnea
"""

import sounddevice as sd
import numpy as np
import pprint
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


class AudioProcessor(mp.Process):
    
    def __init__(self):
        super().__init__()
        self.sampleRate = 48000
        self.dataType = 'float32'
        self.mastervolume = 1
        
    def run(self):
        with sd.Stream(channels=2, callback=self.audio_callback, dtype=self.dataType, samplerate=self.sampleRate):
            while True:
                time.sleep(2)
                
    def audio_callback(self, indata, outdata, frames, time, status):
        outdata[:] = indata

## end class




def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata
 #   print(np.sum(indata[0]))

def audio_process(audio_cfg):
    print("Starting audio process with SR: ", audio_cfg.sampleRate)
    with sd.Stream(channels=2, callback=audio_callback, dtype=audio_cfg.dataType, samplerate=audio_cfg.sampleRate):
        while True:
            time.sleep(2)

class MainApp(MainIODevices):
    
    def startAudioPlayback(self):
        #self.p = mp.Process(target=audio_process, args=(audio_cfg,))
        #self.p.start()
        self.p = AudioProcessor()
        #if p != None:
        #    p.terminate()
        self.p.start()

        
    def stopAudioPlayback(self):
        self.p.terminate()
        
    
    def updateConfig(self, key, value):
         #setattr(audio_cfg, key, value)
         pass

            
if __name__ == '__main__':
    app = MainApp()
    app.getIODevices()
#    pprint.pprint(app.inputDevices)
#    lst = app.inputDevicesList()
#    pprint.pprint(lst)
    