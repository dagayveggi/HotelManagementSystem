# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Desktop\HotelManagementSystem\src\main\resources\base\service.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Service(object):
    def setupUi(self, Service):
        Service.setObjectName("Service")
        Service.resize(300, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/srv/48px-Edit-clear.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Service.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Service)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Service)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setSuffix("")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/commands/48px-Edit-find-replace.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/commands/48px-Ambox_emblem_plus.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/commands/48px-Edit-delete.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(Service)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.statusbar = QtWidgets.QStatusBar(Service)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(Service)
        QtCore.QMetaObject.connectSlotsByName(Service)

    def retranslateUi(self, Service):
        _translate = QtCore.QCoreApplication.translate
        Service.setWindowTitle(_translate("Service", "MainWindow"))
        self.groupBox.setTitle(_translate("Service", "Information"))
        self.label_3.setText(_translate("Service", "Service ID:"))
        self.label.setText(_translate("Service", "Service Name:"))
        self.label_2.setText(_translate("Service", "Price:"))
        self.doubleSpinBox.setPrefix(_translate("Service", "$"))
        self.pushButton_2.setText(_translate("Service", "Edit"))
        self.pushButton.setText(_translate("Service", "Add"))
        self.pushButton_3.setText(_translate("Service", "Delete"))

import UI.rc_rc
