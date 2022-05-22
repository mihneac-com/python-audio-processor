# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:42:18 2022

@author: Mihnea
"""

import sounddevice as sd
import numpy as np
import pprint
import time

import multiprocessing as mp

sd.default.samplerate = 48000
sd.default.device = (2, 4)
            
class Config():
    def __init__(self):
        self.sampleRate = 48000
        self.dataType = 'float32'
        self.masterVolume = 1.00


audio_queue = mp.Queue()
audio_parent_conn, audio_child_conn = mp.Pipe()
audio_cfg = Config()


def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata * audio_cfg.masterVolume
 #   print(np.sum(indata[0]))

def audio_process(audio_cfg, audio_data=None):
    print("Starting audio process with SR: ", audio_cfg.sampleRate)
    with sd.Stream(channels=2, callback=audio_callback, dtype=audio_cfg.dataType, samplerate=audio_cfg.sampleRate):
        while True:
            time.sleep(2)

p = mp.Process(target=audio_process, args=(audio_cfg,audio_child_conn))


class MainApp():
    def __init__(self):
        self.inputDevices = []
        self.outputDevices = []
        self.hostAPIs = []
        
        self.getIODevices()
        
        #self.c = Config()

        pass
    
    def getDefaultIODevs(self):
        return (2,4)
    
    def getIODevices(self):
        devs = sd.query_devices()
        self.hostAPIs = sd.query_hostapis()
        for device in devs:
            device['hostapi_text'] = self.hostAPIs[device['hostapi']]['name']
            if device['max_input_channels'] > 0 and device['max_output_channels'] == 0:
                self.inputDevices.append(device)
            else:
                self.outputDevices.append(device)
            
    def inputDevicesList(self):
        # arrange default items
        defDevicePos, _ = self.getDefaultIODevs()
        fullDevices = []
        fullDevices[:] = self.inputDevices
        fullDevices[0], fullDevices[defDevicePos] = fullDevices[defDevicePos], fullDevices[0]
        devs = []
        for device in fullDevices:
            devs.append(device['name'] + " [" + device['hostapi_text'] + "]")
        return devs
    
    def outputDevicesList(self):
        # arrange default items
        _, defDevicePos = self.getDefaultIODevs()
        defDevicePos = defDevicePos - 3
        fullDevices = []
        fullDevices[:] = self.outputDevices
        fullDevices[0], fullDevices[defDevicePos] = fullDevices[defDevicePos], fullDevices[0]
        devs = []
        for device in fullDevices:
            devs.append(device['name'] + " [" + device['hostapi_text'] + "]")
        return devs
    
    def getIODeviceDetail(kind):
        return "INPUT"
    
    def startAudioPlayback(self):
        #self.q = mp.Queue()
        #self.p = mp.Process(target=audio_process, args=(audio_cfg,))
        #self.p.start()
        p.start()

        
    def stopAudioPlayback(self):
        #self.q.put('exit')
        #self.p.terminate()
        p.terminate()
        
    
    def updateConfig(self, key, value):
        setattr(audio_cfg, key, value)
        
    def getConfig(self, key):
        return getattr(audio_cfg, key)
    

            
if __name__ == '__main__':
    app = MainApp()
    app.getIODevices()
#    pprint.pprint(app.inputDevices)
#    lst = app.inputDevicesList()
#    pprint.pprint(lst)
    