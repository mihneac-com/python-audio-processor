
from PyQt5.QtWidgets import QFileDialog
import os
from Dialogs import *
from MainApp import MainApp

class WindowEvents():
    
    def __init__(self):
        self.ma = MainApp()
    
    def loadFile(self):
        path, _ = QFileDialog.getOpenFileName(self, "Alegeti un fisier", '', 'All files (*.*)')
        if path != '':
            self.label_2.setText(path)
            self.sizeValueLabel.setEnabled(True)
            size = os.path.getsize(path) / 1000
            self.sizeValueLabel.setText(str(size) + " KB")
        else:
            # cancel was pressed; file not chosen
            self.label_2.setText("")
            self.sizeValueLabel.setEnabled(False)
            self.sizeValueLabel.setText("0")
            
    def inputDeviceDialog(self):
        dlg = deviceInfoDialog()
        dlg.setText(self.ma.getIODeviceDetail(kind="input"))
        dlg.exec()
        
        