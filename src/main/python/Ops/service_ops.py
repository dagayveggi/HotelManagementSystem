from PyQt5 import QtWidgets, QtCore
from PyQt5.QtSql import QSqlQuery, QSqlError
from Ops.threading import tableWorker

def add_srv(ui, window, db, thrd, model, updater):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
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
    ui.lineEdit_2.clear()
    ui.lineEdit.clear()
    ui.doubleSpinBox.setValue(0)
    #Call the updateSrvTable func through a worker and start it using the global threadpool
    worker = tableWorker(updater("Service", ['Service ID','Name','Price'], ui, db, model))
    thrd.tryStart(worker)

def del_srv(ui, window, db, thrd, model, updater):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    query.prepare('DELETE FROM Service WHERE ID = ?')
    query.bindValue(0, ui.lineEdit_2.text())
    query.exec()
    db.commit()
    db.close()
    QtWidgets.QMessageBox.information(window, 'Service deleted', 
                                        'Service has been successfully deleted', 
                                        QtWidgets.QMessageBox.Ok)
    ui.lineEdit_2.clear()
    ui.lineEdit.clear()
    ui.doubleSpinBox.setValue(0)
    #Call the updateSrvTable func through a worker and start it using the global threadpool
    worker = tableWorker(updater("Service", ['Service ID','Name','Price'], ui, db, model))
    thrd.tryStart(worker)

def edit_srv(ui, window, db, thrd, model, updater):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    query.prepare('UPDATE Service SET ID = ?, Name = ?, Price = ? WHERE ID = ?')
    query.bindValue(0, ui.lineEdit_2.text())
    query.bindValue(1, ui.lineEdit.text())
    query.bindValue(2, ui.doubleSpinBox.value())
    query.bindValue(3, ui.lineEdit_2.text())
    query.exec()
    db.commit()
    db.close()
    QtWidgets.QMessageBox.information(window, 'Service edited', 
                                        'Service has been successfully edited', 
                                        QtWidgets.QMessageBox.Ok)
    ui.lineEdit_2.clear()
    ui.lineEdit.clear()
    ui.doubleSpinBox.setValue(0)
    #Call the updateSrvTable func through a worker and start it using the global threadpool
    worker = tableWorker(updater("Service", ['Service ID','Name','Price'], ui, db, model))
    thrd.tryStart(worker)