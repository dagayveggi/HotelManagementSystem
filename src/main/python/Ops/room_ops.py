from PyQt5 import QtWidgets, QtCore
from Ops.threading import tableWorker, update_table
from PyQt5.QtSql import QSqlQuery, QSqlError

def update_table_onEnter(window, hlist, ui, db, thrd, model):
    thrd.tryStart(tableWorker(update_table("CurrentReservation", hlist, ui.tableView, db, model, where=f"RmNumber={ui.lineEdit.text()}")))
    db.open()
    if ui.lineEdit.text() != '':
        query = QSqlQuery(db)
        query.setForwardOnly(True)
        query.prepare('SELECT Type, Price FROM Room WHERE Number = ?')
        query.addBindValue(ui.lineEdit.text())
        query.exec_()
        try:
            query.next()
            ui.comboBox.setCurrentIndex(ui.comboBox.findText(query.value(0)))
            ui.spinBox.setValue(query.value(1))
            db.close()
        except Exception:
            QtWidgets.QMessageBox.warning(window,'Warning',f"Room with Number: {ui.lineEdit.text()} was not found", QtWidgets.QMessageBox.NoButton)
            if ui.comboBox.currentText() != '':
                ui.lineEdit.clear()
                ui.spinBox.setValue(0)