from PyQt5 import QtWidgets, QtCore
from PyQt5.QtSql import QSqlQuery, QSqlError
from Ops.threading import tableWorker

def addSrv(ui, window, db, thrd, model):
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
    #Call the updateSrvTable func through a worker and start it using the global threadpool
    worker = tableWorker(updateSrvTable(ui, db, model))
    thrd.tryStart(worker)

def delSrv(ui, window, db, thrd, model):
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
    #Call the updateSrvTable func through a worker and start it using the global threadpool
    worker = tableWorker(updateSrvTable(ui, db, model))
    thrd.tryStart(worker)

def editSrv(ui, window, db, thrd, model):
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
    #Call the updateSrvTable func through a worker and start it using the global threadpool
    worker = tableWorker(updateSrvTable(ui, db, model))
    thrd.tryStart(worker)

def updateSrvTable(ui, db, model):
        db.open()
        model.setTable("Service")
        model.setHeaderData(0, QtCore.Qt.Horizontal,'Service ID')
        model.setHeaderData(1, QtCore.Qt.Horizontal,'Name')
        model.setHeaderData(2, QtCore.Qt.Horizontal,'Price')
        model.select()
        ui.tableView.setModel(model)
        db.close()