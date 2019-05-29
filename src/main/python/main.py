from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog
from newReservation import Ui_Reservation
from room import Ui_Room
from customer import Ui_Customer
from service import Ui_Service
from mainwin import Ui_MainWindow
import sqlite3

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
        """conn = sqlite3.connect(self.get_resource('hotel.db'))
        c = conn.cursor()
        c.execute('SELECT * FROM Room')
        print(c.fetchone())"""
        ui.newRes.triggered.connect(self.newResDialog)
        ui.newRoom.triggered.connect(self.newRoomDialog)
        ui.newService.triggered.connect(self.newServiceDialog)
        return self.app.exec_()                 # 3. End run() with this line
    
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