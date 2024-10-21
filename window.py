from PyQt6.QtWidgets import \
    QMainWindow, QPushButton, QLabel, \
    QWidget, QLineEdit, QSpinBox, \
    QVBoxLayout, QHBoxLayout, QComboBox

from influx import create_db, generate_data, delete_db
from influx import list_buckets

# subclass QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("InfluxDB Interface")


        ##################
        # LAYOUT SCHEMA  #
        ##################

        # parent layout container:
        main_layout = QVBoxLayout()

        # bucket info:
        b_content_left = QVBoxLayout()
        b_content_right = QVBoxLayout()
        b_parent_content_layout = QHBoxLayout()

        # data gen info:
        gen_content_layout = QVBoxLayout()

        ##################
        # LABELS DEFINES #
        ##################

        # bucket:
        self.b_name_label = QLabel("Bucket name")
        self.bucket = QLineEdit()
        self.bucket.setPlaceholderText("enter name")

        # bucket retention:
        self.b_ret_label = QLabel("Bucket retention in days (0 for no expiration)")
        self.retention = QSpinBox()
        
        # bucket submit:
        self.submit_btn = QPushButton("submit")
        self.submit_btn.clicked.connect(self.on_create)

        # data generation:
        self.gen_data_label = QLabel("Generate Data")

        self.bucket_choice_label = QLabel("Choose a bucket to operate on")
        self.bucket_choice = QComboBox()

        # GET: all buckets from current org's database
        # list in combo box:
        bucket_list = list_buckets()       
        self.bucket_choice.addItems(bucket_list)

        # bucket delete
        self.bucket_del_btn = QPushButton("delete")
        self.bucket_del_btn.clicked.connect(self.on_delete)

        self.row_amount_label = QLabel("Number of data rows you want to generate")
        self.row_amount = QSpinBox()
        self.generate_btn = QPushButton("generate")
        self.generate_btn.clicked.connect(self.on_generate)


        ##################
        # LAYOUT DEFINES #
        ##################

        b_content_left.addWidget(self.b_name_label)
        b_content_left.addWidget(self.bucket)
        b_content_right.addWidget(self.b_ret_label)
        b_content_right.addWidget(self.retention)

        b_parent_content_layout.addLayout(b_content_left)
        b_parent_content_layout.addLayout(b_content_right)

        main_layout.addLayout(b_parent_content_layout)
        main_layout.addWidget(self.submit_btn)

        gen_content_layout.addWidget(self.gen_data_label)
        gen_content_layout.addWidget(self.bucket_choice_label)
        gen_content_layout.addWidget(self.bucket_choice)

        gen_content_layout.addWidget(self.bucket_del_btn)

        gen_content_layout.addWidget(self.row_amount_label)
        gen_content_layout.addWidget(self.row_amount)
        gen_content_layout.addWidget(self.generate_btn)

        main_layout.addLayout(gen_content_layout)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    def on_create(self):
        bucket_name = self.bucket.text()
        bucket_ret_days = self.retention.text()

        bucket = create_db(bucket_name, bucket_ret_days)

        if bucket:
            print(f'Successfully created bucket \'{bucket.name}\'.')

            # append new bucket in dropdown menu: 
            bucket_list = list_buckets()       
            self.bucket_choice.addItem(bucket_list[len(bucket_list)-1])
        else:
            print("Faied to create bucket.")

    def on_generate(self):
        bucket_name = self.bucket_choice.currentText()
        row_amount = self.row_amount.text()
        
        print('data generating...')
        sensors = generate_data(bucket_name, row_amount)

        if sensors:
            print('Successfully generated dummy data!!')
        else:
            print('Data generation failed.')
    
    def on_delete(self):
        bucket_name = self.bucket_choice.currentText()
        deleted = delete_db(bucket_name)

        if deleted == None:
            print(f'Bucket: \'{bucket_name}\' successfully deleted.')

            # removes currently selected item from ComboBox:
            idx = self.bucket_choice.currentIndex()
            self.bucket_choice.removeItem(idx)
        else:
            print('Failed to delete bucket.')