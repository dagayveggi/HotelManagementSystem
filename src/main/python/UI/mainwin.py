# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Desktop\HotelManagementSystem\src\main\resources\base\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(self.tableView.NoEditTriggers)
        self.chartView = QtChart.QChartView(self.groupBox_2)
        self.chartView_2 = QtChart.QChartView(self.groupBox_3)
        self.gridLayout_4.addWidget(self.chartView_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.chartView, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.newRes = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Res/48px-Appointment-new.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newRes.setIcon(icon)
        self.newRes.setObjectName("newRes")
        self.newRoom = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/rm/48px-Go-home-2.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newRoom.setIcon(icon1)
        self.newRoom.setObjectName("newRoom")
        self.newService = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/srv/48px-Edit-clear.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newService.setIcon(icon2)
        self.newService.setObjectName("newService")
        self.toolBar.addAction(self.newRes)
        self.toolBar.addAction(self.newRoom)
        self.toolBar.addAction(self.newService)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Chart of Customers by Age"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Chart of Earnings by Month"))
        self.groupBox.setTitle(_translate("MainWindow", "All Current Reservations"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.newRes.setText(_translate("MainWindow", "newRes"))
        self.newRes.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create a new Reservation</p></body></html>"))
        self.newRes.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.newRoom.setText(_translate("MainWindow", "newRoom"))
        self.newRoom.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create a new Room</p></body></html>"))
        self.newRoom.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.newService.setText(_translate("MainWindow", "newService"))
        self.newService.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create a new Service</p></body></html>"))
        self.newService.setShortcut(_translate("MainWindow", "Ctrl+S"))

class tableWorker(QtCore.QRunnable):
    def __init__(self, fn):
        super(tableWorker, self).__init__()
        self.fn = fn
    
    def run(self):
        self.fn

import UI.rc_rc