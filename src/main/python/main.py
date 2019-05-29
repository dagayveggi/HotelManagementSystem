from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from newReservation import Ui_Reservation
from room import Ui_Room
from customer import Ui_Customer
from service import Ui_Service
from mainwin import Ui_MainWindow, tableWorker
#import sqlite3

import sys

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        ui = Ui_MainWindow()
        window = QMainWindow()
        version = self.build_settings['version']
        ui.setupUi(window)
        window.setWindowTitle("HotelManagementSystem v" + version)
        #window.resize(350, 150)
        window.show()

        #Database connection, instead of sqlite3
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName(self.get_resource('hotel.db'))
        model = QSqlTableModel(self.app, db)

        ui.newRes.triggered.connect(self.newResDialog)
        ui.newRoom.triggered.connect(self.newRoomDialog)
        ui.newService.triggered.connect(self.newServiceDialog)

        #Threading
        thrd = QThread()
        worker = tableWorker(self.updateTable(ui, db, model)) #We pass a function for the worker to execute
        worker.moveToThread(thrd)
        thrd.start()
        thrd.started.connect(worker._run_update)
        worker.finished.connect(thrd.quit)

        return self.app.exec_()                 # 3. End run() with this line

    def updateTable(self, ui, db, model):
        db.open()
        model.setTable(f"Room")
        model.setHeaderData(0, QtCore.Qt.Horizontal,'Reserv. ID')
        model.setHeaderData(1, QtCore.Qt.Horizontal,'Customer ID')
        model.setHeaderData(2, QtCore.Qt.Horizontal,'Room #')
        model.setHeaderData(3, QtCore.Qt.Horizontal,'From')
        model.setHeaderData(4, QtCore.Qt.Horizontal,'To')
        model.setHeaderData(5, QtCore.Qt.Horizontal,'Discount')
        model.setHeaderData(6, QtCore.Qt.Horizontal,'Extension')
        model.setHeaderData(7, QtCore.Qt.Horizontal,'Net Total')
        model.select()
        ui.tableView.setModel(model)
        db.close()

    def newResDialog(self):
        ui = Ui_Reservation()
        newRes = QDialog()
        ui.setupUi(newRes)
        newRes.setWindowTitle('Create a new Reservation')
        newRes.exec()
    
    def newRoomDialog(self):
        ui = Ui_Room()
        newRm = QDialog()
        ui.setupUi(newRm)
        newRm.setWindowTitle('Create a new Room')
        newRm.exec()
    
    def newServiceDialog(self):
        ui = Ui_Service()
        newSrv = QDialog()
        ui.setupUi(newSrv)
        newSrv.setWindowTitle('Create a new Service')
        newSrv.exec()

if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    appctxt.app.setStyle('Fusion')
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)