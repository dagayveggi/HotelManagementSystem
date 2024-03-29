from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtSql import QSqlQuery, QSqlError, QSqlQueryModel
from Ops.threading import TableWorker, update_table

def collect_data(ui, db): #! Please add cute Icons back, sir
    num_model = QSqlQueryModel()
    cust_model = QSqlQueryModel()
    ui.treeView = QtWidgets.QTreeView(ui.comboBox)
    db.open()
    num_model.setQuery('SELECT Number FROM Room', db)
    cust_model.setQuery('SELECT Name, ID, Sex FROM Customer', db)
    db.close()

    while cust_model.canFetchMore():
        cust_model.fetchMore()

    ui.comboBox_2.setModel(num_model)
    ui.comboBox.setModel(cust_model)

    ui.comboBox.setView(ui.treeView)
    ui.treeView.setColumnHidden(2, True)

    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(":/ctmr/48px-Emblem-person-blue.svg.png"))
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap(":/ctmr/48px-User_icon_3.svg.png"))

    i = 0
    while i < ui.comboBox.count():
        #print(cust_model.index(i, 1).data())
        if cust_model.index(i, 2).data() == 'Male':
            ui.comboBox.setItemIcon(i, icon4)
        else:
            ui.comboBox.setItemIcon(i, icon5)
        i+=1

def new_reservation(ui, window, db, discount, thrd, mainui, model):
    db.open()
    query = QSqlQuery(db)
    #Retrieve room price from DB
    price_query = QSqlQuery(db)
    price_query.prepare('SELECT Price FROM Room WHERE Number = ?')
    price_query.addBindValue(ui.comboBox_2.currentText())
    price_query.exec_()
    price_query.next()
    price = price_query.value(0)
    #Prepare a query and add all values then execute and commit to DB
    db.transaction()
    query.prepare('INSERT INTO CurrentReservation VALUES (?,?,?,?,?,?,?,?)')
    query.addBindValue(ui.lineEdit.text())
    query.addBindValue(ui.treeView.currentIndex().siblingAtColumn(1).data())
    query.addBindValue(ui.comboBox_2.currentText())
    query.addBindValue(ui.dateEdit.date().toString("yyyy-MM-dd"))
    query.addBindValue(ui.dateEdit_2.date().toString("yyyy-MM-dd"))
    #Check if discount is applied
    if discount:
        query.addBindValue(ui.spinBox.value())
        query.addBindValue(0)
        query.addBindValue(price - (price * (ui.spinBox.value() / 100)))
    else:
        query.addBindValue(ui.spinBox.value())
        query.addBindValue(0)
        query.addBindValue(price)
    query.exec_()
    db.commit()
    db.close()
    if query.lastError().text() == '':
        QtWidgets.QMessageBox.information(window, 'New Reservation', 
                                            'New Reservation has been successfully created', 
                                            QtWidgets.QMessageBox.Ok)
    else:
        QtWidgets.QMessageBox.information(window, 'New Reservation', 
                                            query.lastError().text(), 
                                            QtWidgets.QMessageBox.Ok)
    ui.lineEdit.clear()
    ui.checkBox.setCheckState(QtCore.Qt.Unchecked)
    hlist = ['Reserv. ID','Customer ID','Room #','From','To','Discount','Extension','Net Total']
    worker = TableWorker(update_table("CurrentReservation", hlist, mainui.current_res, db, model))
    thrd.tryStart(worker)