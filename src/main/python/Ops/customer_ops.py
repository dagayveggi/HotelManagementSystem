from PyQt5 import QtWidgets, QtCore
from Ops.threading import tableWorker, update_table
from PyQt5.QtSql import QSqlQuery, QSqlError
from Ops.threading import tableWorker, update_table

def add_rm(ui, window, db):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare('INSERT INTO Room VALUES(?, ?, ?, ?)')
    query.addBindValue(ui.lineEdit.text())
    query.addBindValue(ui.comboBox.currentText())
    query.addBindValue(ui.spinBox.value())
    query.addBindValue(0)
    try:
        query.exec_()
        db.commit()
        db.close()
        QtWidgets.QMessageBox.information(window, 'New Room created', 
                                            'New Room has been successfully created', 
                                            QtWidgets.QMessageBox.Ok)
    except Exception:
        QtWidgets.QMessageBox.critical(window, 'Error', 
                                            'Something went wrong', 
                                            QtWidgets.QMessageBox.Ok)
    finally:
        ui.lineEdit.clear()
        ui.spinBox.setValue(0)

def del_rm(ui, window, db):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare('DELETE FROM Room WHERE Number = ?')
    query.addBindValue(ui.lineEdit.text())
    try:
        query.exec_()
        db.commit()
        db.close()
        QtWidgets.QMessageBox.information(window, 'Room deleted', 
                                            'Room has been successfully deleted', 
                                            QtWidgets.QMessageBox.Ok)
    except Exception:
        QtWidgets.QMessageBox.critical(window, 'Error', 
                                            'Something went wrong', 
                                            QtWidgets.QMessageBox.Ok)
    finally:
        ui.lineEdit.clear()
        ui.spinBox.setValue(0)

def edit_rm(ui, window, db):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare('UPDATE Room SET Number = ?, Type = ?, Price = ? WHERE Number = ?')
    query.addBindValue(ui.lineEdit.text())
    query.addBindValue(ui.comboBox.currentText())
    query.addBindValue(ui.spinBox.value())
    query.addBindValue(ui.lineEdit.text())
    try:
        query.exec_()
        db.commit()
        db.close()
        QtWidgets.QMessageBox.information(window, 'Room edited', 
                                            'Room has been successfully edited', 
                                            QtWidgets.QMessageBox.Ok)
    except Exception:
        QtWidgets.QMessageBox.critical(window, 'Error', 
                                            'Something went wrong', 
                                            QtWidgets.QMessageBox.Ok)
    finally:
        ui.lineEdit.clear()
        ui.spinBox.setValue(0)


def update_custTable_onEnter(window, hlist, ui, db, thrd, model):
    db.open()
    if ui.lineEdit_2.text() != '':
        query = QSqlQuery(db)
        query.setForwardOnly(True)
        query.prepare('SELECT Name, Phone, DoB, Sex FROM Customer WHERE ID = ?')
        query.addBindValue(ui.lineEdit_2.text())
        query.exec_()
        if query.record().count() > 0:
            query.next()
            ui.lineEdit.setText(query.value(0))
            ui.spinBox.setValue(query.value(1))
            ui.dateEdit.setDate(ui.dateEdit.date().fromString(query.value(2), "yyyy-M-d"))
            ui.comboBox.setCurrentIndex(ui.comboBox.findText(query.value(3)))
            db.close()
        else:
            QtWidgets.QMessageBox.warning(window,'Warning',f"Customer with ID: {ui.lineEdit_2.text()} was not found", QtWidgets.QMessageBox.NoButton)
            ui.lineEdit.clear()
            ui.lineEdit_2.clear()
            ui.spinBox.setValue(0)
            ui.dateEdit.setDate(ui.dateEdit.date().currentDate())
    else:
        thrd.tryStart(tableWorker(update_table("CurrentReservation", hlist, ui.tableView, db, model, where=f"CtmrID={ui.lineEdit_2.text()}")))