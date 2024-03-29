from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import QThread, QThreadPool
from PyQt5 import QtCore, QtChart
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery, QSqlQueryModel
from UI.newReservation import Ui_Reservation
from UI.room import Ui_Room
from UI.customer import Ui_Customer
from UI.service import Ui_Service
from UI.add_service import Ui_AddService
from UI.mainwin import Ui_MainWindow
from Ops.database_ops import *
from Ops.reservation_ops import *
from Ops.room_ops import *
from Ops.customer_ops import *
from Ops.threading import TableWorker, update_table
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

        #Threading
        thrd = QThreadPool().globalInstance()
        thrd.setExpiryTimeout(5)
        hlist = ['Reserv. ID','Customer ID','Room #','From','To','Discount','Extension','Net Total']
        worker = TableWorker(update_table("CurrentReservation", hlist, ui.current_res, db, model)) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        #Setup Signals
        ui.newRes.triggered.connect(lambda: self.new_res_dialog(db, ui, model))
        ui.newRoom.triggered.connect(lambda: self.new_room_dialog(db))
        ui.newService.triggered.connect(lambda: self.new_srv_dialog(db))
        ui.newCustomer.triggered.connect(lambda: self.new_customer_dialog(db))
        ui.cancelRes.triggered.connect(lambda: self.new_cancel_dialog(window, db,
                                                ui.current_res.currentIndex(),
                                                thrd, model, hlist, ui.current_res))
        #TODO Add new dialog for adding/deleting services to a current Reservation
        ui.current_res.doubleClicked.connect(lambda: self.new_addservice_dialog(window, db, 
                                                    ui.current_res.currentIndex(), thrd))

        return self.app.exec_()                 # 3. End run() with this line

    def new_res_dialog(self, db, mainui, model):
        ui = Ui_Reservation()
        new_res = QDialog()
        ui.setupUi(new_res)

        thrd = QThreadPool().globalInstance()
        worker = TableWorker(collect_data(ui, db))
        thrd.tryStart(worker)
        
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

        #Threading
        thrd = QThreadPool().globalInstance()
        hlist = ['Reserv. ID','Customer ID','Room #','From','To','Discount','Extension','Net Total']
        worker = TableWorker(update_table("CurrentReservation", hlist, ui.tableView, db, model, where=f"RmNumber={ui.lineEdit.text()}")) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        #Setup Signals and other UI elements
        ui.lineEdit.setFocus()
        # TODO find a better signal than textChanged because it sucks bad
        ui.lineEdit.textChanged.connect(lambda: update_table_onEnter(new_rm, hlist, ui, db, thrd, model))
        ui.pushButton_3.clicked.connect(lambda: thrd.tryStart(TableWorker(add_DB(ui, new_rm, db, 
                                                "Room",
                                                [ui.lineEdit.text(),ui.comboBox.currentText(),ui.spinBox.value(),0],
                                                "?, ?, ?, ?",
                                                [ui.lineEdit,ui.spinBox]))))
        ui.pushButton_2.clicked.connect(lambda: thrd.tryStart(TableWorker(edit_DB(ui, new_rm, db,
                                                "Room",
                                                [ui.lineEdit.text(),ui.comboBox.currentText(),ui.spinBox.value(),ui.lineEdit.text()],
                                                "Number = ?, Type = ?, Price = ?",
                                                "Number",
                                                [ui.lineEdit,ui.spinBox]))))
        ui.pushButton.clicked.connect(lambda: thrd.tryStart(TableWorker(del_DB(ui, new_rm, db,
                                                    "Room", "Number = ?", [ui.lineEdit.text()],
                                                    [ui.lineEdit,ui.spinBox]))))

        new_rm.setWindowTitle('Create, edit, or delete a Room')
        new_rm.exec()

    def new_customer_dialog(self, db):
        ui = Ui_Customer()
        new_cust = QDialog()
        ui.setupUi(new_cust)

        model = QSqlTableModel(new_cust, db)

        #Setup Threading
        thrd = QThreadPool().globalInstance()
        hlist = ['Customer ID','Name','Phone #','Date of Birth','# Reservations']
        worker = TableWorker(update_table("Customer", hlist, ui.tableView, db, model)) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        #? Consider using, instead of QSqlQuery, A QSqlTableModel and insert or delete from it
        ui.lineEdit_2.textEdited.connect(lambda: update_custTable_onEnter(new_cust, hlist, ui, db, thrd, model))
        ui.pushButton_3.clicked.connect(lambda: thrd.tryStart(TableWorker(add_DB(ui, new_cust, db, 
                                                "Customer",
                                                [ui.lineEdit_2.text(),ui.lineEdit.text(),ui.spinBox.value(),ui.dateEdit.date().toString("yyyy-MM-dd"),ui.comboBox.currentText(),0],
                                                "?,?,?,?,?,?",
                                                [ui.lineEdit_2,ui.lineEdit,ui.spinBox,ui.dateEdit]))))
        ui.pushButton_2.clicked.connect(lambda: thrd.tryStart(TableWorker(edit_DB(ui, new_cust, db,
                                                "Customer",
                                                [ui.lineEdit_2.text(),ui.lineEdit.text(),ui.spinBox.value(),ui.dateEdit.date().toString("yyyy-MM-dd"),ui.comboBox.currentText(),ui.lineEdit_2.text()],
                                                "ID = ?, Name = ?, Phone = ?, DoB = ?, Sex = ?",
                                                "ID",
                                                [ui.lineEdit_2,ui.lineEdit,ui.spinBox,ui.dateEdit]))))
        ui.pushButton.clicked.connect(lambda: thrd.tryStart(TableWorker(del_DB(ui, new_cust, db,
                                                    "Customer", "ID = ?", [ui.lineEdit_2.text()],
                                                    [ui.lineEdit_2,ui.lineEdit,ui.spinBox,ui.dateEdit]))))
        ui.lineEdit_2.setText("CTMR" + str(randrange(100, 999, 10)))

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
        worker = TableWorker(update_table("Service", ['Service ID','Name','Price'], ui.tableView, db, model)) #We pass a function for the worker to execute
        thrd.tryStart(worker)

        #Setup Signals and other UI elements
        ui.pushButton.clicked.connect(lambda: thrd.tryStart(TableWorker(add_DB(ui, new_srv, db, 
                                                "Service",
                                                [ui.lineEdit_2.text(),ui.lineEdit.text(),ui.doubleSpinBox.value()],
                                                "?,?,?",
                                                [ui.lineEdit_2,ui.lineEdit,ui.doubleSpinBox]))))
        ui.pushButton_2.clicked.connect(lambda: thrd.tryStart(TableWorker(edit_DB(ui, new_srv, db,
                                                "Service",
                                                [ui.lineEdit_2.text(),ui.lineEdit.text(),ui.doubleSpinBox.value(),ui.lineEdit_2.text()],
                                                "ID = ?, Name = ?, Price = ?",
                                                "ID",
                                                [ui.lineEdit_2,ui.lineEdit,ui.doubleSpinBox]))))
        ui.pushButton_3.clicked.connect(lambda: thrd.tryStart(TableWorker(del_DB(ui, new_srv, db,
                                                    "Service", "ID = ?", [ui.lineEdit_2.text()],
                                                    [ui.lineEdit_2,ui.lineEdit,ui.doubleSpinBox]))))
        #When an item in the tableView is selected update lineEdit and lineEdit_2 for better workflow
        #You can just repeat the connect() method and it wouldn't override the previous one
        ui.tableView.clicked.connect(lambda index: ui.lineEdit_2.setText(index.siblingAtColumn(0).data()))
        ui.tableView.clicked.connect(lambda index: ui.lineEdit.setText(index.siblingAtColumn(1).data()))
        ui.tableView.clicked.connect(lambda index: ui.doubleSpinBox.setValue(index.siblingAtColumn(2).data()))
        ui.lineEdit_2.setText("SRVC" + str(randrange(100, 999, 10)))

        #execute
        new_srv.setWindowTitle('Create, edit, or delete a Service')
        new_srv.exec()
    
    def new_cancel_dialog(self, window, db, res_index, thrd, model, hlist, widget):
        new_cancel = QMessageBox(window)
        new_cancel.setWindowTitle('Cancel Reservation')
        new_cancel.setText('Are you sure you want to cancel the select Reservation')
        new_cancel.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        #TODO Add a boolean column for cancelation
        if new_cancel.exec_() == QMessageBox.Yes:
            db.open()
            query = QSqlQuery(db)
            db.transaction()
            query.prepare('INSERT INTO CancelledReservation VALUES(?, ?, ?)')
            query.addBindValue(res_index.siblingAtColumn(0).data())
            query.addBindValue(res_index.siblingAtColumn(1).data())
            query.addBindValue(res_index.siblingAtColumn(2).data())
            query.exec_()
            query.prepare('DELETE FROM CurrentReservation WHERE ResID = ?')
            query.addBindValue(res_index.siblingAtColumn(0).data())
            query.exec_()
            db.commit()
            db.close()
            worker = TableWorker(update_table("CurrentReservation", hlist, widget, db, model))
            thrd.tryStart(worker)
        else:
            new_cancel.close()

    def new_addservice_dialog(self, window, db, res_index, thrd):
        #Setup UI
        ui = Ui_AddService()
        new_addservice = QDialog()
        ui.setupUi(new_addservice)

        #Setup ComboBox view
        db.open()
        srv_model = QSqlQueryModel()
        ui.treeView = QtWidgets.QTreeView(ui.comboBox)
        srv_model.setQuery('SELECT Name, ID FROM Service', db)
        db.close()

        while srv_model.canFetchMore():
            srv_model.fetchMore()
        ui.comboBox.setModel(srv_model)

        ui.comboBox.setView(ui.treeView)
        db.close()

        ui.pushButton.clicked.connect(lambda: thrd.tryStart(TableWorker(add_DB(ui, new_addservice, db, 
                                                "RoomService",
                                                [res_index.siblingAtColumn(0).data(),res_index.siblingAtColumn(1).data(),res_index.siblingAtColumn(2).data(),ui.treeView.currentIndex().siblingAtColumn(1).data()],
                                                "?, ?, ?, ?",
                                                []))))
        ui.pushButton_2.clicked.connect(lambda: thrd.tryStart(TableWorker(del_DB(ui, new_addservice, db,
                                                    "RoomService", "ResID = ? AND SrvID = ?", [res_index.siblingAtColumn(0).data(), ui.treeView.currentIndex().siblingAtColumn(1).data()],
                                                    []))))

        new_addservice.setWindowTitle('Add or remove a Service')
        new_addservice.exec()

if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    appctxt.app.setStyle('Fusion')
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)