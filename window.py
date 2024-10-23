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
    QListWidget
)

from influxdb import create_db, generate_data, delete_db
from influxdb import get_buckets
from task import get_tasks, create_task_preset

# inherit QMainWindow
class MainWindow(QMainWindow):
    # Static properties:
    # GET: all current buckets
    bucket_list = get_buckets()  

    # GET: all current tasks - active or inactive
    task_list = get_tasks()

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

        # task info:
        task_content_layout = QVBoxLayout()
        task_preset_left = QVBoxLayout()
        task_preset_right = QVBoxLayout()
        task_preset_layout = QHBoxLayout()

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
        self.create_btn = QPushButton("create")
        self.create_btn.clicked.connect(self.on_create)

        # bucket list (dropdown):
        self.bucket_choice_label = QLabel("Bucket list: ")
        self.bucket_choice = QComboBox()
        self.bucket_choice.addItems(MainWindow.bucket_list)
        
        # bucket delete button:
        self.bucket_del_btn = QPushButton("delete")
        self.bucket_del_btn.clicked.connect(self.on_delete)
        
        # data generation:
        self.gen_data_label = QLabel("Data Generation")
        self.bucket_choice_gen_label = QLabel("Choose bucket to generate data for: ")
        self.bucket_choice_gen = QComboBox()
        self.bucket_choice_gen.addItems(MainWindow.bucket_list)

        self.row_amount_label = QLabel("Number of data rows you want to generate")
        self.row_amount = QSpinBox()
        self.generate_btn = QPushButton("generate")
        self.generate_btn.clicked.connect(self.on_generate)

        # tasks:
        self.task_list_label = QLabel("Current tasks")
        self.task_list_active = QListWidget()
        self.task_list_active.addItems(
            f"{x.name} \t-\t {x.status}" for x in MainWindow.task_list)
        self.task_list_active.setMaximumHeight(80)

        self.task_preset_label = QLabel("Task presets")
        self.task_preset_choice = QComboBox()
        self.task_preset_choice.addItems(["Aggregate"])

        self.from_bucket_label = QLabel("from bucket")
        self.from_bucket_choice = QComboBox()
        self.from_bucket_choice.addItems(MainWindow.bucket_list)
        self.to_bucket_label = QLabel("to bucket")
        self.to_bucket_choice = QComboBox()
        self.to_bucket_choice.addItems(MainWindow.bucket_list)
        
        self.task_preset_btn = QPushButton("Create preset task")
        self.task_preset_btn.clicked.connect(self.on_create_preset)

        self.flux_query_label = QLabel("Flux query")
        self.flux_query_window = QTextEdit()
        self.flux_query_window.setPlaceholderText("define your flux query task here")


        ##################
        # LAYOUT DEFINES #
        ##################

        # bucket tab:
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
        
        gen_content_layout.addWidget(self.row_amount_label)
        gen_content_layout.addWidget(self.row_amount)
        gen_content_layout.addWidget(self.generate_btn)
        
        # task tab:
        task_content_layout.addWidget(self.task_list_label)
        task_content_layout.addWidget(self.task_list_active)
        task_content_layout.addWidget(self.task_preset_label)
        task_content_layout.addWidget(self.task_preset_choice)

        task_preset_left.addWidget(self.from_bucket_label)
        task_preset_left.addWidget(self.from_bucket_choice)

        task_preset_right.addWidget(self.to_bucket_label)
        task_preset_right.addWidget(self.to_bucket_choice)

        task_preset_layout.addLayout(task_preset_left)
        task_preset_layout.addLayout(task_preset_right)

        task_content_layout.addLayout(task_preset_layout)
        task_content_layout.addWidget(self.task_preset_btn)

        task_content_layout.addWidget(self.flux_query_label)
        task_content_layout.addWidget(self.flux_query_window)
        
        ##############
        # TAB DEFINE #
        ##############

        tab_list = QTabWidget()
        bucket_tab = QWidget()
        generate_tab = QWidget()
        task_tab = QWidget()
        
        bucket_tab.setLayout(bucket_parent_layout)
        generate_tab.setLayout(gen_content_layout)
        task_tab.setLayout(task_content_layout)

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

            # append new bucket in all dropdown menus: 
            last_element = MainWindow.bucket_list[len(MainWindow.bucket_list)-1]
            self.bucket_choice.addItem(last_element)
            self.bucket_choice_gen.addItem(last_element)
        else:
            print("Error: Bucket name can't be left empty.")

    def on_generate(self):
        bucket_name = self.bucket_choice_gen.currentText()
        row_amount = self.row_amount.text()

        # TODO...
        # select preset theme to generate data for:
        preset_data = ''

        print("data generating...")
        sensors = generate_data(bucket_name, row_amount, preset_data)

        if sensors:
            print("Successfully generated dummy data!!")
        else:
            print("Data generation failed.")
    
    def on_delete(self):
        bucket_name = self.bucket_choice.currentText()
        deleted = delete_db(bucket_name)

        if deleted == None:
            print(f"Bucket: \'{bucket_name}\' successfully deleted.")

            # removes currently selected item from all dropdowns:
            idx = self.bucket_choice.currentIndex()
            self.bucket_choice.removeItem(idx)
            self.bucket_choice_gen.removeItem(idx)
        else:
            print("Failed to delete bucket.")

    def on_create_preset(self):
        # chosen task preset:
        task_preset = self.task_preset_choice.currentText()
        
        from_bucket = self.from_bucket_choice.currentText()
        to_bucket = self.to_bucket_choice.currentText()

        if from_bucket == to_bucket:
            print("Can't aggregate into the same bucket.")

        # TODO:
        # add more task preset
        match task_preset:
            case "Aggregate":
                task = create_task_preset(from_bucket, to_bucket)

            case "other":
                pass
            case _:
                pass
        
        if task:
            print("Task preset created!")
        else:
            print("Error: failed to create task.")