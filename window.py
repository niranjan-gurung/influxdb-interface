from PyQt6.QtWidgets import (
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QWidget, 
    QLineEdit, 
    QSpinBox, 
    QVBoxLayout, 
    QHBoxLayout, 
    QComboBox,
    QTabWidget,
)

from influx import create_db, generate_data, delete_db
from influx import list_buckets

# subclass QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("InfluxDB Interface")
        
        ##################
        # LAYOUT SCHEMA  #
        ##################

        # bucket create/delete info:
        bucket_parent_layout = QVBoxLayout()
        b_content_left = QVBoxLayout()
        b_content_right = QVBoxLayout()
        b_create_layout = QHBoxLayout()
        b_delete_layout = QVBoxLayout()

        # data gen info:
        gen_content_layout = QVBoxLayout()

        # task info (TODO):
        task_content_layout = QVBoxLayout()

        ##################
        # LABELS DEFINES #
        ##################

        # GET: all buckets from current org's database
        bucket_list = list_buckets()      

        # bucket:
        self.b_name_label = QLabel("Bucket name")
        self.bucket = QLineEdit()
        self.bucket.setPlaceholderText("enter name")

        # bucket retention:
        self.b_ret_label = QLabel("Bucket retention in days (0 for no expiration)")
        self.retention = QSpinBox()
        
        # bucket submit:
        self.create_btn = QPushButton("create")
        self.create_btn.clicked.connect(self.on_create)

        # bucket list (dropdown):
        self.bucket_choice_label = QLabel("Bucket list: ")
        self.bucket_choice = QComboBox()
        self.bucket_choice.addItems(bucket_list)
        
        # bucket delete button:
        self.bucket_del_btn = QPushButton("delete")
        self.bucket_del_btn.clicked.connect(self.on_delete)
        
        # data generation:
        self.gen_data_label = QLabel("Data Generation")
        self.bucket_choice_gen_label = QLabel("Choose bucket to generate data for: ")
        self.bucket_choice_gen = QComboBox()
        self.bucket_choice_gen.addItems(bucket_list)

        self.data_theme_label = QLabel("Pick preset data theme (default is 'sensor'): ")
        self.data_theme_choice = QComboBox()
        self.data_theme_choice.addItems(["sensor", "Country", "..."])

        self.row_amount_label = QLabel("Number of data rows you want to generate")
        self.row_amount = QSpinBox()
        self.generate_btn = QPushButton("generate")
        self.generate_btn.clicked.connect(self.on_generate)


        ##################
        # LAYOUT DEFINES #
        ##################

        # bucket page:
        b_content_left.addWidget(self.b_name_label)
        b_content_left.addWidget(self.bucket)
        b_content_right.addWidget(self.b_ret_label)
        b_content_right.addWidget(self.retention)

        b_create_layout.addLayout(b_content_left)
        b_create_layout.addLayout(b_content_right)

        bucket_parent_layout.addLayout(b_create_layout)
        bucket_parent_layout.addWidget(self.create_btn)
        
        b_delete_layout.addWidget(self.bucket_choice_label)
        b_delete_layout.addWidget(self.bucket_choice)
        b_delete_layout.addWidget(self.bucket_del_btn)

        bucket_parent_layout.addLayout(b_delete_layout)

        # generate tab:
        gen_content_layout.addWidget(self.gen_data_label)
        gen_content_layout.addWidget(self.bucket_choice_gen_label)
        gen_content_layout.addWidget(self.bucket_choice_gen)
        
        gen_content_layout.addWidget(self.data_theme_label)
        gen_content_layout.addWidget(self.data_theme_choice)

        gen_content_layout.addWidget(self.row_amount_label)
        gen_content_layout.addWidget(self.row_amount)
        gen_content_layout.addWidget(self.generate_btn)
        
        
        ##############
        # TAB DEFINE #
        ##############

        tab_list = QTabWidget()
        bucket_tab = QWidget()
        generate_tab = QWidget()
        task_tab = QWidget()
        
        bucket_tab.setLayout(bucket_parent_layout)
        generate_tab.setLayout(gen_content_layout)

        tab_list.addTab(bucket_tab, "Bucket")
        tab_list.addTab(generate_tab, "Generate")
        tab_list.addTab(task_tab, "Tasks")

        self.setCentralWidget(tab_list)

    def on_create(self):
        bucket_name = self.bucket.text()
        bucket_ret_days = self.retention.text()

        bucket = create_db(bucket_name, bucket_ret_days)

        # MAKE THIS INTO A POP UP???? #
        if bucket:
            print(f"Successfully created bucket \'{bucket.name}\'.")

            # append new bucket in dropdown menu: 
            bucket_list = list_buckets()       
            self.bucket_choice.addItem(bucket_list[len(bucket_list)-1])
        else:
            print("Error: Bucket name can't be left empty.")

    def on_generate(self):
        bucket_name = self.bucket_choice.currentText()
        row_amount = self.row_amount.text()
        
        print("data generating...")
        sensors = generate_data(bucket_name, row_amount)

        if sensors:
            print("Successfully generated dummy data!!")
        else:
            print("Data generation failed.")
    
    def on_delete(self):
        bucket_name = self.bucket_choice.currentText()
        deleted = delete_db(bucket_name)

        if deleted == None:
            print(f"Bucket: \'{bucket_name}\' successfully deleted.")

            # removes currently selected item from ComboBox:
            idx = self.bucket_choice.currentIndex()
            self.bucket_choice.removeItem(idx)
        else:
            print("Failed to delete bucket.")
            