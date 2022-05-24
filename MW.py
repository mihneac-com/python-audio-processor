# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 807)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 181))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 471, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.outputDeviceSelector = QtWidgets.QComboBox(self.formLayoutWidget)
        self.outputDeviceSelector.setObjectName("outputDeviceSelector")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.outputDeviceSelector)
        self.inputDeviceSelector = QtWidgets.QComboBox(self.formLayoutWidget)
        self.inputDeviceSelector.setEnabled(True)
        self.inputDeviceSelector.setEditable(False)
        self.inputDeviceSelector.setObjectName("inputDeviceSelector")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputDeviceSelector)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(500, 20, 261, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startPlaybackBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.startPlaybackBtn.setFont(font)
        self.startPlaybackBtn.setFlat(False)
        self.startPlaybackBtn.setObjectName("startPlaybackBtn")
        self.horizontalLayout.addWidget(self.startPlaybackBtn)
        self.stopPlaybackBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopPlaybackBtn.setObjectName("stopPlaybackBtn")
        self.horizontalLayout.addWidget(self.stopPlaybackBtn)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 231, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.sampleRateSelector = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.sampleRateSelector.setObjectName("sampleRateSelector")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sampleRateSelector)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dataTypeSelector = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.dataTypeSelector.setObjectName("dataTypeSelector")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dataTypeSelector)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(500, 60, 261, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.audioStatusLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.audioStatusLabel.setFont(font)
        self.audioStatusLabel.setObjectName("audioStatusLabel")
        self.horizontalLayout_2.addWidget(self.audioStatusLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.CPUTimeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.CPUTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CPUTimeLabel.setObjectName("CPUTimeLabel")
        self.horizontalLayout_3.addWidget(self.CPUTimeLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.inputLatencyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.inputLatencyLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputLatencyLabel.setObjectName("inputLatencyLabel")
        self.horizontalLayout_4.addWidget(self.inputLatencyLabel)
        self.outputLatencyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.outputLatencyLabel.setObjectName("outputLatencyLabel")
        self.horizontalLayout_4.addWidget(self.outputLatencyLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.blockSizeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.blockSizeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.blockSizeLabel.setObjectName("blockSizeLabel")
        self.horizontalLayout_5.addWidget(self.blockSizeLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(250, 100, 231, 41))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.blockSizeSelector = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.blockSizeSelector.setObjectName("blockSizeSelector")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.blockSizeSelector)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 781, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.masterVolumeSlider = QtWidgets.QSlider(self.groupBox_2)
        self.masterVolumeSlider.setGeometry(QtCore.QRect(30, 40, 22, 121))
        self.masterVolumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.masterVolumeSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.masterVolumeSlider.setTickInterval(10)
        self.masterVolumeSlider.setObjectName("masterVolumeSlider")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 55, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.volumeSliderValue = QtWidgets.QLabel(self.groupBox_2)
        self.volumeSliderValue.setGeometry(QtCore.QRect(10, 170, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setKerning(True)
        self.volumeSliderValue.setFont(font)
        self.volumeSliderValue.setAlignment(QtCore.Qt.AlignCenter)
        self.volumeSliderValue.setObjectName("volumeSliderValue")
        self.fftGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.fftGroupBox.setGeometry(QtCore.QRect(10, 420, 781, 331))
        self.fftGroupBox.setObjectName("fftGroupBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sound Processing"))
        self.groupBox.setTitle(_translate("MainWindow", "Audio flow control"))
        self.label_2.setText(_translate("MainWindow", "Output device"))
        self.label.setText(_translate("MainWindow", "Input device"))
        self.startPlaybackBtn.setText(_translate("MainWindow", "Start playback"))
        self.stopPlaybackBtn.setText(_translate("MainWindow", "Stop"))
        self.label_4.setText(_translate("MainWindow", "Sample rate"))
        self.label_5.setText(_translate("MainWindow", "Data type"))
        self.label_3.setText(_translate("MainWindow", "Status:"))
        self.audioStatusLabel.setText(_translate("MainWindow", "STOPPED"))
        self.label_8.setText(_translate("MainWindow", "CPU Time:"))
        self.CPUTimeLabel.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "I/O latency [ms]:"))
        self.inputLatencyLabel.setText(_translate("MainWindow", "0"))
        self.outputLatencyLabel.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Block size"))
        self.blockSizeLabel.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Block size"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Signal processing"))
        self.label_6.setText(_translate("MainWindow", "Volume"))
        self.volumeSliderValue.setText(_translate("MainWindow", "1.00"))
        self.fftGroupBox.setTitle(_translate("MainWindow", "Signal Spectrum"))
