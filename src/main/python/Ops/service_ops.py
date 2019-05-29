from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlQuery, QSqlError

"""
self.pushButton.clicked.connect(lambda: addSrv(None, self, MainWindow, db))
I have to add an extra argument before the required positional arguments I have for some reason..."""

def addSrv(self, ui, window, db):
    try:
        db.open()
        query = QSqlQuery(db)
        query.prepare('INSERT INTO Service (Id, Name, Price) VALUES(?, ?, ?)')
        query.bindValue(0, ui.lineEdit_2.text())
        query.bindValue(1, ui.lineEdit.text())
        query.bindValue(2, ui.doubleSpinBox.value())
        query.exec()
        db.commit()
        db.close()
        QtWidgets.QMessageBox.information(window, 'New Service created', 
                                            'New Service has been successfully created', 
                                            QtWidgets.QMessageBox.Ok)
        window.close()
    except QSqlError.TransactionError as e:
        QtWidgets.QMessageBox.critical(window, 'Transaction error', 
                                            str(e), 
                                            QtWidgets.QMessageBox.Ok)
    except QSqlError.StatementError as e:
        QtWidgets.QMessageBox.critical(window, 'Statement error', 
                                            str(e), 
                                            QtWidgets.QMessageBox.Ok)
    except QSqlError.ConnectionError as e:
        QtWidgets.QMessageBox.critical(window, 'Connection error', 
                                            str(e), 
                                            QtWidgets.QMessageBox.Ok)

def delSrv(self, ui, window, db):
    try:
        db.open()
        query = QSqlQuery(db)
        query.prepare('DELETE FROM Service WHERE ID = ?')
        query.bindValue(0, ui.lineEdit_2.text())
        query.exec()
        db.commit()
        db.close()
        QtWidgets.QMessageBox.information(window, 'Service deleted', 
                                            'Service has been successfully deleted', 
                                            QtWidgets.QMessageBox.Ok)
        window.close()
    except QSqlError.TransactionError as e:
        QtWidgets.QMessageBox.critical(window, 'Transaction error', 
                                            str(e), 
                                            QtWidgets.QMessageBox.Ok)
    except QSqlError.StatementError as e:
        QtWidgets.QMessageBox.critical(window, 'Statement error', 
                                            str(e), 
                                            QtWidgets.QMessageBox.Ok)
    except QSqlError.ConnectionError as e:
        QtWidgets.QMessageBox.critical(window, 'Connection error', 
                                            str(e), 
                                            QtWidgets.QMessageBox.Ok)