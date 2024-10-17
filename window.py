from PyQt6.QtWidgets import \
    QMainWindow, QPushButton, QLabel, \
    QWidget, QLineEdit, QSpinBox, \
    QVBoxLayout, QHBoxLayout

from influx import create_db, generate_data

# subclass QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("InfluxDB Interface")

        # bucket label
        self.b_name_label = QLabel("Bucket name")
        self.b_ret_label = QLabel("Bucket retention in days (0 for no expiration)")
        # data label
        self.gen_data_label = QLabel("Generate Data")

        self.bucket = QLineEdit()
        self.bucket.setPlaceholderText("enter name")
        self.retention = QSpinBox()

        self.submit_btn = QPushButton("submit")
        self.submit_btn.clicked.connect(self.on_create)

        self.generate_btn = QPushButton("generate")
        self.generate_btn.clicked.connect(self.on_generate)

        main_layout = QVBoxLayout()
        content_left = QVBoxLayout()
        content_right = QVBoxLayout()
        content_layout = QHBoxLayout()

        content_left.addWidget(self.b_name_label)
        content_left.addWidget(self.bucket)
        content_right.addWidget(self.b_ret_label)
        content_right.addWidget(self.retention)

        content_layout.addLayout(content_left)
        content_layout.addLayout(content_right)

        main_layout.addLayout(content_layout)
        main_layout.addWidget(self.submit_btn)


        # list all buckets from the org,
        # allowing user to select which bucket to generate data for..

        # client = init_connection()
        # buckets_api = client.buckets_api()

        # buckets = buckets_api.find_buckets_iter()
        # print("\n".join([f"\n Name: {bucket.name}" 
        #          for bucket in buckets]))


        #######################################################
        #                                                     #
        # add QSpinBox() to define how many rows to generate? #
        #                                                     #
        #######################################################


        main_layout.addWidget(self.gen_data_label)
        main_layout.addWidget(self.generate_btn)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    def on_create(self):
        bucket_name = self.bucket.text()
        bucket_ret_days = self.retention.text()

        res = create_db(bucket_name, bucket_ret_days)

        if res:
            print(f'Successfully created bucket \'{res.name}\'.')
        else:
            print("Faied to create bucket.")

    def on_generate(self):
        print('data generated...')

        # replace this with selected bucket from drop down list..
        bucket_name = self.bucket.text()

        data = generate_data(bucket_name)