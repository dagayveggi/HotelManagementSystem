from PyQt5.QtCore import QRunnable

class tableWorker(QRunnable):
    def __init__(self, fn):
        super(tableWorker, self).__init__()
        self.fn = fn
    
    def run(self):
        self.fn