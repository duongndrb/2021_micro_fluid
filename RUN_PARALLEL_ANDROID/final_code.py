# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_test_layout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QSizePolicy
#from get_firebase import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import sys
import serial
import time
import serial.tools.list_ports

dataPump1 = ""
dataPump2 = ""
dataPump3 = ""

data1 = ""
data2 = ""
data3 = ""

status_1 = ""
status_2 = ""
status_3 = ""
volume_1 = ""
volume_2 = ""
volume_3 = ""
target_1 = ""
target_2 = ""
target_3 = ""
flowrate_1 = ""
flowrate_2 = ""
flowrate_3 = ""
andr_dataP1 = ""
andr_dataP2 = ""
andr_dataP3 = ""

ser1 = serial.Serial('/dev/ttyUSB0',9600, timeout = 1)
ser2 = serial.Serial('/dev/ttyUSB1',9600, timeout = 1)
ser3 = serial.Serial('/dev/ttyUSB2',9600, timeout = 1)

def receive_from_mega(ser):
    if (ser.in_waiting > 0):
        cmd = ser.readline().decode('utf-8').rstrip()
        print(cmd)
        return(cmd)


class Arduino1(QThread):
    progress = pyqtSignal()

    def run(self):
            while True:
                self.progress.emit()
                time.sleep(1)

class Arduino2(QThread):
    progress = pyqtSignal()

    def run(self):
            while True:
                self.progress.emit()
                time.sleep(1)

class Arduino3(QThread):
    progress = pyqtSignal()

    def run(self):
            while True:
                self.progress.emit()
                time.sleep(1)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.power = QtWidgets.QPushButton(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(20, 450, 71, 71))
        self.power.setObjectName("power")
        self.runP1 = QtWidgets.QPushButton(self.centralwidget)
        self.runP1.setGeometry(QtCore.QRect(120, 450, 71, 71))
        self.runP1.setObjectName("runP1")
        self.pauseP1 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseP1.setGeometry(QtCore.QRect(210, 450, 71, 71))
        self.pauseP1.setObjectName("pauseP1")
        self.setP1 = QtWidgets.QPushButton(self.centralwidget)
        self.setP1.setGeometry(QtCore.QRect(300, 450, 71, 71))
        self.setP1.setObjectName("setP1")
        self.pauseP2 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseP2.setGeometry(QtCore.QRect(510, 450, 71, 71))
        self.pauseP2.setObjectName("pauseP2")
        self.setP2 = QtWidgets.QPushButton(self.centralwidget)
        self.setP2.setGeometry(QtCore.QRect(600, 450, 71, 71))
        self.setP2.setObjectName("setP2")
        self.runP2 = QtWidgets.QPushButton(self.centralwidget)
        self.runP2.setGeometry(QtCore.QRect(420, 450, 71, 71))
        self.runP2.setObjectName("runP2")
        self.pauseP3 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseP3.setGeometry(QtCore.QRect(820, 450, 71, 71))
        self.pauseP3.setObjectName("pauseP3")
        self.setP3 = QtWidgets.QPushButton(self.centralwidget)
        self.setP3.setGeometry(QtCore.QRect(910, 450, 71, 71))
        self.setP3.setObjectName("setP3")
        self.runP3 = QtWidgets.QPushButton(self.centralwidget)
        self.runP3.setGeometry(QtCore.QRect(730, 450, 71, 71))
        self.runP3.setObjectName("runP3")
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(20, 110, 81, 81))
        self.home.setObjectName("home")
        self.pump1 = QtWidgets.QLabel(self.centralwidget)
        self.pump1.setGeometry(QtCore.QRect(120, 120, 251, 71))
        self.pump1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pump1.setAlignment(QtCore.Qt.AlignCenter)
        self.pump1.setObjectName("pump1")
        self.pump2 = QtWidgets.QLabel(self.centralwidget)
        self.pump2.setGeometry(QtCore.QRect(420, 110, 251, 81))
        self.pump2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pump2.setAlignment(QtCore.Qt.AlignCenter)
        self.pump2.setObjectName("pump2")
        self.pump3 = QtWidgets.QLabel(self.centralwidget)
        self.pump3.setGeometry(QtCore.QRect(740, 110, 251, 81))
        self.pump3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pump3.setAlignment(QtCore.Qt.AlignCenter)
        self.pump3.setObjectName("pump3")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(950, 40, 61, 61))
        self.info.setObjectName("info")
        self.menu = QtWidgets.QLabel(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(300, 60, 431, 51))
        self.menu.setAlignment(QtCore.Qt.AlignCenter)
        self.menu.setObjectName("menu")
        self.namePump = QtWidgets.QLabel(self.centralwidget)
        self.namePump.setGeometry(QtCore.QRect(240, 0, 551, 61))
        self.namePump.setAlignment(QtCore.Qt.AlignCenter)
        self.namePump.setObjectName("namePump")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 10, 101, 81))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("8916abae7ffe8ea0d7ef.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.statusP1 = QtWidgets.QComboBox(self.centralwidget)
        self.statusP1.setGeometry(QtCore.QRect(120, 200, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.statusP1.setFont(font)
        self.statusP1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusP1.setAutoFillBackground(True)
        self.statusP1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.statusP1.setObjectName("statusP1")
        self.statusP1.addItem("")
        self.statusP1.addItem("")
        self.statusP1.addItem("")
        self.statusP1.addItem("")
        self.statusP2 = QtWidgets.QComboBox(self.centralwidget)
        self.statusP2.setGeometry(QtCore.QRect(420, 200, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.statusP2.setFont(font)
        self.statusP2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusP2.setAutoFillBackground(True)
        self.statusP2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.statusP2.setObjectName("statusP2")
        self.statusP2.addItem("")
        self.statusP2.addItem("")
        self.statusP2.addItem("")
        self.statusP2.addItem("")
        self.statusP3 = QtWidgets.QComboBox(self.centralwidget)
        self.statusP3.setGeometry(QtCore.QRect(730, 200, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.statusP3.setFont(font)
        self.statusP3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusP3.setAutoFillBackground(True)
        self.statusP3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.statusP3.setObjectName("statusP3")
        self.statusP3.addItem("")
        self.statusP3.addItem("")
        self.statusP3.addItem("")
        self.statusP3.addItem("")
        self.volumeP1 = QtWidgets.QComboBox(self.centralwidget)
        self.volumeP1.setGeometry(QtCore.QRect(120, 250, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeP1.sizePolicy().hasHeightForWidth())
        self.volumeP1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.volumeP1.setFont(font)
        self.volumeP1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.volumeP1.setAutoFillBackground(True)
        self.volumeP1.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.volumeP1.setObjectName("volumeP1")
        self.volumeP1.addItem("")
        self.volumeP1.addItem("")
        self.volumeP1.addItem("")
        self.volumeP1.addItem("")
        self.volumeP1.addItem("")
        self.volumeP1.addItem("")
        self.volumeP1.addItem("")
        self.volumeP1.addItem("")
        self.targetP1 = QtWidgets.QComboBox(self.centralwidget)
        self.targetP1.setGeometry(QtCore.QRect(120, 300, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.targetP1.setFont(font)
        self.targetP1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.targetP1.setObjectName("targetP1")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.targetP1.addItem("")
        self.flowRateP1 = QtWidgets.QComboBox(self.centralwidget)
        self.flowRateP1.setGeometry(QtCore.QRect(120, 350, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.flowRateP1.setFont(font)
        self.flowRateP1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.flowRateP1.setObjectName("flowRateP1")
        self.flowRateP1.addItem("")
        self.flowRateP1.addItem("")
        self.flowRateP1.addItem("")
        self.flowRateP1.addItem("")
        self.flowRateP1.addItem("")
        self.flowRateP1.addItem("")
        self.flowRateP1.addItem("")
        self.flowRateP1.addItem("")
        self.volumeP2 = QtWidgets.QComboBox(self.centralwidget)
        self.volumeP2.setGeometry(QtCore.QRect(420, 250, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeP2.sizePolicy().hasHeightForWidth())
        self.volumeP2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.volumeP2.setFont(font)
        self.volumeP2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.volumeP2.setAutoFillBackground(True)
        self.volumeP2.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.volumeP2.setObjectName("volumeP2")
        self.volumeP2.addItem("")
        self.volumeP2.addItem("")
        self.volumeP2.addItem("")
        self.volumeP2.addItem("")
        self.volumeP2.addItem("")
        self.volumeP2.addItem("")
        self.volumeP2.addItem("")
        self.volumeP2.addItem("")
        self.targetP2 = QtWidgets.QComboBox(self.centralwidget)
        self.targetP2.setGeometry(QtCore.QRect(420, 300, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.targetP2.setFont(font)
        self.targetP2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.targetP2.setObjectName("targetP2")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.targetP2.addItem("")
        self.flowRateP2 = QtWidgets.QComboBox(self.centralwidget)
        self.flowRateP2.setGeometry(QtCore.QRect(420, 350, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.flowRateP2.setFont(font)
        self.flowRateP2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.flowRateP2.setObjectName("flowRateP2")
        self.flowRateP2.addItem("")
        self.flowRateP2.addItem("")
        self.flowRateP2.addItem("")
        self.flowRateP2.addItem("")
        self.flowRateP2.addItem("")
        self.flowRateP2.addItem("")
        self.flowRateP2.addItem("")
        self.flowRateP2.addItem("")
        self.volumeP3 = QtWidgets.QComboBox(self.centralwidget)
        self.volumeP3.setGeometry(QtCore.QRect(730, 250, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeP3.sizePolicy().hasHeightForWidth())
        self.volumeP3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.volumeP3.setFont(font)
        self.volumeP3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.volumeP3.setAutoFillBackground(True)
        self.volumeP3.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.volumeP3.setObjectName("volumeP3")
        self.volumeP3.addItem("")
        self.volumeP3.addItem("")
        self.volumeP3.addItem("")
        self.volumeP3.addItem("")
        self.volumeP3.addItem("")
        self.volumeP3.addItem("")
        self.volumeP3.addItem("")
        self.volumeP3.addItem("")
        self.targetP3 = QtWidgets.QComboBox(self.centralwidget)
        self.targetP3.setGeometry(QtCore.QRect(730, 300, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.targetP3.setFont(font)
        self.targetP3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.targetP3.setObjectName("targetP3")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.targetP3.addItem("")
        self.flowRateP3 = QtWidgets.QComboBox(self.centralwidget)
        self.flowRateP3.setGeometry(QtCore.QRect(730, 350, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.flowRateP3.setFont(font)
        self.flowRateP3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.flowRateP3.setObjectName("flowRateP3")
        self.flowRateP3.addItem("")
        self.flowRateP3.addItem("")
        self.flowRateP3.addItem("")
        self.flowRateP3.addItem("")
        self.flowRateP3.addItem("")
        self.flowRateP3.addItem("")
        self.flowRateP3.addItem("")
        self.flowRateP3.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 200, 81, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.status = QtWidgets.QLabel(self.layoutWidget)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.volume = QtWidgets.QLabel(self.layoutWidget)
        self.volume.setObjectName("volume")
        self.verticalLayout.addWidget(self.volume)
        self.target = QtWidgets.QLabel(self.layoutWidget)
        self.target.setObjectName("target")
        self.verticalLayout.addWidget(self.target)
        self.flowRate = QtWidgets.QLabel(self.layoutWidget)
        self.flowRate.setObjectName("flowRate")
        self.verticalLayout.addWidget(self.flowRate)
        self.timeLeft = QtWidgets.QLabel(self.layoutWidget)
        self.timeLeft.setObjectName("timeLeft")
        self.verticalLayout.addWidget(self.timeLeft)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        global ser1
        global ser2
        global ser3

        self.pressed1_status = False
        self.pressed2_status = False
        self.pressed3_status = False 
        
        self.transmitAndroid1_status = False
        self.transmitAndroid2_status = False
        self.transmitAndroid3_status = False
        
        def listener1(event):
            if event.data != None:
                self.transmitAndroid1_status = True
                global andr_dataP1
                andr_dataP1 = event.data

        def listener2(event):
            if event.data != None:
                self.transmitAndroid2_status = True
                global andr_dataP2
                andr_dataP2 = event.data
    
        def listener3(event):
            if event.data != None:
                self.transmitAndroid3_status = True
                global andr_dataP3
                andr_dataP3 = event.data

        cred_obj = firebase_admin.credentials.Certificate('/home/pi/Downloads/microfluid/test_parellel/pi_stream_android/test-18cfb-firebase-adminsdk-717o7-9d907373d4.json')
        default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': 'https://test-18cfb-default-rtdb.firebaseio.com/'
        })
        ref1 = db.reference("/Pump1").listen(listener1)
        ref2 = db.reference("/Pump2").listen(listener2)
        ref3 = db.reference("/Pump3").listen(listener3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.setP1.clicked.connect(self.pressed_P1)
        self.setP2.clicked.connect(self.pressed_P2)
        self.setP3.clicked.connect(self.pressed_P3)
        self.pauseP1.clicked.connect(self.pressed_stop_P1)
        self.pauseP1.clicked.connect(self.pressed_stop_P2)
        self.pauseP1.clicked.connect(self.pressed_stop_P3)
        self.runP1.clicked.connect(self.pressed_run_P1)
        self.runP2.clicked.connect(self.pressed_run_P2)
        self.runP3.clicked.connect(self.pressed_run_P3)
        
        #khi nhan info
        self.info.clicked.connect(self.show_info)

        #create Thread
        self.arduino1_thread = Arduino1()
        self.arduino1_thread.progress.connect(self.arduino1_process)
        self.arduino2_thread = Arduino2()
        self.arduino2_thread.progress.connect(self.arduino2_process)
        self.arduino3_thread = Arduino3()
        self.arduino3_thread.progress.connect(self.arduino3_process)

        # Run Thread
        self.arduino1_thread.start()
        self.arduino2_thread.start()
        self.arduino3_thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.power.setText(_translate("MainWindow", "POWER"))
        self.runP1.setText(_translate("MainWindow", "RUN"))
        self.pauseP1.setText(_translate("MainWindow", "PAUSE"))
        self.setP1.setText(_translate("MainWindow", "SET"))
        self.pauseP2.setText(_translate("MainWindow", "PAUSE"))
        self.setP2.setText(_translate("MainWindow", "SET"))
        self.runP2.setText(_translate("MainWindow", "RUN"))
        self.pauseP3.setText(_translate("MainWindow", "PAUSE"))
        self.setP3.setText(_translate("MainWindow", "SET"))
        self.runP3.setText(_translate("MainWindow", "RUN"))
        self.home.setText(_translate("MainWindow", "HOME"))
        self.pump1.setText(_translate("MainWindow", "PUMP 1"))
        self.pump2.setText(_translate("MainWindow", "PUMP 2"))
        self.pump3.setText(_translate("MainWindow", "PUMP 3"))
        self.info.setText(_translate("MainWindow", "Info"))
        self.menu.setText(_translate("MainWindow", "MENU"))
        self.namePump.setText(_translate("MainWindow", "MICROFLUID PUMP "))
        self.statusP1.setItemText(0, _translate("MainWindow", "Infusion ONLY"))
        self.statusP1.setItemText(1, _translate("MainWindow", "Withdraw ONLY"))
        self.statusP1.setItemText(2, _translate("MainWindow", "Infusion/ Withdraw"))
        self.statusP1.setItemText(3, _translate("MainWindow", "Withdraw/Infusion"))
        self.statusP2.setItemText(0, _translate("MainWindow", "Infusion ONLY"))
        self.statusP2.setItemText(1, _translate("MainWindow", "Withdraw ONLY"))
        self.statusP2.setItemText(2, _translate("MainWindow", "Infusion/ Withdraw"))
        self.statusP2.setItemText(3, _translate("MainWindow", "Withdraw/Infusion"))
        self.statusP3.setItemText(0, _translate("MainWindow", "Infusion ONLY"))
        self.statusP3.setItemText(1, _translate("MainWindow", "Withdraw ONLY"))
        self.statusP3.setItemText(2, _translate("MainWindow", "Infusion/ Withdraw"))
        self.statusP3.setItemText(3, _translate("MainWindow", "Withdraw/Infusion"))
        self.volumeP1.setItemText(0, _translate("MainWindow", "1 ml"))
        self.volumeP1.setItemText(1, _translate("MainWindow", "3 ml"))
        self.volumeP1.setItemText(2, _translate("MainWindow", "5 ml"))
        self.volumeP1.setItemText(3, _translate("MainWindow", "10 ml"))
        self.volumeP1.setItemText(4, _translate("MainWindow", "20 ml"))
        self.volumeP1.setItemText(5, _translate("MainWindow", "50 ml"))
        self.volumeP1.setItemText(6, _translate("MainWindow", "200 μl"))
        self.volumeP1.setItemText(7, _translate("MainWindow", "500 μl"))
        self.targetP1.setItemText(0, _translate("MainWindow", "100 μl"))
        self.targetP1.setItemText(1, _translate("MainWindow", "200 μl"))
        self.targetP1.setItemText(2, _translate("MainWindow", "300 μl"))
        self.targetP1.setItemText(3, _translate("MainWindow", "400 μl"))
        self.targetP1.setItemText(4, _translate("MainWindow", "500 μl"))
        self.targetP1.setItemText(5, _translate("MainWindow", "600 μl"))
        self.targetP1.setItemText(6, _translate("MainWindow", "700 μl"))
        self.targetP1.setItemText(7, _translate("MainWindow", "800 μl"))
        self.targetP1.setItemText(8, _translate("MainWindow", "900 μl"))
        self.targetP1.setItemText(9, _translate("MainWindow", "1000 μl"))
        self.flowRateP1.setItemText(0, _translate("MainWindow", "10 μl/min"))
        self.flowRateP1.setItemText(1, _translate("MainWindow", "20 μl/min"))
        self.flowRateP1.setItemText(2, _translate("MainWindow", "50 μl/min"))
        self.flowRateP1.setItemText(3, _translate("MainWindow", "100 μl/min"))
        self.flowRateP1.setItemText(4, _translate("MainWindow", "200 μl/min"))
        self.flowRateP1.setItemText(5, _translate("MainWindow", "500 μl/min"))
        self.flowRateP1.setItemText(6, _translate("MainWindow", "1000 μl/min"))
        self.flowRateP1.setItemText(7, _translate("MainWindow", "1500 μl/min"))
        self.volumeP2.setItemText(0, _translate("MainWindow", "1 ml"))
        self.volumeP2.setItemText(1, _translate("MainWindow", "3 ml"))
        self.volumeP2.setItemText(2, _translate("MainWindow", "5 ml"))
        self.volumeP2.setItemText(3, _translate("MainWindow", "10 ml"))
        self.volumeP2.setItemText(4, _translate("MainWindow", "20 ml"))
        self.volumeP2.setItemText(5, _translate("MainWindow", "50 ml"))
        self.volumeP2.setItemText(6, _translate("MainWindow", "200 μl"))
        self.volumeP2.setItemText(7, _translate("MainWindow", "500 μl"))
        self.targetP2.setItemText(0, _translate("MainWindow", "100 μl"))
        self.targetP2.setItemText(1, _translate("MainWindow", "200 μl"))
        self.targetP2.setItemText(2, _translate("MainWindow", "300 μl"))
        self.targetP2.setItemText(3, _translate("MainWindow", "400 μl"))
        self.targetP2.setItemText(4, _translate("MainWindow", "500 μl"))
        self.targetP2.setItemText(5, _translate("MainWindow", "600 μl"))
        self.targetP2.setItemText(6, _translate("MainWindow", "700 μl"))
        self.targetP2.setItemText(7, _translate("MainWindow", "800 μl"))
        self.targetP2.setItemText(8, _translate("MainWindow", "900 μl"))
        self.targetP2.setItemText(9, _translate("MainWindow", "1000 μl"))
        self.flowRateP2.setItemText(0, _translate("MainWindow", "10 μl/min"))
        self.flowRateP2.setItemText(1, _translate("MainWindow", "20 μl/min"))
        self.flowRateP2.setItemText(2, _translate("MainWindow", "50 μl/min"))
        self.flowRateP2.setItemText(3, _translate("MainWindow", "100 μl/min"))
        self.flowRateP2.setItemText(4, _translate("MainWindow", "200 μl/min"))
        self.flowRateP2.setItemText(5, _translate("MainWindow", "500 μl/min"))
        self.flowRateP2.setItemText(6, _translate("MainWindow", "1000 μl/min"))
        self.flowRateP2.setItemText(7, _translate("MainWindow", "1500 μl/min"))
        self.volumeP3.setItemText(0, _translate("MainWindow", "1 ml"))
        self.volumeP3.setItemText(1, _translate("MainWindow", "3 ml"))
        self.volumeP3.setItemText(2, _translate("MainWindow", "5 ml"))
        self.volumeP3.setItemText(3, _translate("MainWindow", "10 ml"))
        self.volumeP3.setItemText(4, _translate("MainWindow", "20 ml"))
        self.volumeP3.setItemText(5, _translate("MainWindow", "50 ml"))
        self.volumeP3.setItemText(6, _translate("MainWindow", "200 μl"))
        self.volumeP3.setItemText(7, _translate("MainWindow", "500 μl"))
        self.targetP3.setItemText(0, _translate("MainWindow", "100 μl"))
        self.targetP3.setItemText(1, _translate("MainWindow", "200 μl"))
        self.targetP3.setItemText(2, _translate("MainWindow", "300 μl"))
        self.targetP3.setItemText(3, _translate("MainWindow", "400 μl"))
        self.targetP3.setItemText(4, _translate("MainWindow", "500 μl"))
        self.targetP3.setItemText(5, _translate("MainWindow", "600 μl"))
        self.targetP3.setItemText(6, _translate("MainWindow", "700 μl"))
        self.targetP3.setItemText(7, _translate("MainWindow", "800 μl"))
        self.targetP3.setItemText(8, _translate("MainWindow", "900 μl"))
        self.targetP3.setItemText(9, _translate("MainWindow", "1000 μl"))
        self.flowRateP3.setItemText(0, _translate("MainWindow", "10 μl/min"))
        self.flowRateP3.setItemText(1, _translate("MainWindow", "20 μl/min"))
        self.flowRateP3.setItemText(2, _translate("MainWindow", "50 μl/min"))
        self.flowRateP3.setItemText(3, _translate("MainWindow", "100 μl/min"))
        self.flowRateP3.setItemText(4, _translate("MainWindow", "200 μl/min"))
        self.flowRateP3.setItemText(5, _translate("MainWindow", "500 μl/min"))
        self.flowRateP3.setItemText(6, _translate("MainWindow", "1000 μl/min"))
        self.flowRateP3.setItemText(7, _translate("MainWindow", "1500 μl/min"))
        self.status.setText(_translate("MainWindow", "STATUS"))
        self.volume.setText(_translate("MainWindow", "Volume"))
        self.target.setText(_translate("MainWindow", "Target"))
        self.flowRate.setText(_translate("MainWindow", "Flow rate"))
        self.timeLeft.setText(_translate("MainWindow", "Time left"))
        
    def pressed_P1(self):
        self.pressed1_status = True

    def pressed_P2(self):
        self.pressed2_status = True

    def pressed_P3(self):
        self.pressed3_status = True
        
    def pressed_stop_P1(self):
        print("Pause Pump 1")
        #self.th.quit()
        self.arduino1_thread.quit()
        ser.write("q1".encode('utf-8'))
        
    def pressed_stop_P2(self):
        print("Pause Pump 2")
        #self.th.quit()
        self.arduino2_thread.quit()
        ser2.write("q2".encode('utf-8'))
    
    def pressed_stop_P3(self):
        print("Pause Pump 3")
        #self.th.quit()
        self.arduino3_thread.quit()
        ser3.write("q3".encode('utf-8'))
        
    def pressed_run_P1(self):
        print("RUN Pump 1")
        #self.th.quit()
        ser1.write("r1".encode('utf-8'))
    
    def pressed_run_P2(self):
        print("RUN Pump 2")
        #self.th.quit()
        ser2.write("r2".encode('utf-8'))
    
    def pressed_run_P3(self):
        print("RUN Pump 3")
        ser3.write("r3".encode('utf-8'))
        
    def show_info(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information of Microfluid Pump")
        msg.setText("This is the microfluid pump by MEMs-Lab, UET, VNU")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Close|QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("This is the first version of pump!")
        x = msg.exec_()

    def arduino1_process(self):
        if self.pressed1_status == True:
             #doc cac trang thai nhap tu man hinh sang String
            status1 = str(self.statusP1.currentText())
            volume1 = str(self.volumeP1.currentText())
            target1 = str(self.targetP1.currentText())
            flowrate1 = str(self.flowRateP1.currentText())
            #in ra man hinh
            print(" Status of Pump 1:",status1)
            print(" Volume of Pump 1:",volume1)
            print(" Target of Pump 1:",target1)
            print(" Flowrate of Pump 1:",flowrate1)
            #quy doi sang so cho de doc dinh dang
            global data1
            global status_1
            global volume_1
            global target_1
            global flowrate_1
            if status1 == "Infusion ONLY":
                    status_1 = "1"
            elif status1 == "Withdraw ONLY":
                    status_1 = "2"
            elif status1 == "Infusion/ Withdraw":
                    status_1 = "3"
            elif status1 == "Withdraw/Infusion":
                    status_1 = "4"
            else:
                    status_1 = "0"
            #chuyen kieu truyen di cua VOLUME
            if volume1 == "1 ml":
                    volume_1 = "1"
            elif volume1 == "3 ml":
                    volume_1 = "3"
            elif volume1 == "5 ml":
                    volume_1 = "5"
            elif volume1 == "10 ml":
                    volume_1 = "10"
            elif volume1 == "20 ml":
                    volume_1 = "20"
            elif volume1 == "50 ml" :
                    volume_1 = "50"
            else:
                    volume_1 = "0"
            
            #chuyen kieu du lieu truyen di cua Target
            if target1 == "100 μl":
                    target_1 = "100"
            elif target1 == "200 μl":
                    target_1 = "200"
            elif target1 == "300 μl":
                    target_1 = "300"
            elif target1 == "400 μl":
                    target_1 = "400"
            elif target1 == "500 μl":
                    target_1 = "500"
            elif target1 == "600 μl":
                    target_1 = "600"
            elif target1 == "700 μl":
                    target_1 = "700"
            elif target1 == "800 μl":
                    target_1 = "800"
            elif target1 == "900 μl":
                    target_1 = "900"
            elif target1 == "1000 μl":
                    target_1 = "1000"
            else:
                    target_1 = "0"
            
    #         status1 += "\n"
    #         volume1 += "\n"
    #         target1 += "\n"
            if flowrate1 == "10 μl/min":
                    flowrate_1 = "10"
            elif flowrate1 == "20 μl/min":
                    flowrate_1 = "20"
            elif flowrate1 == "50 μl/min":
                    flowrate_1 = "50"
            elif flowrate1 == "100 μl/min":
                    flowrate_1 = "100"
            elif flowrate1 == "200 μl/min":
                    flowrate_1 = "200"
            elif flowrate1 == "500 μl/min":
                    flowrate_1 = "500"
            elif flowrate1 == "1000 μl/min":
                    flowrate_1 = "1000"
            elif flowrate1 == "1500 μl/min":
                    flowrate_1 = "1500"
                    
            data1 = "1:" + status_1 + "_" + volume_1 + ":" + target_1 + "_" + flowrate_1 + "\n";
            print(data1)
            
            #self.th.start()
    #         ser.write("Pump 1: ".encode('utf-8'))
    #         ser.write(status1.encode('utf-8'))
    #         ser.write(volume1.encode('utf-8'))
    #         ser.write(target1.encode('utf-8'))
            ser1.write(data1.encode('utf-8'))
            self.pressed1_status = False
            
        if self.transmitAndroid1_status == True:
           global andr_dataP1
           print(andr_dataP1)
           dataFromAndroid1 = str(andr_dataP1)
           ser1.write(dataFromAndroid1.encode('utf-8'))
           time.sleep(5)
           ser1.write("r1".encode('utf-8'))
           print("RUN Pump 1")
           self.transmitAndroid1_status = False
            

        
    def arduino2_process(self):
        if self.pressed2_status == True:
            status2 = str(self.statusP2.currentText())
            volume2 = str(self.volumeP2.currentText())
            target2 = str(self.targetP2.currentText())
            flowrate2 = str(self.flowRateP2.currentText())
            
            print(" Status of Pump 2:",status2)
            print(" Volume of Pump 2:",volume2)
            print(" Target of Pump 2:",target2)
            print(" Flowrate of Pump 2:",flowrate2)
            
    #         status2 += "\n"
    #         volume2 += "\n"
    #         target2 += "\n"
            global data2
            global status_2
            global volume_2
            global target_2
            global flowrate_2
            #quy doi sang so cho de doc dinh dang
            if status2 == "Infusion ONLY":
                    status_2 = "1"
            elif status2 == "Withdraw ONLY":
                    status_2 = "2"
            elif status2 == "Infusion/ Withdraw":
                    status_2 = "3"
            elif status2 == "Withdraw/Infusion":
                    status_2 = "4"
            else:
                    status_2 = "0"
            #chuyen kieu truyen di cua VOLUME
            if volume2 == "1 ml":
                    volume_2 = "1"
            elif volume2 == "3 ml":
                    volume_2 = "3"
            elif volume2 == "5 ml":
                    volume_2 = "5"
            elif volume2 == "10 ml":
                    volume_2 = "10"
            elif volume2 == "20 ml":
                    volume_2 = "20"
            elif volume2 == "50 ml" :
                    volume_2 = "50"
            else:
                    volume_2 = "0"
            
            #chuyen kieu du lieu truyen di cua Target
            if target2 == "100 μl":
                    target_2 = "100"
            elif target2 == "200 μl":
                    target_2 = "200"
            elif target2 == "300 μl":
                    target_2 = "300"
            elif target2 == "400 μl":
                    target_2 = "400"
            elif target2 == "500 μl":
                    target_2 = "500"
            elif target2 == "600 μl":
                    target_2 = "600"
            elif target2 == "700 μl":
                    target_2 = "700"
            elif target2 == "800 μl":
                    target_2 = "800"
            elif target2 == "900 μl":
                    target_2 = "900"
            elif target2 == "1000 μl":
                    target_2 = "1000"
            else:
                    target_2 = "0"
            
            if flowrate2 == "10 μl/min":
                    flowrate_2 = "10"
            elif flowrate2 == "20 μl/min":
                    flowrate_2 = "20"
            elif flowrate2 == "50 μl/min":
                    flowrate_2 = "50"
            elif flowrate2 == "100 μl/min":
                    flowrate_2 = "100"
            elif flowrate2 == "200 μl/min":
                    flowrate_2 = "200"
            elif flowrate2 == "500 μl/min":
                    flowrate_2 = "500"
            elif flowrate2 == "1000 μl/min":
                    flowrate_2 = "1000"
            elif flowrate2 == "1500 μl/min":
                    flowrate_2 = "1500"
                    
            data2 = "2:" + status_2 + "_" + volume_2 + ":" + target_2 + "_" + flowrate_2 + "\n";
            print(data2);
            
            #self.th.start()
    #         ser.write("Pump 2: ".encode('utf-8'))
    #         ser.write(status2.encode('utf-8'))
    #         ser.write(volume2.encode('utf-8'))
    #         ser.write(target2.encode('utf-8'))
            
            ##self.arduino2_thread.start()
            
            ser2.write(data2.encode('utf-8'))
            self.pressed2_status = False
        if self.transmitAndroid2_status == True:
            global andr_dataP2
            print(andr_dataP2)
            dataFromAndroid2 = str(andr_dataP2)
            ser2.write(dataFromAndroid2.encode('utf-8'))
            time.sleep(5)
            ser2.write("r2".encode('utf-8'))
            print("RUN Pump 2")
            self.transmitAndroid2_status = False
            
        
    def arduino3_process(self):
        if self.pressed3_status == True:
            status3 = str(self.statusP3.currentText())
            volume3 = str(self.volumeP3.currentText())
            target3 = str(self.targetP3.currentText())
            flowrate3 = str(self.flowRateP3.currentText())
            
            print(" Status of Pump 3:",status3)
            print(" Volume of Pump 3:",volume3)
            print(" Target of Pump 3:",target3)
            print(" Flowrate of Pump 3:",flowrate3)
            
    #         status3 += "\n"
    #         volume3 += "\n"
    #         target3 += "\n"
            global data3
            global status_3
            global volume_3
            global target_3
            global flowrate_3
            #quy doi sang so cho de doc dinh dang
            if status3 == "Infusion ONLY":
                    status_3 = "1"
            elif status3 == "Withdraw ONLY":
                    status_3 = "2"
            elif status3 == "Infusion/ Withdraw":
                    status_3 = "3"
            elif status3 == "Withdraw/Infusion":
                    status_3 = "4"
            else:
                    status_3 = "0"
            #chuyen kieu truyen di cua VOLUME
            if volume3 == "1 ml":
                    volume_3 = "1"
            elif volume3 == "3 ml":
                    volume_3 = "3"
            elif volume3 == "5 ml":
                    volume_3 = "5"
            elif volume3 == "10 ml":
                    volume_3 = "10"
            elif volume3 == "20 ml":
                    volume_3 = "20"
            elif volume3 == "50 ml" :
                    volume_3 = "50"
            else:
                    volume_3 = "0"
            
            #chuyen kieu du lieu truyen di cua Target
            if target3 == "100 μl":
                    target_3 = "100"
            elif target3 == "200 μl":
                    target_3 = "200"
            elif target3 == "300 μl":
                    target_3 = "300"
            elif target3 == "400 μl":
                    target_3 = "400"
            elif target3 == "500 μl":
                    target_3 = "500"
            elif target3 == "600 μl":
                    target_3 = "600"
            elif target3 == "700 μl":
                    target_3 = "700"
            elif target3 == "800 μl":
                    target_3 = "800"
            elif target3 == "900 μl":
                    target_3 = "900"
            elif target3 == "1000 μl":
                    target_3 = "1000"
            
            if flowrate3 == "10 μl/min":
                    flowrate_3 = "10"
            elif flowrate3 == "20 μl/min":
                    flowrate_3 = "20"
            elif flowrate3 == "50 μl/min":
                    flowrate_3 = "50"
            elif flowrate3 == "100 μl/min":
                    flowrate_3 = "100"
            elif flowrate3 == "200 μl/min":
                    flowrate_3 = "200"
            elif flowrate3 == "500 μl/min":
                    flowrate_3 = "500"
            elif flowrate3 == "1000 μl/min":
                    flowrate_3 = "1000"
            elif flowrate3 == "1500 μl/min":
                    flowrate_3 = "1500"
            
            data3 = "3:" + status_3 + "_" + volume_3 + ":" + target_3 + "_" + flowrate_3 + "\n";
            print(data3)
            #self.th.start()
    #         ser.write("Pump 3: ".encode('utf-8'))
    #         ser.write(status3.encode('utf-8'))
    #         ser.write(volume3.encode('utf-8'))
    #         ser.write(target3.encode('utf-8'))
            
            
            ##self.arduino3_thread.start()
            ser3.write(data3.encode('utf-8'))
            self.pressed3_status = False
            
        if self.transmitAndroid3_status == True:
           global andr_dataP3
           print(andr_dataP3)
           dataFromAndroid3 = str(andr_dataP3)
           ser3.write(dataFromAndroid3.encode('utf-8'))
           time.sleep(5)
           ser3.write("r3".encode('utf-8'))
           print("RUN Pump 3")
           self.transmitAndroid3_status = False
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

