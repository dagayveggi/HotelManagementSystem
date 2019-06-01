from PyQt5 import QtWidgets, QtCore
from PyQt5.QtSql import QSqlQuery, QSqlError
from Ops.threading import tableWorker, update_table

def add_rm(ui, window, db, thrd, model):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare('INSERT INTO Room VALUES(?, ?, ?, ?)')
    query.addBindValue(ui.lineEdit.text())
    query.addBindValue(ui.comboBox.currentText())
    query.addBindValue(ui.spinBox.value())
    query.exec_()
    db.commit()
    db.close()
    QtWidgets.QMessageBox.information(window, 'New Room created', 
                                        'New Room has been successfully created', 
                                        QtWidgets.QMessageBox.Ok)
    ui.lineEdit.clear()
    ui.spinBox.setValue(0)

def del_rm(ui, window, db, thrd, model):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare('DELETE FROM Room WHERE Number = ?')
    query.addBindValue(ui.lineEdit.text())
    query.exec_()
    db.commit()
    db.close()
    QtWidgets.QMessageBox.information(window, 'Room deleted', 
                                        'Room has been successfully deleted', 
                                        QtWidgets.QMessageBox.Ok)
    ui.lineEdit.clear()
    ui.spinBox.setValue(0)

def edit_rm(ui, window, db, thrd, model):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare('UPDATE Room SET Number = ?, Type = ?, Price = ? WHERE Number = ?')
    query.addBindValue(ui.lineEdit.text())
    query.addBindValue(ui.comboBox.currentText())
    query.addBindValue(ui.spinBox.value())
    query.addBindValue(ui.lineEdit.text())
    query.exec_()
    db.commit()
    db.close()
    QtWidgets.QMessageBox.information(window, 'Room edited', 
                                        'Room has been successfully edited', 
                                        QtWidgets.QMessageBox.Ok)
    ui.lineEdit.clear()
    ui.spinBox.setValue(0)