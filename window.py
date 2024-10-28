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
    QListView,
)

from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt
from models import BucketModel

from influxdb import create_db, generate_data, delete_db
from influxdb import get_buckets
from task import get_tasks, create_task_preset, update_task

# inherit QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("InfluxDB Interface")

        # GET: all current buckets
        buckets = get_buckets()  

        # GET: all current tasks - active or inactive
        tasks = get_tasks()

        # extract name properties from bucket list object:
        self.bucket_names = [bucket.name for bucket in buckets]

        # models
        self.bucket_model = BucketModel(self.bucket_names)
        self.task_model = QStandardItemModel()

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

        # bucket list (dropdown):
        self.bucket_choice_label = QLabel("Bucket list: ")
        self.bucket_create_view = QComboBox()
        
        # bucket delete button:
        self.bucket_del_btn = QPushButton("delete")
        
        # data generation:
        self.gen_data_label = QLabel("Data Generation")
        self.bucket_choice_gen_label = QLabel("Choose bucket to generate data for: ")
        self.bucket_gen_view = QComboBox()

        self.row_amount_label = QLabel("Number of data rows you want to generate")
        self.row_amount = QSpinBox()
        self.generate_btn = QPushButton("generate")
        
        # tasks:
        self.task_list_label = QLabel("Current tasks")
        self.task_view = QListView()

        self.task_preset_label = QLabel("Task presets")
        self.task_preset_choice = QComboBox()
        self.task_preset_choice.addItems(["Aggregate"])

        self.from_bucket_label = QLabel("from bucket")
        self.from_bucket_choice = QComboBox()
        self.to_bucket_label = QLabel("to bucket")
        self.to_bucket_choice = QComboBox()
        
        self.task_preset_btn = QPushButton("Create preset task")
        
        # init task model:
        for task in tasks:
            task_info = f"{task.name}\t-\t{task.status}"
            item = QStandardItem(task_info)
            item.setEditable(False)
            item.setCheckable(True)
            if task.status == "active":
                item.setCheckState(Qt.CheckState.Checked)
            else:
                item.setCheckState(Qt.CheckState.Unchecked)

            self.task_model.appendRow(item)
        self.task_view.setMaximumHeight(80)
        
        # setup view models:
        self.bucket_create_view.setModel(self.bucket_model)
        self.bucket_gen_view.setModel(self.bucket_model)
        self.from_bucket_choice.setModel(self.bucket_model)
        self.to_bucket_choice.setModel(self.bucket_model)
        self.task_view.setModel(self.task_model)

        # signals:
        self.create_btn.clicked.connect(self.on_create)             # create bucket
        self.bucket_del_btn.clicked.connect(self.on_delete)         # delete bucket
        self.generate_btn.clicked.connect(self.on_generate)         # gen data

        self.task_preset_btn.clicked.connect(self.on_task_create)   # create task
        self.task_view.clicked.connect(
            lambda index: self.on_task_toggled(index, tasks))       # toggle task

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
        b_delete_layout.addWidget(self.bucket_create_view)
        b_delete_layout.addWidget(self.bucket_del_btn)

        bucket_parent_layout.addLayout(b_delete_layout)

        # generate tab:
        gen_content_layout.addWidget(self.gen_data_label)
        gen_content_layout.addWidget(self.bucket_choice_gen_label)
        gen_content_layout.addWidget(self.bucket_gen_view)
        
        gen_content_layout.addWidget(self.row_amount_label)
        gen_content_layout.addWidget(self.row_amount)
        gen_content_layout.addWidget(self.generate_btn)
        
        # task tab:
        task_content_layout.addWidget(self.task_list_label)
        task_content_layout.addWidget(self.task_view)
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

        if bucket:
            # update the bucket lists after inserting:
            self.bucket_model.insertRow(bucket.name)
            self.bucket_model.layoutChanged.emit()
            self.bucket.setText("")

            print(f"Successfully created bucket \'{bucket.name}\'.")
        else:
            print("Error: Bucket name can't be left empty.")

    def on_generate(self):
        bucket_name = self.bucket_gen_view.currentText()
        row_amount = self.row_amount.text()

        # TODO...
        # select preset theme to generate data for:
        preset_data = ''

        print("data generating...")
        data = generate_data(bucket_name, row_amount, preset_data)

        if data:
            print("Successfully generated dummy data!!")
        else:
            print("Data generation failed.")

    def on_delete(self):
        bucket_name = self.bucket_create_view.currentText()
        deleted = delete_db(bucket_name)

        if deleted == None:
            # update the bucket lists after removing:
            idx = self.bucket_create_view.currentIndex()
            self.bucket_model.removeRow(idx)
            self.bucket_model.layoutChanged.emit()
            
            print(f"Bucket: \'{bucket_name}\' successfully deleted.")
        else:
            print("Failed to delete bucket.")

    def on_task_create(self):
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
                task = create_task_preset(from_bucket, to_bucket, task_preset)

            case "other":
                pass
            case _:
                pass
        
        if task:
            item = QStandardItem(task.name)
            self.task_model.appendRow(item)
            self.task_model.layoutChanged.emit()

            print("Task preset created!")
        else:
            print("Error: failed to create task.")

    def on_task_toggled(self, index, tasks):
        item = self.task_model.itemFromIndex(index)
        values = item.text().split("\t")

        name = values[0]
        checked = item.checkState() is Qt.CheckState.Checked

        for task in tasks:
            matched = name == task.name
            if matched:
                break

        # how am I accessing task outside of for loop..
        if checked:
            task.status = "active"
        else:
            task.status = "inactive"

        task_info = f"{task.name}\t-\t{task.status}"

        # introduces slight delay when toggling checkbox:
        updated_status = update_task(task)

        if updated_status:
            self.task_model.setData(index, task_info)
            self.task_model.layoutChanged.emit()
            print(f"Task toggled - Status: {task.status}")
        else:
            print("Error: Toggle failed.")