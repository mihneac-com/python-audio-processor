# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:36:45 2022

@author: Mihnea
"""

import pyaudio
import pprint 

p = pyaudio.PyAudio()

cnt = p.get_device_count()

for i in range(cnt):
    #print("Device " + str(i) + ":")
    d = p.get_device_info_by_index(i)
    pprint.pprint(d)
    print('-----------')