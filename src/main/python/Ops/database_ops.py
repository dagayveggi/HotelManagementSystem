from PyQt5 import QtWidgets, QtCore
from Ops.threading import TableWorker, update_table
from PyQt5.QtSql import QSqlQuery, QSqlError

#! All functions need revision to maybe find a way to reduce
#! the number parameters used
def add_DB(ui, window, db, table, vlist, placeholderstr, widget_list):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare(f"INSERT INTO {table} VALUES({placeholderstr})")
    for i in vlist:
        query.addBindValue(i)
    try:
        query.exec_()
        db.commit()
        db.close()
        QtWidgets.QMessageBox.information(window, f"New {table} created", 
                                            f"New {table} has been successfully created", 
                                            QtWidgets.QMessageBox.Ok)
    except Exception:
        QtWidgets.QMessageBox.critical(window, 'Error', 
                                            'Something went wrong', 
                                            QtWidgets.QMessageBox.Ok)
    finally:
        for i in widget_list:
            i.clear()

def del_DB(ui, window, db, table, identifier, idvalue, widget_list):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare(f"DELETE FROM {table} WHERE {identifier} = ?")
    query.addBindValue(idvalue)
    try:
        query.exec_()
        db.commit()
        db.close()
        QtWidgets.QMessageBox.information(window, f"{table} deleted", 
                                            f"{table} has been successfully deleted", 
                                            QtWidgets.QMessageBox.Ok)
    except Exception:
        QtWidgets.QMessageBox.critical(window, 'Error', 
                                            'Something went wrong', 
                                            QtWidgets.QMessageBox.Ok)
    finally:
        for i in widget_list:
            i.clear()

def edit_DB(ui, window, db, table, vlist, query_list, ider, widget_list):
    db.open()
    #Prepare a query and add all values then execute and commit to DB
    query = QSqlQuery(db)
    db.transaction()
    query.prepare(f"UPDATE {table} SET {query_list} WHERE {ider} = ?")
    for i in vlist:
        query.addBindValue(i)
    try:
        query.exec_()
        db.commit()
        db.close()
        QtWidgets.QMessageBox.information(window, f"{table} edited", 
                                            f"{table} has been successfully edited", 
                                            QtWidgets.QMessageBox.Ok)
    except Exception:
        QtWidgets.QMessageBox.critical(window, 'Error', 
                                            'Something went wrong', 
                                            QtWidgets.QMessageBox.Ok)
    finally:
        for i in widget_list:
            i.clear()