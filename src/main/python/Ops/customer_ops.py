from PyQt5 import QtWidgets, QtCore
from Ops.threading import TableWorker, update_table
from PyQt5.QtSql import QSqlQuery, QSqlError

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
            try:
                ui.spinBox.setValue(int(query.value(1)))
            except TypeError:
                ui.spinBox.setValue(0)
            ui.dateEdit.setDate(ui.dateEdit.date().fromString(query.value(2), "yyyy-M-d"))
            ui.comboBox.setCurrentIndex(ui.comboBox.findText(query.value(3)))
            db.close()
        else:
            QtWidgets.QMessageBox.warning(window,'Warning',f"Customer with ID: {ui.lineEdit_2.text()} was not found", QtWidgets.QMessageBox.NoButton)
            ui.lineEdit.clear()
            ui.lineEdit_2.clear()
            ui.spinBox.setValue(0)
            ui.dateEdit.setDate(ui.dateEdit.date().currentDate())
    elif ui.lineEdit_2.text() == '':
        thrd.tryStart(TableWorker(update_table("CurrentReservation", hlist, ui.tableView, db, model, where=f"CtmrID={ui.lineEdit_2.text()}")))