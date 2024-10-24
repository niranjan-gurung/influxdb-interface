from PyQt6.QtCore import Qt, QAbstractListModel

class BucketModel(QAbstractListModel):
    def __init__(self, buckets = None):
        super(BucketModel, self).__init__()
        self.__buckets = buckets or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.__buckets[index.row()]
    
    def rowCount(self, index):
        return len(self.__buckets)
    
class TaskModel(QAbstractListModel):
    def __init__(self, tasks = None):
        super(TaskModel, self).__init__()
        self.__tasks = tasks or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.__tasks[index.row()]
    
    def rowCount(self, index):
        return len(self.__tasks)