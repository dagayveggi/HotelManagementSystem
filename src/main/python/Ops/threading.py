from PyQt5.QtCore import QRunnable, Qt

class TableWorker(QRunnable):
    def __init__(self, fn):
        super(TableWorker, self).__init__()
        self.fn = fn
    
    def run(self):
        self.fn

def update_table(table, headers, widget, db, model, where=None):
        db.open()
        model.setTable(table)
        if where != None:
            model.setFilter(where)
        num = 0
        for i in headers:
            model.setHeaderData(num, Qt.Horizontal, i)
            num+=1
        model.select()
        while model.canFetchMore():
            model.fetchMore()
        widget.setModel(model)
        widget.horizontalHeader().setStretchLastSection(True)
        db.close()