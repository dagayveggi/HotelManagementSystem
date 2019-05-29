# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Desktop\HotelManagementSystem\src\main\resources\base\service.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Service(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 166)
        self.formLayout = QtWidgets.QFormLayout(MainWindow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(MainWindow)
        self.doubleSpinBox.setSuffix("")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Service Name:"))
        self.label_2.setText(_translate("MainWindow", "Price:"))
        self.doubleSpinBox.setPrefix(_translate("MainWindow", "$"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Edit"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.label_3.setText(_translate("MainWindow", "Service ID:"))