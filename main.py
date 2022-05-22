from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QFileDialog
import sys
from events import WindowEvents
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
        
        self.initUIContent()
    
    def UiEvents(self):
        #self.loadFileBtn.clicked.connect(self.loadFile)
        #return
        self.inputDeviceDetailsBtn.clicked.connect(self.eventsHdlr.inputDeviceDialog)
        
        self.startPlaybackBtn.clicked.connect(self.startPlaybackEvent)
        self.stopPlaybackBtn.clicked.connect(self.stopPlaybackEvent)
        self.masterVolumeSlider.valueChanged.connect(self.updateVolume)
        
    
    def initUIContent(self):
        self.inputDeviceSelector.addItems(self.mainApp.inputDevicesList())
        self.inputDeviceSelector.setEnabled(False)
        self.outputDeviceSelector.addItems(self.mainApp.outputDevicesList())
        self.outputDeviceSelector.setEnabled(False)

        self.stopPlaybackBtn.setEnabled(False)
        
        self.sampleRateSelector.addItems(['48000', '44100', '16000', '8000'])
        self.dataTypeSelector.addItems(['float32', 'int32', 'int16'])
        

    def startPlaybackEvent(self):
        self.mainApp.updateConfig('sampleRate', int(self.sampleRateSelector.currentText()))
        self.mainApp.updateConfig('dataType', self.dataTypeSelector.currentText())
        
        self.mainApp.startAudioPlayback()
        self.startPlaybackBtn.setEnabled(False)
        self.stopPlaybackBtn.setEnabled(True)
        # set status to on
        self.audioStatusLabel.setText("RUNNING")
        self.audioStatusLabel.setStyleSheet('color: green')
        
        self.enableInitControls(False)
        
    def closeEvent(self, event):
        self.stopPlaybackEvent()
    
    def stopPlaybackEvent(self):
        self.mainApp.stopAudioPlayback()
        self.startPlaybackBtn.setEnabled(True)
        self.stopPlaybackBtn.setEnabled(False)
        self.audioStatusLabel.setText("STOPPED")
        self.audioStatusLabel.setStyleSheet('color: black')
        
        self.enableInitControls()
        
    def enableInitControls(self, enable=True):
        self.sampleRateSelector.setEnabled(enable)
        self.dataTypeSelector.setEnabled(enable)
        
    def updateVolume(self, event):
        vol = np.interp(event, np.arange(0,100), np.arange(0,1,0.01))
        self.mainApp.updateConfig('masterVolume', vol)
        #print("sent vol: ", vol)


def main():
    app = QApplication(sys.argv)
#    app.setStyle('Fusion')
    a = MainApp()
    wd = MainWindow(mainApp=a, events=WindowEvents)
    wd.show()
    
    app.exec_()

if __name__ == '__main__':
    main()