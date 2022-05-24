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
#import time
import queue
from MainIODevices import MainIODevices



sd.default.samplerate = 48000
sd.default.device = (2, 4)

     
class AudioConfig():
    def __init__(self):
        self.sampleRate = 48000
        self.dataType = 'float32'
        self.masterVolume = 1.0
        self.blockSize = 0
        
        self.fftColumns = 1024
        
        self.computeFFTDetails()
    
    def computeFFTDetails(self):
        #low = 0
        #high = np.clip(int(self.sampleRate/2), None, 20000)
        #high = int(self.sampleRate/2)
        #self.fftRange = (low, high)
        #delta_f = (high - low) / (self.fftColumns - 1)
        #self.fftFreqs = np.arange(low, high+1, delta_f )
        #self.fftSize = int(np.ceil(self.sampleRate / delta_f))
        
        self.fftSize = self.fftColumns
        self.fftFreqs = np.fft.rfftfreq(self.fftSize, 1/self.sampleRate)
        
        #print("FFT Range:", self.fftRange)
#        print("FFT Size:", self.fftSize)
#        print("FFT Columns:", self.fftFreqs)
    
        

        
audio_cfg = AudioConfig()
audio_queue = queue.Queue()
audio_meta_queue = queue.Queue()

def audio_callback(indata, outdata, frames, time, status):
    outdata[:] = indata * audio_cfg.masterVolume
    mono = outdata[:,0] + outdata[:,1]
    mag = np.abs(np.fft.rfft(mono[:], n=audio_cfg.fftSize))
    audio_queue.put(mag)
    #audio_meta_queue.put((frames, time, status))

class MainApp(MainIODevices):
    
    def __init__(self):
        super().__init__()
        sd.default.samplerate = 48000
        sd.default.device = (2, 4)
        self.audio_stream = None
        
        #self.c = AudioConfig()

    
    def startAudioPlayback(self):
        global audio_callback
        global audio_cfg
        global audio_queue
        audio_queue = None
        audio_queue = queue.Queue()
        self.audio_stream = sd.Stream(channels=2,
                                      callback=audio_callback,
                                      dtype=audio_cfg.dataType,
                                      samplerate=audio_cfg.sampleRate,
                                      device=(2,4),
                                      blocksize=audio_cfg.blockSize)
        self.audio_stream.start()
      
 
    def stopAudioPlayback(self):
        global audio_queue
        if self.audio_stream != None:
            self.audio_stream.close()
        self.audio_stream = None
        audio_queue = None
        
    def updateVolume(self, vol):
        pass
    
    def updateConfigValue(self, key, val):
        setattr(audio_cfg, key, val)
        
    def getConfigValue(self, key):
        getattr(audio_cfg, key)
        
        
    def computeFFT(self):
        pass
        
    
# end class MainApp


if __name__ == '__main__':
    app = MainApp()
    app.getIODevices()
#    app.startAudioPlayback()
#    s = sd.Stream(channels=2, callback=audio_callback, dtype='float32', samplerate=48000, device=(2,4))
#    s.start()
#    time.sleep(60)
#    s.stop()
    