from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
from events import WindowEvents
import MainApp as ma
from MainApp import MainApp
from MW import Ui_MainWindow
import numpy as np


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, mainApp=None, events=None):
        self.mainApp = mainApp
        self.eventsHdlr = events
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.UiEvents()
        
        self.fftGraph = pg.PlotWidget(self.fftGroupBox)
        self.fftGraph.setBackground('w')
        self.fftGraph.setGeometry(QtCore.QRect(10, 20, 761, 301))
        self.fftGraph.plotItem.setLogMode(x=None, y=None)
        self.fftGraph.setYRange(0, 100)
        self.fftPlotPen = pg.mkPen(color=(0,0,0))
        
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
        
        

    def startPlaybackEvent(self):
        self.mainApp.updateConfigValue('sampleRate', int(self.sampleRateSelector.currentText()))
        self.mainApp.updateConfigValue('dataType', self.dataTypeSelector.currentText())
        self.mainApp.updateConfigValue('blockSize', int(self.blockSizeSelector.currentText()))
        
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
        self.fftPlotLine = self.fftGraph.plot(ma.audio_cfg.fftFreqs, np.zeros_like(ma.audio_cfg.fftFreqs), pen=self.fftPlotPen)
        
        
        self.fftTimer.start(50)
        
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
            #self.blockSizeLabel.setText(str(self.mainApp.audio_stream()))
            
            
            
            #print("----")
            #val = ma.audio_queue.get()
            #print(val)
            #print(np.shape(val))
            #print("Size:", ma.audio_queue.qsize())
            
    def updateFFT(self):
        # get data from queue until empty
        data = []
        while not ma.audio_queue.empty():
            data.append(ma.audio_queue.get())
        avg = np.average(data, 0)
        self.fftPlotLine.setData(ma.audio_cfg.fftFreqs, avg)
            


def main():
    app = QApplication(sys.argv)
#    app.setStyle('Fusion')
    a = MainApp()
    wd = MainWindow(mainApp=a, events=WindowEvents)
    wd.show()
    
    app.exec_()

if __name__ == '__main__':
    main()