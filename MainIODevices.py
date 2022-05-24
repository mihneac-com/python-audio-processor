# -*- coding: utf-8 -*-
"""
Created on Sun May 22 22:27:19 2022

@author: Mihnea
"""
import sounddevice as sd

class MainIODevices():
    def __init__(self):
        self.inputDevices = []
        self.outputDevices = []
        self.hostAPIs = []
        self.getIODevices()
    
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
    