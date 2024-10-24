from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import (
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QWidget, 
    QLineEdit, 
    QTextEdit,
    QSpinBox, 
    QVBoxLayout, 
    QHBoxLayout, 
    QComboBox,
    QTabWidget,
    QListWidget,
    QListWidgetItem,
    QListView,
)

from PyQt6.QtCore import Qt, QAbstractListModel, QStringListModel
from PyQt6.QtGui import QStandardItem, QStandardItemModel

from models import BucketModel

from influxdb import create_db, generate_data, delete_db
from influxdb import get_buckets
from task import get_tasks, create_task_preset, update_task

# inherit QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("InfluxDB Interface")

        buckets = get_buckets()
        tasks = get_tasks()
        
        layout = QVBoxLayout()

        # bucket:
        self.b_name_label = QLabel("Bucket name")
        self.bucket = QLineEdit()
        self.bucket.setPlaceholderText("enter name")
        self.bucket_btn = QPushButton("create")
        self.bucket_btn.clicked.connect(self.create_bucket)

        # # models
        # self.bucket_model = BucketModel(buckets)
        # self.task_model = QStandardItemModel()

        # # views        
        # self.bucket_view = QListView()
        # self.task_view = QComboBox()

        # for task in tasks:
        #     item = QStandardItem(task.name)
        #     self.task_model.appendRow(item)
        #     self.task_view.addItem(str(item))

        # # bind models + views
        # self.bucket_view.setModel(self.bucket_model)
        # self.task_view.setModel(self.task_model)

        # layout.addWidget(self.bucket_view)
        # layout.addWidget(self.task_view)

        layout.addWidget(self.b_name_label)
        layout.addWidget(self.bucket)
        layout.addWidget(self.bucket_btn)

        main = QWidget()
        main.setLayout(layout)

        self.setCentralWidget(main)
    
    def create_bucket(self):
        text = self.bucket.text()
        print(text)