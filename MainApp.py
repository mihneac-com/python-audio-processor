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
from scipy import signal



sd.default.samplerate = 48000
sd.default.device = (2, 4)

     
class AudioConfig():
    def __init__(self):
        self.sampleRate = 48000
        self.dataType = 'float32'
        self.masterVolume = 1.0
        self.blockSize = 0
        
        self.fftColumns = 20000
        self.fftSize = self.fftColumns
        self.fftFreqs = np.fft.rfftfreq(self.fftSize, 1/self.sampleRate)
        
        self.actualBlockSize = 0
        
        self.eqBands = 10
        self.eqFreqs = [60, 170, 310, 600, 1000, 3000, 6000, 12000, 14000, 16000]
        self.eqGain = np.ones(self.eqBands, dtype=float)
        self.eqEnabled = True
        self.eqLRTest = False
        
        self.mono = False
        
    def computeFFTDetails(self):
        self.fftSize = self.fftColumns
        self.fftFreqs = np.fft.rfftfreq(self.fftSize, 1/self.sampleRate)
        
    
class AudioFilter():
    def __init__(self, order=2, ftype='bandpass', freq=(None,None), fs=48000):
        self.flt = signal.butter(order, 
                                     freq,
                                     fs=fs,
                                     output='sos',
                                     btype=ftype
                                     )
        self.zi_l = signal.sosfilt_zi(self.flt)
        self.zi_r = signal.sosfilt_zi(self.flt)
        
    def compute(self, left, right, gain=1):
        left_flt, self.zi_l = signal.sosfilt(self.flt, left, zi=self.zi_l)
        right_flt, self.zi_r = signal.sosfilt(self.flt, right, zi=self.zi_r)
    
        left_flt = left_flt * gain
        right_flt = right_flt * gain
        
        return left_flt, right_flt
        
        
audio_cfg = AudioConfig()
audio_queue = queue.Queue()
audio_meta_queue = queue.Queue()

### bandpass filter test


audio_filters = []

#print(audio_filter_zi_l)
### end filter test
    

def audio_callback(indata, outdata, frames, time, status):
    left = indata[:,0] * audio_cfg.masterVolume
    right = indata[:,1] * audio_cfg.masterVolume
    
    out_l = np.zeros_like(left)
    out_r = np.zeros_like(right)
    
    #print(np.shape(indata), np.shape(outdata))
 
    #left_flt, right_flt = af.compute(left, right, audio_cfg.eqGain[0])
    if audio_cfg.eqEnabled == True:
        for i in range(0, len(audio_filters)):
            left_flt, right_flt = audio_filters[i].compute(left, right, audio_cfg.eqGain[i])
            out_l = out_l + left_flt
            out_r = out_r + right_flt
        if audio_cfg.eqLRTest == True:
            out_r = right
    else:
        out_l = left
        out_r = right
        
    outdata[:,0] = out_l
    outdata[:,1] = out_r
    
    mono = outdata[:,0] + outdata[:,1]
    mono = mono / 2
    
    if audio_cfg.mono == True:
        outdata[:, 0] = mono
        outdata[:, 1] = mono
#    mag = np.abs(np.fft.rfft(mono[:], n=audio_cfg.fftSize))
#    audio_queue.put(mag)
    audio_queue.put(mono)
    #print(np.shape(mono))
    if audio_cfg.actualBlockSize != frames:
        audio_cfg.actualBlockSize = frames
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
        global audio_filters
        audio_queue = None
        audio_queue = queue.Queue()
        audio_filters = []
        # make filters
        
        # check filters and sample rate compatibility
        flt_max = 0
        for fr in audio_cfg.eqFreqs:
            if fr < int(audio_cfg.sampleRate/2):
                flt_max += 1
        
        audio_cfg.eqBands = flt_max
        
        audio_filters.append(AudioFilter(order=3, freq=audio_cfg.eqFreqs[0], ftype='lowpass', fs=audio_cfg.sampleRate))
        for i in range(0, audio_cfg.eqBands-1):
            # 1 ... 8 - shelving filters will be treated manually
            low = audio_cfg.eqFreqs[i]
            high = audio_cfg.eqFreqs[i+1]
            audio_filters.append(AudioFilter(order=3,
                                             freq=(low,high),
                                             fs=audio_cfg.sampleRate)
                                 )
        #print(audio_filters)
        #print(len(audio_filters))
        
        if self.inDevice == None:
            self.inDevice = 2
        if self.outDevice == None:
            self.outDevice = 4
        
        self.audio_stream = sd.Stream(channels=2,
                                      callback=audio_callback,
                                      dtype=audio_cfg.dataType,
                                      samplerate=audio_cfg.sampleRate,
                                      device=(self.inDevice,self.outDevice),
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
        
        
        
    
# end class MainApp


if __name__ == '__main__':
    app = MainApp()
    app.getIODevices()
#    app.startAudioPlayback()
#    s = sd.Stream(channels=2, callback=audio_callback, dtype='float32', samplerate=48000, device=(2,4))
#    s.start()
#    time.sleep(60)
#    s.stop()
    