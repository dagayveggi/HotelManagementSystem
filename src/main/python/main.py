from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import QThread, QThreadPool
from PyQt5 import QtCore, QtChart
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from UI.newReservation import Ui_Reservation
from UI.room import Ui_Room
from UI.customer import Ui_Customer
from UI.service import Ui_Service
from UI.mainwin import Ui_MainWindow
from Ops.reservation_ops import *
from Ops.service_ops import *
from Ops.threading import tableWorker, update_table
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
        ui.newRes.triggered.connect(lambda: self.new_res_dialog(db, ui, model))
        ui.newRoom.triggered.connect(lambda: self.new_room_dialog(db))
        ui.newService.triggered.connect(lambda: self.new_srv_dialog(db))
        ui.newCustomer.triggered.connect(lambda: self.new_customer_dialog(db))
        ui.cancelRes.triggered.connect(lambda: self.new_cancel_dialog((window, db, ui.current_res.currentIndex().siblingAtColumn(0).data())))
        ui.current_res.doubleClicked.connect(lambda: self.new_cancel_dialog((window, db, ui.current_res.currentIndex().siblingAtColumn(0).data())))
        
        #Threading
        thrd = QThreadPool().globalInstance()
        thrd.setExpiryTimeout(5)
        hlist = ['Reserv. ID','Customer ID','Room #','From','To','Discount','Extension','Net Total']
        worker = tableWorker(update_table("CurrentReservation", hlist, ui.current_res, db, model)) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        return self.app.exec_()                 # 3. End run() with this line

    def new_res_dialog(self, db, mainui, model):
        ui = Ui_Reservation()
        new_res = QDialog()
        ui.setupUi(new_res)

        thrd = QThreadPool().globalInstance()
        worker = tableWorker(collect_data(ui, db))
        
        ui.pushButton.clicked.connect(lambda: new_reservation(ui, new_res, db, ui.checkBox.isChecked(), thrd, mainui, model))
        ui.lineEdit.setText("RES" + str(randrange(100, 999, 10)))
        ui.dateEdit.setDate(ui.dateEdit.date().currentDate())
        ui.dateEdit_2.setDate(ui.dateEdit.date().currentDate())
        ui.checkBox.stateChanged.connect(ui.spinBox.setEnabled)

        new_res.setWindowTitle('Create, edit, or delete a Reservation')
        new_res.exec()
    
    def new_room_dialog(self, db):
        ui = Ui_Room()
        new_rm = QDialog()
        ui.setupUi(new_rm)

        model = QSqlTableModel(new_rm, db)
        
        new_rm.setWindowTitle('Create, edit, or delete a Room')
        new_rm.exec()

    def new_customer_dialog(self, db):
        ui = Ui_Customer()
        new_cust = QDialog()
        ui.setupUi(new_cust)

        model = QSqlTableModel(new_cust, db)

        #Setup Threading
        thrd = QThreadPool().globalInstance()
        worker = tableWorker(update_table("Customer", ['Customer ID','Name','Phone #','Date of Birth','# Reservations'], ui.tableView, db, model)) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        new_cust.setWindowTitle('Create, edit, or delete a Customer')
        new_cust.exec()
    
    def new_srv_dialog(self, db):
        #Setup UI
        ui = Ui_Service()
        new_srv = QDialog()
        ui.setupUi(new_srv)

        model = QSqlTableModel(new_srv, db)

        #Setup Threading
        thrd = QThreadPool().globalInstance()
        worker = tableWorker(update_table("Service", ['Service ID','Name','Price'], ui.tableView, db, model)) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        #Setup Signals and other UI elements
        ui.pushButton.clicked.connect(lambda: add_srv(ui, new_srv, db, thrd, model))
        ui.pushButton_2.clicked.connect(lambda: edit_srv(ui, new_srv, db, thrd, model))
        ui.pushButton_3.clicked.connect(lambda: del_srv(ui, new_srv, db, thrd, model))
        #When an item in the tableView is selected update lineEdit and lineEdit_2 for better workflow
        #You can just repeat the connect() method and it wouldn't override the previous one
        ui.tableView.clicked.connect(lambda index: ui.lineEdit_2.setText(index.siblingAtColumn(0).data()))
        ui.tableView.clicked.connect(lambda index: ui.lineEdit.setText(index.siblingAtColumn(1).data()))
        ui.tableView.clicked.connect(lambda index: ui.doubleSpinBox.setValue(index.siblingAtColumn(2).data()))
        ui.lineEdit_2.setText("SRVC" + str(randrange(100, 999, 10)))

        #execute
        new_srv.setWindowTitle('Create, edit, or delete a Service')
        new_srv.exec()
    
    def new_cancel_dialog(self, window, db, resID):
        new_cancel = QMessageBox.critical(window, 'Cancel Reservation',
                                            'Are you sure you want to cancel the select Reservation',
                                            QMessageBox.Yes | QMessageBox.No)
        if new_cancel.exec_() == QMessageBox.Yes:
            db.open()
            query = QSqlQuery(db)
            db.transaction()
            query.prepare('DELETE FROM CurrentReservation WHERE ResID = ?')
            query.addBindValue(resID)
            query.exec_()
            db.commit()
            db.close
        else:
            new_cancel.close()


if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    appctxt.app.setStyle('Fusion')
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)