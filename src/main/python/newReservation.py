# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/resources/newReservation.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 291)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.groupBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setEnabled(False)
        self.spinBox.setFrame(True)
        self.spinBox.setSuffix("")
        self.spinBox.setMaximum(100)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.checkBox.stateChanged.connect(self.spinBox.setEnabled)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New Reservation"))
        self.groupBox.setTitle(_translate("MainWindow", "Reserve A Room"))
        self.label_3.setText(_translate("MainWindow", "Customer:"))
        self.label_4.setText(_translate("MainWindow", "Room:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Date of Reservation"))
        self.label.setText(_translate("MainWindow", "From:"))
        self.label_2.setText(_translate("MainWindow", "To:"))
        self.checkBox.setText(_translate("MainWindow", "Discount?"))
        self.spinBox.setPrefix(_translate("MainWindow", "%"))
        self.pushButton.setText(_translate("MainWindow", "Reserve"))


