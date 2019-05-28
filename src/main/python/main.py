from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from newReservation import Ui_MainWindow
import sqlite3

import sys

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        ui = Ui_MainWindow()
        window = QMainWindow()
        version = self.build_settings['version']
        ui.setupUi(window)
        window.setWindowTitle("HotelManagementSystem v" + version)
        window.resize(350, 150)
        window.show()
        conn = sqlite3.connect(self.get_resource('hotel.db'))
        c = conn.cursor()
        c.execute('SELECT * FROM Room')
        print(c.fetchone())
        return self.app.exec_()                 # 3. End run() with this line

if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    appctxt.app.setStyle('Fusion')
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)