# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Desktop\HotelManagementSystem\src\main\resources\base\customer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Customer(object):
    def setupUi(self, Customer):
        Customer.setObjectName("Customer")
        Customer.resize(800, 478)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ctmr/48px-System-users-3.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Customer.setWindowIcon(icon)
        self.gridLayout_6 = QtWidgets.QGridLayout(Customer)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Customer)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/commands/48px-Ambox_emblem_plus.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/commands/48px-Edit-find-replace.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/commands/48px-Edit-delete.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 13, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 8, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 9, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setObjectName("comboBox")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ctmr/48px-Emblem-person-blue.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ctmr/48px-User_icon_3.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon5, "")
        self.gridLayout_2.addWidget(self.comboBox, 9, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Customer)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.gridLayout_4.addWidget(self.tableView, 0, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Res/48px-Appointment.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableView_2 = QtWidgets.QTableView(self.tab_2)
        self.tableView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout_5.addWidget(self.tableView_2, 0, 0, 1, 1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Res/48px-Appointment-archive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon7, "")
        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Customer)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Customer)
        Customer.setTabOrder(self.lineEdit_2, self.lineEdit)
        Customer.setTabOrder(self.lineEdit, self.spinBox)
        Customer.setTabOrder(self.spinBox, self.dateEdit)
        Customer.setTabOrder(self.dateEdit, self.comboBox)
        Customer.setTabOrder(self.comboBox, self.pushButton_3)
        Customer.setTabOrder(self.pushButton_3, self.pushButton_2)
        Customer.setTabOrder(self.pushButton_2, self.pushButton)
        Customer.setTabOrder(self.pushButton, self.tabWidget)
        Customer.setTabOrder(self.tabWidget, self.tableView)
        Customer.setTabOrder(self.tableView, self.tableView_2)

    def retranslateUi(self, Customer):
        _translate = QtCore.QCoreApplication.translate
        Customer.setWindowTitle(_translate("Customer", "MainWindow"))
        self.groupBox.setTitle(_translate("Customer", "Information"))
        self.groupBox_2.setTitle(_translate("Customer", "Commands"))
        self.pushButton_3.setText(_translate("Customer", "Add"))
        self.pushButton_2.setText(_translate("Customer", "Edit"))
        self.pushButton.setText(_translate("Customer", "Delete"))
        self.label.setText(_translate("Customer", "Name:"))
        self.spinBox.setPrefix(_translate("Customer", "0"))
        self.label_3.setText(_translate("Customer", "Date of Birth:"))
        self.label_2.setText(_translate("Customer", "Phone Number:"))
        self.label_4.setText(_translate("Customer", "Sex:"))
        self.comboBox.setItemText(0, _translate("Customer", "Male"))
        self.comboBox.setItemText(1, _translate("Customer", "Female"))
        self.label_5.setText(_translate("Customer", "Customer ID:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Customer", "Current Reservations"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Customer", "Archived Reservations"))

import UI.rc_rc
