# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Desktop\HotelManagementSystem\src\main\resources\base\room.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Room(object):
    def setupUi(self, Room):
        Room.setObjectName("Room")
        Room.resize(800, 377)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rm/48px-Go-home-2.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Room.setWindowIcon(icon)
        self.gridLayout_4 = QtWidgets.QGridLayout(Room)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Room)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setObjectName("tableView")
        self.gridLayout_5.addWidget(self.tableView, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Res/48px-Appointment.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableView_2 = QtWidgets.QTableView(self.tab_2)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout_6.addWidget(self.tableView_2, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Res/48px-Appointment-archive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Room)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/commands/48px-Ambox_emblem_plus.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/commands/48px-Edit-find-replace.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/commands/48px-Edit-delete.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 10, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 7, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Room)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Room)

    def retranslateUi(self, Room):
        _translate = QtCore.QCoreApplication.translate
        Room.setWindowTitle(_translate("Room", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Room", "Current Reservations"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Room", "Archived Reservations"))
        self.groupBox.setTitle(_translate("Room", "Information"))
        self.groupBox_2.setTitle(_translate("Room", "Commands"))
        self.pushButton_3.setText(_translate("Room", "Add"))
        self.pushButton_2.setText(_translate("Room", "Edit"))
        self.pushButton.setText(_translate("Room", "Delete"))
        self.label.setText(_translate("Room", "Room Number:"))
        self.spinBox.setPrefix(_translate("Room", "$"))
        self.label_3.setText(_translate("Room", "Room Type:"))
        self.label_2.setText(_translate("Room", "Price"))
        self.lineEdit.setPlaceholderText(_translate("Room", "Enter a Room number and press Enter"))
        self.comboBox.setItemText(0, _translate("Room", "Single"))
        self.comboBox.setItemText(1, _translate("Room", "Double"))
        self.comboBox.setItemText(2, _translate("Room", "Triple"))
        self.comboBox.setItemText(3, _translate("Room", "Quad"))
        self.comboBox.setItemText(4, _translate("Room", "Queen"))
        self.comboBox.setItemText(5, _translate("Room", "King"))
        self.comboBox.setItemText(6, _translate("Room", "Twin"))
        self.comboBox.setItemText(7, _translate("Room", "Hollywood Twin"))
        self.comboBox.setItemText(8, _translate("Room", "Double-Double"))
        self.comboBox.setItemText(9, _translate("Room", "Studio"))
        self.comboBox.setItemText(10, _translate("Room", "Suite / Executive Suite"))
        self.comboBox.setItemText(11, _translate("Room", "Mini Suite / Junior Suite"))
        self.comboBox.setItemText(12, _translate("Room", "President Suite / Presidential Suite"))
        self.comboBox.setItemText(13, _translate("Room", "Apartment"))
        self.comboBox.setItemText(14, _translate("Room", "Connecting Rooms"))
        self.comboBox.setItemText(15, _translate("Room", "Murphy Room"))
        self.comboBox.setItemText(16, _translate("Room", "Accessible Room / Disabled Room"))
        self.comboBox.setItemText(17, _translate("Room", "Cabana"))
        self.comboBox.setItemText(18, _translate("Room", "Villa"))
        self.comboBox.setItemText(19, _translate("Room", "Executive Floor / Floored Room"))
        self.comboBox.setItemText(20, _translate("Room", "Non-Smoking Room"))
        self.comboBox.setItemText(21, _translate("Room", "Smoking Room"))

import UI.rc_rc
