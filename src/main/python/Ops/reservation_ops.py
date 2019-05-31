from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtSql import QSqlQuery, QSqlError, QSqlQueryModel
from Ops.threading import tableWorker, update_table

def collect_data(ui, db): #! Needs revision and reformatting
    num_model = QSqlQueryModel()
    cust_model = QSqlQueryModel()
    ui.treeView = QtWidgets.QTreeView(ui.comboBox)
    #cust_ID = QSqlQuery(db)
    db.open()
    num_model.setQuery('SELECT Number FROM Room', db)
    cust_model.setQuery('SELECT Name, ID, Sex FROM Customer', db)
    #cust_ID.exec('SELECT ID FROM Customer')
    db.close()

    while cust_model.canFetchMore():
        cust_model.fetchMore()

    ui.comboBox_2.setModel(num_model)
    ui.comboBox.setModel(cust_model)

    ui.comboBox.setView(ui.treeView)
    ui.treeView.setColumnHidden(2, True)

    """icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(":/ctmr/48px-Emblem-person-blue.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap(":/ctmr/48px-User_icon_3.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    i = 0
    while i < cust_model.rowCount():
        #print(cust_model.index(i, 1).data())
        if cust_model.index(i, 2).data() == 'Male':
            ui.comboBox.addItem(icon4, cust_model.index(i, 0).data(), cust_model.index(i, 1).data())
        else:
            ui.comboBox.addItem(icon5, cust_model.index(i, 0).data(), cust_model.index(i, 1).data())
        i+=1"""

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