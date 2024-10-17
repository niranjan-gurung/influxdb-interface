from PyQt6.QtWidgets import \
    QMainWindow, QPushButton, QVBoxLayout, \
    QWidget, QLineEdit, QComboBox

from init_bucket import create

from dotenv import load_dotenv
import os

# influx api token, url, org..
load_dotenv()

url = os.getenv('URL')
token = os.getenv('INFLUX_TOKEN')
org = os.getenv('ORG')

# subclass QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("InfluxDB Interface")
        
        self.dropdown = QComboBox()
        self.dropdown.addItems(["Create", "Generate Data"])

        self.bucket = QLineEdit()
        self.retention = QLineEdit()
        self.bucket.setPlaceholderText("Enter bucket name")
        self.retention.setPlaceholderText("Enter retention (in days)")

        self.button = QPushButton("submit")
        self.button.clicked.connect(self.on_btn_click)

        layout = QVBoxLayout()
        layout.addWidget(self.dropdown)
        layout.addWidget(self.bucket)
        layout.addWidget(self.retention)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def on_btn_click(self):
        bucket_name = self.bucket.text()
        bucket_ret_days = self.retention.text()

        res = create(url, token, org, bucket_name, bucket_ret_days)

        if res:
            print(f'Successfully created bucket {res.name}.')
        else:
            print("Faied to create bucket.")