from PyQt5 import QtWidgets, QtCore
from PyQt5.QtSql import QSqlQuery, QSqlError, QSqlQueryModel
from Ops.threading import tableWorker, update_table

def collect_data(ui, db):
    num_model = QSqlQueryModel()
    cust_model = QSqlQueryModel()
    cust_ID = QSqlQuery(db)
    db.open()
    num_model.setQuery('SELECT Number FROM Room', db)
    cust_model.setQuery('SELECT Name FROM Customer', db)
    cust_ID.exec('SELECT ID FROM Customer')
    db.close()

    ui.comboBox_2.setModel(num_model)
    ui.comboBox.setModel(cust_model)

def new_reservation(ui, window, db, thrd, model, discount):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    query.prepare('SELECT Price FROM Room WHERE Number = ?')
    query.bindValue(0, ui.comboBox_2.currentText())
    query.exec()
    price = query.result().data(0)
    query.prepare("""INSERT INTO CurrentReservation (ResID, CtmrID, RmNumber, From, To, Discount, Extension, NetTotal)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?)""")
    query.bindValue(0, ui.lineEdit.text())
    query.bindValue(1, ui.comboBox.currentData())
    query.bindValue(2, ui.comboBox_2.currentText())
    query.bindValue(3, ui.dateEdit.date().toString("d-M-yyyy"))
    query.bindValue(4, ui.dateEdit_2.date().toString("d-M-yyyy"))
    if discount:
        query.bindValue(5, ui.spinBox.value())
        query.bindValue(6, price - (price * (ui.spinBox.value() / 100)))
    else:
        query.bindValue(6, price)
    query.exec()
    db.commit()
    db.close()
    QtWidgets.QMessageBox.information(window, 'New Reservation created', 
                                        'New Reservation has been successfully created', 
                                        QtWidgets.QMessageBox.Ok)