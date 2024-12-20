from PyQt6.QtCore import (
    Qt, 
    QAbstractListModel, 
    QModelIndex, 
    pyqtSlot
)

class BucketModel(QAbstractListModel):
    def __init__(self, buckets = None):
        super(BucketModel, self).__init__()
        self.buckets = buckets or []

    # return data at the current given index:
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.buckets[index.row()]
    
    # return size of bucket
    def rowCount(self, parent=QModelIndex()):
        return len(self.buckets)
    
    @pyqtSlot(str)
    def insertRow(self, name):
        print('adding...')
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.buckets.append(name)
        self.endInsertRows()
        return True
    
    @pyqtSlot(int)
    def removeRow(self, row):
        print('removing..')
        self.beginRemoveRows(QModelIndex(), row, row)
        del self.buckets[row]
        self.endRemoveRows()
        return True