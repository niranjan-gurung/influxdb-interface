# Form implementation generated from reading ui file 'ui_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 411)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 411, 381))
        self.tabs.setObjectName("tabs")
        self.Bucket = QtWidgets.QWidget()
        self.Bucket.setObjectName("Bucket")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(parent=self.Bucket)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 0, 381, 345))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.buckets_container = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.buckets_container.setContentsMargins(0, 0, 0, 0)
        self.buckets_container.setObjectName("buckets_container")
        self.bucket_container = QtWidgets.QVBoxLayout()
        self.bucket_container.setObjectName("bucket_container")
        self.bucket_parent_layout = QtWidgets.QVBoxLayout()
        self.bucket_parent_layout.setSpacing(6)
        self.bucket_parent_layout.setObjectName("bucket_parent_layout")
        self.b_create_layout = QtWidgets.QHBoxLayout()
        self.b_create_layout.setSpacing(6)
        self.b_create_layout.setObjectName("b_create_layout")
        self.b_content_left = QtWidgets.QVBoxLayout()
        self.b_content_left.setObjectName("b_content_left")
        self.b_name_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.b_name_label.setEnabled(True)
        self.b_name_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.b_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.b_name_label.setWordWrap(False)
        self.b_name_label.setObjectName("b_name_label")
        self.b_content_left.addWidget(self.b_name_label)
        self.bucket_name = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_9)
        self.bucket_name.setObjectName("bucket_name")
        self.b_content_left.addWidget(self.bucket_name)
        self.b_create_layout.addLayout(self.b_content_left)
        self.b_content_right = QtWidgets.QVBoxLayout()
        self.b_content_right.setObjectName("b_content_right")
        self.b_name_label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.b_name_label_2.setEnabled(True)
        self.b_name_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.b_name_label_2.setObjectName("b_name_label_2")
        self.b_content_right.addWidget(self.b_name_label_2)
        self.retention = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_9)
        self.retention.setObjectName("retention")
        self.b_content_right.addWidget(self.retention)
        self.b_create_layout.addLayout(self.b_content_right)
        self.bucket_parent_layout.addLayout(self.b_create_layout)
        self.create_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_9)
        self.create_btn.setObjectName("create_btn")
        self.bucket_parent_layout.addWidget(self.create_btn)
        self.b_delete_layout = QtWidgets.QVBoxLayout()
        self.b_delete_layout.setContentsMargins(-1, -1, -1, 0)
        self.b_delete_layout.setSpacing(6)
        self.b_delete_layout.setObjectName("b_delete_layout")
        self.bucket_choice_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.bucket_choice_label.setEnabled(True)
        self.bucket_choice_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bucket_choice_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.bucket_choice_label.setWordWrap(False)
        self.bucket_choice_label.setObjectName("bucket_choice_label")
        self.b_delete_layout.addWidget(self.bucket_choice_label)
        self.bucket_create_view = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.bucket_create_view.setObjectName("bucket_create_view")
        self.b_delete_layout.addWidget(self.bucket_create_view)
        self.bucket_del_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_9)
        self.bucket_del_btn.setObjectName("bucket_del_btn")
        self.b_delete_layout.addWidget(self.bucket_del_btn)
        self.bucket_parent_layout.addLayout(self.b_delete_layout)
        self.bucket_container.addLayout(self.bucket_parent_layout)
        self.buckets_container.addLayout(self.bucket_container)
        self.data_gen_parent_layout = QtWidgets.QVBoxLayout()
        self.data_gen_parent_layout.setObjectName("data_gen_parent_layout")
        self.gen_data_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.gen_data_label.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gen_data_label.setFont(font)
        self.gen_data_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.gen_data_label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.gen_data_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gen_data_label.setWordWrap(False)
        self.gen_data_label.setObjectName("gen_data_label")
        self.data_gen_parent_layout.addWidget(self.gen_data_label)
        self.gen_bucket_choice_layout = QtWidgets.QVBoxLayout()
        self.gen_bucket_choice_layout.setObjectName("gen_bucket_choice_layout")
        self.bucket_choice_gen = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.bucket_choice_gen.setEnabled(True)
        self.bucket_choice_gen.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.bucket_choice_gen.setFont(font)
        self.bucket_choice_gen.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bucket_choice_gen.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.bucket_choice_gen.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.bucket_choice_gen.setWordWrap(False)
        self.bucket_choice_gen.setObjectName("bucket_choice_gen")
        self.gen_bucket_choice_layout.addWidget(self.bucket_choice_gen)
        self.bucket_gen_view = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_9)
        self.bucket_gen_view.setObjectName("bucket_gen_view")
        self.gen_bucket_choice_layout.addWidget(self.bucket_gen_view)
        self.data_gen_parent_layout.addLayout(self.gen_bucket_choice_layout)
        self.gen_row_layout = QtWidgets.QVBoxLayout()
        self.gen_row_layout.setObjectName("gen_row_layout")
        self.row_amount_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_9)
        self.row_amount_label.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.row_amount_label.setFont(font)
        self.row_amount_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.row_amount_label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.row_amount_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.row_amount_label.setWordWrap(False)
        self.row_amount_label.setObjectName("row_amount_label")
        self.gen_row_layout.addWidget(self.row_amount_label)
        self.row_amount = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_9)
        self.row_amount.setObjectName("row_amount")
        self.gen_row_layout.addWidget(self.row_amount)
        self.generate_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_9)
        self.generate_btn.setObjectName("generate_btn")
        self.gen_row_layout.addWidget(self.generate_btn)
        self.data_gen_parent_layout.addLayout(self.gen_row_layout)
        self.buckets_container.addLayout(self.data_gen_parent_layout)
        self.tabs.addTab(self.Bucket, "")
        self.Tasks = QtWidgets.QWidget()
        self.Tasks.setObjectName("Tasks")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(parent=self.Tasks)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(10, 10, 371, 311))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.tasks_container = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.tasks_container.setContentsMargins(0, 0, 0, 0)
        self.tasks_container.setObjectName("tasks_container")
        self.tasks_layout = QtWidgets.QVBoxLayout()
        self.tasks_layout.setObjectName("tasks_layout")
        self.current_tasks_layout = QtWidgets.QVBoxLayout()
        self.current_tasks_layout.setObjectName("current_tasks_layout")
        self.task_view_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_15)
        self.task_view_label.setObjectName("task_view_label")
        self.current_tasks_layout.addWidget(self.task_view_label)
        self.task_view = QtWidgets.QListView(parent=self.verticalLayoutWidget_15)
        self.task_view.setObjectName("task_view")
        self.current_tasks_layout.addWidget(self.task_view)
        self.tasks_layout.addLayout(self.current_tasks_layout)
        self.tasks_container.addLayout(self.tasks_layout)
        self.task_preset_layout = QtWidgets.QVBoxLayout()
        self.task_preset_layout.setObjectName("task_preset_layout")
        self.task_preset_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_15)
        self.task_preset_label.setObjectName("task_preset_label")
        self.task_preset_layout.addWidget(self.task_preset_label)
        self.task_preset_choice = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_15)
        self.task_preset_choice.setObjectName("task_preset_choice")
        self.task_preset_layout.addWidget(self.task_preset_choice)
        self.tasks_container.addLayout(self.task_preset_layout)
        self.create_task_preset_layout = QtWidgets.QVBoxLayout()
        self.create_task_preset_layout.setObjectName("create_task_preset_layout")
        self.bucket_choice_layout = QtWidgets.QHBoxLayout()
        self.bucket_choice_layout.setObjectName("bucket_choice_layout")
        self.to_bucket_layout = QtWidgets.QVBoxLayout()
        self.to_bucket_layout.setObjectName("to_bucket_layout")
        self.to_bucket_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_15)
        self.to_bucket_label.setObjectName("to_bucket_label")
        self.to_bucket_layout.addWidget(self.to_bucket_label)
        self.to_bucket_choice = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_15)
        self.to_bucket_choice.setObjectName("to_bucket_choice")
        self.to_bucket_layout.addWidget(self.to_bucket_choice)
        self.bucket_choice_layout.addLayout(self.to_bucket_layout)
        self.from_bucket_layout = QtWidgets.QVBoxLayout()
        self.from_bucket_layout.setObjectName("from_bucket_layout")
        self.from_bucket_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_15)
        self.from_bucket_label.setObjectName("from_bucket_label")
        self.from_bucket_layout.addWidget(self.from_bucket_label)
        self.from_bucket_choice = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_15)
        self.from_bucket_choice.setObjectName("from_bucket_choice")
        self.from_bucket_layout.addWidget(self.from_bucket_choice)
        self.bucket_choice_layout.addLayout(self.from_bucket_layout)
        self.create_task_preset_layout.addLayout(self.bucket_choice_layout)
        self.task_preset_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_15)
        self.task_preset_btn.setObjectName("task_preset_btn")
        self.create_task_preset_layout.addWidget(self.task_preset_btn)
        self.tasks_container.addLayout(self.create_task_preset_layout)
        self.tabs.addTab(self.Tasks, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_name_label.setText(_translate("MainWindow", "Bucket Name"))
        self.bucket_name.setPlaceholderText(_translate("MainWindow", "enter name"))
        self.b_name_label_2.setText(_translate("MainWindow", "Bucket Retention Days (0 for no expiration)"))
        self.create_btn.setText(_translate("MainWindow", "create"))
        self.bucket_choice_label.setText(_translate("MainWindow", "Bucket List"))
        self.bucket_del_btn.setText(_translate("MainWindow", "delete"))
        self.gen_data_label.setText(_translate("MainWindow", "Data Generation"))
        self.bucket_choice_gen.setText(_translate("MainWindow", "Choose bucket to generate data for"))
        self.row_amount_label.setText(_translate("MainWindow", "Number of data rows to generate"))
        self.generate_btn.setText(_translate("MainWindow", "generate"))
        self.tabs.setTabText(self.tabs.indexOf(self.Bucket), _translate("MainWindow", "Bucket"))
        self.task_view_label.setText(_translate("MainWindow", "Current Tasks"))
        self.task_preset_label.setText(_translate("MainWindow", "Task presets"))
        self.to_bucket_label.setText(_translate("MainWindow", "To bucket"))
        self.from_bucket_label.setText(_translate("MainWindow", "From bucket"))
        self.task_preset_btn.setText(_translate("MainWindow", "Create preset task"))
        self.tabs.setTabText(self.tabs.indexOf(self.Tasks), _translate("MainWindow", "Tasks"))