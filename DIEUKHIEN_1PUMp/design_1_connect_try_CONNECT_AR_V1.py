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

import sys
import serial
import time
import serial.tools.list_ports
# volumeP1 = 1;
# targetP1 = 100;
# volumeP2 = 1;
# targetP2 = 100;
# volumeP3 = 1;
# targetP3 = 100;
# 
# information_Pump_list = [str(volumeP1), str(targetP1), str(volumeP2), str(targetP2), str(volumeP3), str(targetP3)]
# send_string = ','.join(information_Pump_list)
# send_string += "\n"

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
def get_serial_port():
    ports = serial.tools.list_ports.comports()
    for i in ports:
        port = str(i).split('  ')[0]
        #print port
        if(port == "/dev/ttyACM0" or port == "/dev/ttyACM1" or port == "/dev/ttyUSB0"):
            return port
        
port = get_serial_port()
print(port)

ser = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
#ser = serial.Serial(port, 9600, timeout = 0.1)

##Get rid of garbage/incomplete data
ser.flush()


def receive_from_mega(ser):
    if (ser.in_waiting > 0):
        cmd = ser.readline().decode('utf-8').rstrip()
        print(cmd)
        return(cmd)
    
class Thread(object):
    global ser
    statistic = pyqtSignal(str)
    def run(self):
        while True:
            cmd = receive_from_mega(ser)
            if cmd == '0':
                self.statistic.emit("0")
                print('0')
            

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
        
        self.th = Thread()
        


        global ser
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
#         index1 = self.statusP1.findText("Infusion ONLY", QtCore.Qt.MatchFixedString)
#         self.statusP1.setCurrentIndex(index1)
#         index2 = self.statusP2.findText("Infusion ONLY", QtCore.Qt.MatchFixedString)
#         self.statusP2.setCurrentIndex(index2)
#         index3 = self.statusP3.findText("Infusion ONLY", QtCore.Qt.MatchFixedString)
#         self.statusP3.setCurrentIndex(index3)
       
        
        self.setP1.clicked.connect(self.pressed_P1)
        self.setP2.clicked.connect(self.pressed_P2)
        self.setP3.clicked.connect(self.pressed_P3)
        self.pauseP1.clicked.connect(self.pressed_stop_P1)
        self.pauseP1.clicked.connect(self.pressed_stop_P2)
        self.pauseP1.clicked.connect(self.pressed_stop_P3)
        self.runP1.clicked.connect(self.pressed_run_P1)
        self.runP2.clicked.connect(self.pressed_run_P2)
        self.runP3.clicked.connect(self.pressed_run_P3)
        self.power.clicked.connect(self.pressed_run_all)
        
        #khi nhan info
        self.info.clicked.connect(self.show_info)

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
        self.statusP1.setItemText(2, _translate("MainWindow", "Infusion/Withdraw"))
        self.statusP1.setItemText(3, _translate("MainWindow", "Withdraw/Infusion"))
        self.statusP2.setItemText(0, _translate("MainWindow", "Infusion ONLY"))
        self.statusP2.setItemText(1, _translate("MainWindow", "Withdraw ONLY"))
        self.statusP2.setItemText(2, _translate("MainWindow", "Infusion/Withdraw"))
        self.statusP2.setItemText(3, _translate("MainWindow", "Withdraw/Infusion"))
        self.statusP3.setItemText(0, _translate("MainWindow", "Infusion ONLY"))
        self.statusP3.setItemText(1, _translate("MainWindow", "Withdraw ONLY"))
        self.statusP3.setItemText(2, _translate("MainWindow", "Infusion/Withdraw"))
        self.statusP3.setItemText(3, _translate("MainWindow", "Withdraw/Infusion"))
        self.volumeP1.setItemText(0, _translate("MainWindow", "1 ml"))
        self.volumeP1.setItemText(1, _translate("MainWindow", "3 ml"))
        self.volumeP1.setItemText(2, _translate("MainWindow", "5 ml"))
        self.volumeP1.setItemText(3, _translate("MainWindow", "10 ml"))
        self.volumeP1.setItemText(4, _translate("MainWindow", "20 ml"))
        self.volumeP1.setItemText(5, _translate("MainWindow", "50 ml"))
        self.targetP1.setItemText(0, _translate("MainWindow", "100 ??l"))
        self.targetP1.setItemText(1, _translate("MainWindow", "200 ??l"))
        self.targetP1.setItemText(2, _translate("MainWindow", "300 ??l"))
        self.targetP1.setItemText(3, _translate("MainWindow", "400 ??l"))
        self.targetP1.setItemText(4, _translate("MainWindow", "500 ??l"))
        self.targetP1.setItemText(5, _translate("MainWindow", "600 ??l"))
        self.targetP1.setItemText(6, _translate("MainWindow", "700 ??l"))
        self.targetP1.setItemText(7, _translate("MainWindow", "800 ??l"))
        self.targetP1.setItemText(8, _translate("MainWindow", "900 ??l"))
        self.targetP1.setItemText(9, _translate("MainWindow", "1000 ??l"))
        self.volumeP2.setItemText(0, _translate("MainWindow", "1 ml"))
        self.volumeP2.setItemText(1, _translate("MainWindow", "3 ml"))
        self.volumeP2.setItemText(2, _translate("MainWindow", "5 ml"))
        self.volumeP2.setItemText(3, _translate("MainWindow", "10 ml"))
        self.volumeP2.setItemText(4, _translate("MainWindow", "20 ml"))
        self.volumeP2.setItemText(5, _translate("MainWindow", "50 ml"))
        self.targetP2.setItemText(0, _translate("MainWindow", "100 ??l"))
        self.targetP2.setItemText(1, _translate("MainWindow", "200 ??l"))
        self.targetP2.setItemText(2, _translate("MainWindow", "300 ??l"))
        self.targetP2.setItemText(3, _translate("MainWindow", "400 ??l"))
        self.targetP2.setItemText(4, _translate("MainWindow", "500 ??l"))
        self.targetP2.setItemText(5, _translate("MainWindow", "600 ??l"))
        self.targetP2.setItemText(6, _translate("MainWindow", "700 ??l"))
        self.targetP2.setItemText(7, _translate("MainWindow", "800 ??l"))
        self.targetP2.setItemText(8, _translate("MainWindow", "900 ??l"))
        self.targetP2.setItemText(9, _translate("MainWindow", "1000 ??l"))
        self.volumeP3.setItemText(0, _translate("MainWindow", "1 ml"))
        self.volumeP3.setItemText(1, _translate("MainWindow", "3 ml"))
        self.volumeP3.setItemText(2, _translate("MainWindow", "5 ml"))
        self.volumeP3.setItemText(3, _translate("MainWindow", "10 ml"))
        self.volumeP3.setItemText(4, _translate("MainWindow", "20 ml"))
        self.volumeP3.setItemText(5, _translate("MainWindow", "50 ml"))
        self.targetP3.setItemText(0, _translate("MainWindow", "100 ??l"))
        self.targetP3.setItemText(1, _translate("MainWindow", "200 ??l"))
        self.targetP3.setItemText(2, _translate("MainWindow", "300 ??l"))
        self.targetP3.setItemText(3, _translate("MainWindow", "400 ??l"))
        self.targetP3.setItemText(4, _translate("MainWindow", "500 ??l"))
        self.targetP3.setItemText(5, _translate("MainWindow", "600 ??l"))
        self.targetP3.setItemText(6, _translate("MainWindow", "700 ??l"))
        self.targetP3.setItemText(7, _translate("MainWindow", "800 ??l"))
        self.targetP3.setItemText(8, _translate("MainWindow", "900 ??l"))
        self.targetP3.setItemText(9, _translate("MainWindow", "1000 ??l"))
        self.status.setText(_translate("MainWindow", "STATUS"))
        self.volume.setText(_translate("MainWindow", "Volume"))
        self.target.setText(_translate("MainWindow", "Target"))
        self.flowRate.setText(_translate("MainWindow", "Flow rate"))
        self.timeLeft.setText(_translate("MainWindow", "Time left"))
        
    #@pyqtSlot()
    def pressed_P1(self):
        #doc cac trang thai nhap tu man hinh sang String
        status1 = str(self.statusP1.currentText())
        volume1 = str(self.volumeP1.currentText())
        target1 = str(self.targetP1.currentText())
        #in ra man hinh
        print(" Status of Pump 1:",status1)
        print(" Volume of Pump 1:",volume1)
        print(" Target of Pump 1:",target1)
        #quy doi sang so cho de doc dinh dang
        global data1
        global status_1
        global volume_1
        global target_1
        if status1 == "Infusion ONLY":
                status_1 = "1"
        elif status1 == "Withdraw ONLY":
                status_1 = "2"
        elif status1 == "Infusion/Withdraw":
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
        if target1 == "100 ??l":
                target_1 = "100"
        elif target1 == "200 ??l":
                target_1 = "200"
        elif target1 == "300 ??l":
                target_1 = "300"
        elif target1 == "400 ??l":
                target_1 = "400"
        elif target1 == "500 ??l":
                target_1 = "500"
        elif target1 == "600 ??l":
                target_1 = "600"
        elif target1 == "700 ??l":
                target_1 = "700"
        elif target1 == "800 ??l":
                target_1 = "800"
        elif target1 == "900 ??l":
                target_1 = "900"
        elif target1 == "1000 ??l":
                target_1 = "1000"
        else:
                target_1 = "0"
        
#         status1 += "\n"
#         volume1 += "\n"
#         target1 += "\n"
        
        data1 = "1_" + status_1 + "_" + volume_1 + "_" + target_1 + "\n";
        print(data1);
        
        #self.th.start()
#         ser.write("Pump 1: ".encode('utf-8'))
#         ser.write(status1.encode('utf-8'))
#         ser.write(volume1.encode('utf-8'))
#         ser.write(target1.encode('utf-8'))
        
        ser.write(data1.encode('utf-8'))
        
    def pressed_P2(self):
        status2 = str(self.statusP2.currentText())
        volume2 = str(self.volumeP2.currentText())
        target2 = str(self.targetP2.currentText())
        
        print(" Status of Pump 2:",status2)
        print(" Volume of Pump 2:",volume2)
        print(" Target of Pump 2:",target2)
        
#         status2 += "\n"
#         volume2 += "\n"
#         target2 += "\n"
        global data2
        global status_2
        global volume_2
        global target_2
        #quy doi sang so cho de doc dinh dang
        if status2 == "Infusion ONLY":
                status_2 = "1"
        elif status2 == "Withdraw ONLY":
                status_2 = "2"
        elif status2 == "Infusion/Withdraw":
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
        if target2 == "100 ??l":
                target_2 = "100"
        elif target2 == "200 ??l":
                target_2 = "200"
        elif target2 == "300 ??l":
                target_2 = "300"
        elif target2 == "400 ??l":
                target_2 = "400"
        elif target2 == "500 ??l":
                target_2 = "500"
        elif target2 == "600 ??l":
                target_2 = "600"
        elif target2 == "700 ??l":
                target_2 = "700"
        elif target2 == "800 ??l":
                target_2 = "800"
        elif target2 == "900 ??l":
                target_2 = "900"
        elif target2 == "1000 ??l":
                target_2 = "1000"
        else:
                target_2 = "0"
        
                
        data2 = "2_" + status_2 + "_" + volume_2 + "_" + target_2 + "\n";
        print(data2)
        #self.th.start()
#         ser.write("Pump 2: ".encode('utf-8'))
#         ser.write(status2.encode('utf-8'))
#         ser.write(volume2.encode('utf-8'))
#         ser.write(target2.encode('utf-8'))
        
        ser.write(data2.encode('utf-8'))

    def pressed_P3(self):
        status3 = str(self.statusP3.currentText())
        volume3 = str(self.volumeP3.currentText())
        target3 = str(self.targetP3.currentText())
        
        print(" Status of Pump 3:",status3)
        print(" Volume of Pump 3:",volume3)
        print(" Target of Pump 3:",target3)
        
#         status3 += "\n"
#         volume3 += "\n"
#         target3 += "\n"
        global data3
        global status_3
        global volume_3
        global target_3
        #quy doi sang so cho de doc dinh dang
        if status3 == "Infusion ONLY":
                status_3 = "1"
        elif status3 == "Withdraw ONLY":
                status_3 = "2"
        elif status3 == "Infusion/Withdraw":
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
        if target3 == "100 ??l":
                target_3 = "100"
        elif target3 == "200 ??l":
                target_3 = "200"
        elif target3 == "300 ??l":
                target_3 = "300"
        elif target3 == "400 ??l":
                target_3 = "400"
        elif target3 == "500 ??l":
                target_3 = "500"
        elif target3 == "600 ??l":
                target_3 = "600"
        elif target3 == "700 ??l":
                target_3 = "700"
        elif target3 == "800 ??l":
                target_3 = "800"
        elif target3 == "900 ??l":
                target_3 = "900"
        elif target3 == "1000 ??l":
                target_3 = "1000"
        
        data3 = "3_" + status_3 + "_" + volume_3 + "_" + target_3 + "\n";
        print(data3)
        #self.th.start()
#         ser.write("Pump 3: ".encode('utf-8'))
#         ser.write(status3.encode('utf-8'))
#         ser.write(volume3.encode('utf-8'))
#         ser.write(target3.encode('utf-8'))
        
        ser.write(data3.encode('utf-8'))
        
    def pressed_stop_P1(self):
        print("Pause Pump 1")
        #self.th.quit()
        ser.write("q1".encode('utf-8'))
        
    def pressed_stop_P2(self):
        print("Pause Pump 2")
        #self.th.quit()
        ser.write("q2".encode('utf-8'))
    
    def pressed_stop_P3(self):
        print("Pause Pump 3")
        #self.th.quit()
        ser.write("q3".encode('utf-8'))
        
    def pressed_run_P1(self):
        print("RUN Pump 1")
        #self.th.quit()
        ser.write("r1".encode('utf-8'))
    
    def pressed_run_P2(self):
        print("RUN Pump 2")
        #self.th.quit()
        ser.write("r2".encode('utf-8'))
    
    def pressed_run_P3(self):
        print("RUN Pump 3")
        ser.write("r3".encode('utf-8'))
    
    def pressed_run_all(self):
        print("RUN ALL PUMP")
        ser.write("rA".encode('utf-8'))
        
    def show_info(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information of Microfluid Pump")
        msg.setText("This is the microfluid pump by MEMs-Lab, UET, VNU")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Close|QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("This is the first version of pump!")
        x = msg.exec_()


if __name__ == "__main__":
    #import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    
    
    #Infinite loop
#     while True:
#         value_pump_list = [ui.self.pressed_p1(status1)]
#         send_string = ','.join(value_pump_list)
#         send_string += "\n"
#         
#         ser.write(send_string.encode('utf-8'))
#         receive_string = ser.readline().decode('utf-8','replace').rstrip()
#         
#         print(receive_string)        
# #     
    #end
    sys.exit(app.exec_())



