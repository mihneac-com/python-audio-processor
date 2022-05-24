# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:18:46 2022

@author: Mihnea
"""

import numpy as np
from scipy import signal

import matplotlib.pyplot as plt

class AudioConfig():
    def __init__(self):
        self.sampleRate = 48000
        self.dataType = 'float32'
        self.masterVolume = 1.0
        self.blockSize = 0
        
        self.fftColumns = 1024
        self.fftSize = self.fftColumns
        self.fftFreqs = np.fft.rfftfreq(self.fftSize, 1/self.sampleRate)
        
        self.actualBlockSize = 0
        
        self.eqBands = 10
        self.eqFreqs = [60, 170, 310, 600, 1000, 3000, 6000, 12000, 14000, 16000]
        self.eqGain = np.ones(self.eqBands, dtype=float)
        
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
   

af = AudioFilter(order=2, freq=60, ftype='lowpass')
af2 = AudioFilter(order=2, freq=(60,170))
af3 = AudioFilter(order=2, freq=(170,310))
### plotting

w, h = signal.sosfreqz(af.flt, worN=4000, fs=48000)
w, h2 = signal.sosfreqz(af2.flt, worN=4000, fs=48000)
w, h3 = signal.sosfreqz(af3.flt, worN=4000, fs=48000)

#bands = [60, 170, 310, 600, 1000, 3000, 6000, 12000, 14000, 16000]
bands = [(20, 39), (40,79), (80, 159), (160,299), (300,599), (600,1199), (1200, 2399), (2400,4999), (5000, 9999), (10000, 20000)]
flt = []
h = []
db = []

audio_cfg = AudioConfig()
audio_filters = []
# make filters
audio_filters.append(AudioFilter(order=3, freq=39, ftype='lowpass', fs=audio_cfg.sampleRate))
for i in range(1, audio_cfg.eqBands):
    # 1 ... 8 - shelving filters will be treated manually

    audio_filters.append(AudioFilter(order=3,
                                     freq=bands[i],
                                     fs=audio_cfg.sampleRate)
                         )
 
print(len(audio_filters))

w, h = signal.sosfreqz(audio_filters[0].flt, worN=4000, fs=48000)
summed_response = np.zeros_like(h)

plt.figure(1)
plt.clf()


for flt in audio_filters:
    w, h = signal.sosfreqz(flt.flt, worN=4000, fs=48000)
    summed_response = summed_response + h
    dbx = 20*np.log10(np.maximum(np.abs(h), 1e-5))
    plt.plot(w, dbx)

dbx = 20*np.log10(np.maximum(np.abs(summed_response), 1e-5))
plt.plot(w, dbx, label='sum')

plt.ylim(-60, 5)
plt.show()

# plt.figure(1)
# plt.clf()

# flt.append(AudioFilter(order=2, freq=60, ftype='lowpass'))
# w, h = signal.sosfreqz(af.flt, worN=4000, fs=48000)
# dbx = 20*np.log10(np.maximum(np.abs(h), 1e-5))
# db.append(dbx)
# plt.plot (w, db[0])

# for i in range (1, 10):
#     # 1 .. 9
#     flt.append(AudioFilter(order=3, freq=(bands[i-1], bands[i])))
#     w, h = signal.sosfreqz(flt[i].flt, worN=4000, fs=48000)
#     dbx = 20*np.log10(np.maximum(np.abs(h[i]), 1e-5))
    
    
#     plt.plot(w, dbx)

# db = 20*np.log10(np.maximum(np.abs(h), 1e-5))
# db2 = 20*np.log10(np.maximum(np.abs(h2), 1e-5))
# db3 = 20*np.log10(np.maximum(np.abs(h3), 1e-5))

# dbsum = 20*np.log10(np.maximum(np.abs(h3+h2+h), 1e-5))
