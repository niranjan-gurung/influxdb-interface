from PyQt6.QtWidgets import QMainWindow

from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt

from package.influxdb import (get_buckets, create_db, generate_data, delete_db)
from package.task import (get_tasks, create_task_preset, update_task)
from package.models.bucket_model import BucketModel 

from package.ui.ui_window import Ui_MainWindow

# inherit QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # load ui Qt designer file:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("InfluxDB Interface")
        self.sizePolicy()

        # GET: all current buckets
        buckets = get_buckets()  

        # GET: all current tasks - active or inactive
        tasks = get_tasks()

        # extract name properties from bucket list object:
        self.bucket_names = [bucket.name for bucket in buckets]

        # models
        self.bucket_model = BucketModel(self.bucket_names)
        self.task_model = QStandardItemModel()

        # task preset (only 1 atm):
        self.ui.task_preset_choice.addItems(["Aggregate"])

        # setup view models:
        self.ui.bucket_create_view.setModel(self.bucket_model)
        self.ui.bucket_gen_view.setModel(self.bucket_model)
        self.ui.from_bucket_choice.setModel(self.bucket_model)
        self.ui.to_bucket_choice.setModel(self.bucket_model)
        self.ui.task_view.setModel(self.task_model)

        # signals:
        self.ui.create_btn.clicked.connect(self.on_create)              # create bucket
        self.ui.bucket_del_btn.clicked.connect(self.on_delete)          # delete bucket
        self.ui.generate_btn.clicked.connect(self.on_generate)          # gen data

        self.ui.task_preset_btn.clicked.connect(self.on_task_create)    # create task
        self.ui.task_view.clicked.connect(
            lambda index: self.on_task_toggled(index, tasks))           # toggle task

        # init task model:
        for task in tasks:
            task_info = self.__new_task_model(task)
            self.task_model.appendRow(task_info)

    # private method.
    # setup any new task being created
    # gets added to task model: 
    def __new_task_model(self, task):
        task_info = f"{task.name}\t-\t{task.status}"
        item = QStandardItem(task_info)
        item.setEditable(False)
        item.setCheckable(True)

        if task.status == "active":
            item.setCheckState(Qt.CheckState.Checked)
        else:
            item.setCheckState(Qt.CheckState.Unchecked)
        
        return item

    # slots:
    def on_create(self):
        bucket_name = self.ui.bucket_name.text()
        bucket_ret_days = self.ui.retention.text()
        bucket = create_db(bucket_name, bucket_ret_days)

        if bucket:
            # update the bucket lists after inserting:
            self.bucket_model.insertRow(bucket.name)
            self.bucket_model.layoutChanged.emit()
            self.ui.bucket_name.setText("")

            print(f"Successfully created bucket \'{bucket.name}\'.")
        else:
            print("Error: Bucket name can't be left empty.")

    def on_generate(self):
        bucket_name = self.ui.bucket_gen_view.currentText()
        row_amount = self.ui.row_amount.text()

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
        bucket_name = self.ui.bucket_create_view.currentText()
        deleted = delete_db(bucket_name)

        if deleted == None:
            # update the bucket lists after removing:
            idx = self.ui.bucket_create_view.currentIndex()
            self.bucket_model.removeRow(idx)
            self.bucket_model.layoutChanged.emit()
            
            print(f"Bucket: \'{bucket_name}\' successfully deleted.")
        else:
            print("Failed to delete bucket.")

    def on_task_create(self):
        # chosen task preset:
        task_preset = self.ui.task_preset_choice.currentText()
        from_bucket = self.ui.from_bucket_choice.currentText()
        to_bucket = self.ui.to_bucket_choice.currentText()

        if from_bucket == to_bucket:
            print("Can't aggregate into the same bucket.")
            return -1

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
            task_info = self.__new_task_model(task)
            self.task_model.appendRow(task_info)
            self.task_model.layoutChanged.emit()

            print("Task preset created!")
        else:
            print("Error: failed to create task.")

    # current issues:
    # duplication in task check status..
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
        
        # # update existing item's status: 
        item = QStandardItem(task_info)

        # introduces slight delay when toggling checkbox:
        updated_status = update_task(task)

        if updated_status:
            self.task_model.setData(index, item.text())
            self.task_model.layoutChanged.emit()
            print(f"Task toggled - Status: {task.status}")
        else:
            print("Error: Toggle failed.")