from PyQt6.QtCore import Qt, QAbstractListModel

class BucketModel(QAbstractListModel):
    def __init__(self, buckets = None):
        super(BucketModel, self).__init__()
        self.buckets = buckets or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.buckets[index.row()]
    
    def rowCount(self, index):
        return len(self.buckets)
    
# Not sure if needed (replaced by QStandardItemModel)
# as 'tasks' list is a list of json objects:
class TaskModel(QAbstractListModel):
    def __init__(self, tasks = None):
        super(TaskModel, self).__init__()
        self.tasks = tasks or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.tasks[index.row()]
    
    def rowCount(self, index):
        return len(self.tasks)