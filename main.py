from PyQt5 import QtCore, QtWidgets
#from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWidgets import QDialog
#from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer
#from pyqtgraph import PlotWidget, plot #unused
import pyqtgraph as pg
import sys
from events import WindowEvents
import MainApp as ma
from MainApp import MainApp
from MW import Ui_MainWindow
import numpy as np
import re


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, mainApp=None, events=None):
        self.mainApp = mainApp
        self.eventsHdlr = events
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.UiEvents()
        
        self.EQ_max_gain = 6
        
        self.fftGraph = pg.PlotWidget(self.fftGroupBox)
        self.fftGraph.setBackground('w')
        self.fftGraph.setGeometry(QtCore.QRect(10, 20, 761, 301))
        self.fftGraph.plotItem.setLogMode(x=True, y=False)
        self.fftGraph.setYRange(0, 200)
        self.fftGraph.setXRange(1.5, 4.2)
        self.fftPlotPen = pg.mkPen(color=(0,0,0))
        # setup ticks
        ticksValues = [ 20, 60, 100, 170, 310, 600, 1000, 3000, 6000, 12000, 20000 ]
        ticks = []
        for tick in ticksValues:
            if tick < 1000:
                txt = str(tick)
            else:
                txt = str(int(tick/1000)) + 'k'
            ticks.append((np.log10(tick), txt))
        
        self.fftXAxis = self.fftGraph.getPlotItem().getAxis('bottom')
        self.fftXAxis.setTicks([ticks])
        
        self.initUIContent()
        
        self.guiTimer = QTimer()
        self.guiTimer.timeout.connect(self.updateGUI)
        self.guiTimer.start(500)
        
        self.fftTimer = QTimer()
        self.fftTimer.timeout.connect(self.updateFFT)
    
    def UiEvents(self):
        #self.loadFileBtn.clicked.connect(self.loadFile)
        #return
        #self.inputDeviceDetailsBtn.clicked.connect(self.eventsHdlr.inputDeviceDialog)
        
        self.startPlaybackBtn.clicked.connect(self.startPlaybackEvent)
        self.stopPlaybackBtn.clicked.connect(self.stopPlaybackEvent)
        self.masterVolumeSlider.valueChanged.connect(self.updateVolume)
        self.EQ_resetButton.clicked.connect(self.resetEQ)
        self.EQ_Enable_btn.clicked.connect(self.enableEQ)
        self.EQ_LRTest_btn.clicked.connect(self.lrTestEQ)
        self.MonoBtn.clicked.connect(self.enableMono)
        
        for i in range(1, 11):
            getattr(self, 'EQ_slider' + str(i)).valueChanged.connect(self.updateEqSliders)
        
    
    def initUIContent(self):
        self.inputDeviceSelector.addItems(self.mainApp.inputDevicesList())
        #self.inputDeviceSelector.setEnabled(False)
        self.outputDeviceSelector.addItems(self.mainApp.outputDevicesList())
        #self.outputDeviceSelector.setEnabled(False)

        self.stopPlaybackBtn.setEnabled(False)
        
        self.sampleRateSelector.addItems(['48000', '44100', '16000', '8000'])
        self.dataTypeSelector.addItems(['float32', 'int32', 'int16'])
        self.blockSizeSelector.addItems(['0','128', '256', '512', '1024', '2048', '4096'])
        
        self.masterVolumeSlider.setValue(100)
        
        for i in range(1, 11):
            freq = ma.audio_cfg.eqFreqs[i-1]
            if freq >= 1000:
                ft = str(int(freq/1000)) + "k"
            else:
                ft = str(freq)
            getattr(self, "EQ_label" + str(i)).setText(ft)
            
        self.EQ_max_gain_label.setText("+" + str(int(20*np.log10(self.EQ_max_gain))) + " dB")
        
        

    def startPlaybackEvent(self):
        self.mainApp.updateConfigValue('sampleRate', int(self.sampleRateSelector.currentText()))
        self.mainApp.updateConfigValue('dataType', self.dataTypeSelector.currentText())
        self.mainApp.updateConfigValue('blockSize', int(self.blockSizeSelector.currentText()))
        
        self.mainApp.setInputDevice(self.inputDeviceSelector.currentText())
        self.mainApp.setOutputDevice(self.outputDeviceSelector.currentText())
        
        self.mainApp.startAudioPlayback()
        self.startPlaybackBtn.setEnabled(False)
        self.stopPlaybackBtn.setEnabled(True)
        # set status to on
        self.audioStatusLabel.setText("RUNNING")
        self.audioStatusLabel.setStyleSheet('color: green')
        
        self.enableInitControls(False)
        
        # fft plot
        self.fftGraph.plotItem.clear()
        ma.audio_cfg.computeFFTDetails()
        self.fftPlotLine = self.fftGraph.plot(ma.audio_cfg.fftFreqs,
                                              np.zeros_like(ma.audio_cfg.fftFreqs),
                                              pen=self.fftPlotPen
                                              )
        
        
        self.fftTimer.start(35)
        
    def closeEvent(self, event):
        self.stopPlaybackEvent()
    
    def stopPlaybackEvent(self):
        self.mainApp.stopAudioPlayback()
        self.startPlaybackBtn.setEnabled(True)
        self.stopPlaybackBtn.setEnabled(False)
        self.audioStatusLabel.setText("STOPPED")
        self.audioStatusLabel.setStyleSheet('color: black')
        
        self.enableInitControls()
        self.fftTimer.stop()
        
        self.fftGraph.plotItem.clear()
        self.fftPlotLine = self.fftGraph.plot(ma.audio_cfg.fftFreqs,
                                              np.zeros_like(ma.audio_cfg.fftFreqs),
                                              pen=self.fftPlotPen
                                              )
        
    def enableInitControls(self, enable=True):
        self.sampleRateSelector.setEnabled(enable)
        self.dataTypeSelector.setEnabled(enable)
        self.blockSizeSelector.setEnabled(enable)
        self.outputDeviceSelector.setEnabled(enable)
        self.inputDeviceSelector.setEnabled(enable)
        
    def updateVolume(self, event):
        vol = np.interp(event, np.arange(0,100), np.arange(0,1,0.01))
        #self.mainApp.c.masterVolume = vol
        self.mainApp.updateConfigValue('masterVolume', vol)
        self.volumeSliderValue.setText("{:.2f}".format(vol))
        
    def updateGUI(self):
        if self.mainApp.audio_stream != None and not self.mainApp.audio_stream.closed:
            self.CPUTimeLabel.setText("{:.2f} / {:.1f}".format(self.mainApp.audio_stream.cpu_load, self.mainApp.audio_stream.cpu_load * 100) + " %")
            lat = self.mainApp.audio_stream.latency
            #print(lat)
            self.inputLatencyLabel.setText("{:.1f}".format(lat[0]*1000))
            self.outputLatencyLabel.setText("{:.1f}".format(lat[1]*1000))
            self.blockSizeLabel.setText(str(ma.audio_cfg.actualBlockSize))
            
            
    def updateFFT(self):
        # get data from queue until empty
        data = np.array([])
        while not ma.audio_queue.empty():
            data = np.append(data, ma.audio_queue.get())
#        print(np.shape(data))
        if np.shape(data)[0] < 1024:
            return
        data_2 = data[0:1024]
        mag = np.abs(np.fft.rfft(data_2, n=ma.audio_cfg.fftSize))
        if ma.audio_cfg.dataType != 'float32':
            mag = mag / 32768.0
        #print(np.shape(mag))
        self.fftPlotLine.setData(ma.audio_cfg.fftFreqs, mag)
        
            
    def updateEqSliders(self, event):
        sender = self.sender()
        name = sender.objectName()
        # get slider number
        num = int(name.replace("EQ_slider", "")) - 1
        # scale gain
        lower_gain = np.linspace(0, 1, 51, endpoint=False)
        upper_gain = np.linspace(1, self.EQ_max_gain, 50)
        total_gain = np.append(lower_gain, upper_gain)
        val = np.interp(event, np.arange(-50,51), total_gain)
        ma.audio_cfg.eqGain[num] = val
        #print(num, '=>', val)
        #print(ma.audio_cfg.eqGain)
        
    def resetEQ(self):
        for i in range(1, 11):
            getattr(self, 'EQ_slider' + str(i)).setValue(0)
            
    def enableEQ(self, event :bool):
        ma.audio_cfg.eqEnabled = event
    def lrTestEQ(self, event :bool):
        ma.audio_cfg.eqLRTest = event
    def enableMono(self, event :bool):
        ma.audio_cfg.mono = event


def main():
    app = QApplication(sys.argv)
#    app.setStyle('Fusion')
    a = MainApp()
    wd = MainWindow(mainApp=a, events=WindowEvents)
    wd.show()
    
    app.exec_()

if __name__ == '__main__':
    main()