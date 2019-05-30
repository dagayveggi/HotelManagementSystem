from PyQt5.QtCore import QRunnable, Qt

class tableWorker(QRunnable):
    def __init__(self, fn):
        super(tableWorker, self).__init__()
        self.fn = fn
    
    def run(self):
        self.fn

def update_table(table, headers, ui, db, model):
        db.open()
        model.setTable(table)
        num = 0
        for i in headers:
            model.setHeaderData(num, Qt.Horizontal, i)
            num+=1
        model.select()
        ui.tableView.setModel(model)
        db.close()