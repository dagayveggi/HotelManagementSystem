from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import QThread, QThreadPool
from PyQt5 import QtCore, QtChart
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from UI.newReservation import Ui_Reservation
from UI.room import Ui_Room
from UI.customer import Ui_Customer
from UI.service import Ui_Service
from UI.mainwin import Ui_MainWindow
from Ops.service_ops import *
from Ops.threading import tableWorker
from random import randrange

import sys

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        ui = Ui_MainWindow()
        window = QMainWindow()
        version = self.build_settings['version']
        ui.setupUi(window)
        window.setWindowTitle("HotelManagementSystem v" + version)

        #Setup Charts for isolated UI editing
        ui.chartView = QtChart.QChartView(window)
        ui.chartView_2 = QtChart.QChartView(window)
        ui.gridLayout_3 = QtWidgets.QGridLayout(ui.groupBox_2)
        ui.gridLayout_3.addWidget(ui.chartView, 0, 0, 1, 1)
        ui.gridLayout_4 = QtWidgets.QGridLayout(ui.groupBox_3)
        ui.gridLayout_4.addWidget(ui.chartView_2, 0, 0, 1, 1)

        window.showMaximized()

        #Database connection, instead of sqlite3
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName(self.get_resource('hotel.db'))
        model = QSqlTableModel(self.app, db)

        #Setup Signals
        ui.newRes.triggered.connect(self.newResDialog)
        ui.newRoom.triggered.connect(self.newRoomDialog)
        ui.newService.triggered.connect(self.newServiceDialog)
        ui.newCustomer.triggered.connect(self.newCustomerDialog)

        #Threading
        thrd = QThreadPool().globalInstance()
        thrd.setExpiryTimeout(5)
        hlist = ['Reserv. ID','Customer ID','Room #','From','To','Discount','Extension','Net Total']
        worker = tableWorker(self.updateTable("Room", hlist, ui, db, model)) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        return self.app.exec_()                 # 3. End run() with this line

    def updateTable(self, table, headers, ui, db, model):
        db.open()
        model.setTable(table)
        num = 0
        for i in headers:
            model.setHeaderData(num, QtCore.Qt.Horizontal, i)
            num+=1
        model.select()
        ui.tableView.setModel(model)
        db.close()

    def newResDialog(self):
        ui = Ui_Reservation()
        newRes = QDialog()
        ui.setupUi(newRes)
        newRes.setWindowTitle('Create, edit, or delete a Reservation')
        newRes.exec()
    
    def newRoomDialog(self):
        ui = Ui_Room()
        newRm = QDialog()
        ui.setupUi(newRm)
        newRm.setWindowTitle('Create, edit, or delete a Room')
        newRm.exec()

    def newCustomerDialog(self):
        ui = Ui_Customer()
        newCust = QDialog()
        ui.setupUi(newCust)
        newCust.setWindowTitle('Create, edit, or delete a Customer')
        newCust.exec()
    
    def newServiceDialog(self):
        #setup DB
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName(self.get_resource('hotel.db'))
        model = QSqlTableModel(self.app, db)
        
        #Setup UI
        ui = Ui_Service()
        newSrv = QDialog()
        ui.setupUi(newSrv)

        #Setup Threading
        thrd = QThreadPool().globalInstance()
        worker = tableWorker(self.updateTable("Service", ['Service ID','Name','Price'], ui, db, model)) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        #Setup Signals and other UI elements
        ui.pushButton.clicked.connect(lambda: addSrv(ui, newSrv, db, thrd, model, self.updateTable))
        ui.pushButton_2.clicked.connect(lambda: editSrv(ui, newSrv, db, thrd, model, self.updateTable))
        ui.pushButton_3.clicked.connect(lambda: delSrv(ui, newSrv, db, thrd, model, self.updateTable))
        #When an item in the tableView is selected update lineEdit_2 for better workflow
        ui.tableView.clicked.connect(lambda index: ui.lineEdit_2.setText(index.siblingAtColumn(0).data()))
        ui.lineEdit_2.setText("SRVC" + str(randrange(100, 999, 10)))

        #execute
        newSrv.setWindowTitle('Create, edit, or delete a Service')
        newSrv.exec()

if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    appctxt.app.setStyle('Fusion')
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)