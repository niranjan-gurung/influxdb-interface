from PyQt6.QtWidgets import QApplication

from window import MainWindow

# app instance (once per app)
app = QApplication([])

# window instance
# .show() -> windows hidden by default
window = MainWindow()
window.show()

# event loop
app.exec()

# from connect_db import init_connection

# with init_connection() as client:
#     buckets_str = []
#     buckets_api = client.buckets_api()
#     buckets = buckets_api.find_buckets_iter()

#     for bucket in buckets:
#         buckets_str.append(bucket.name)
        
#     print(buckets_str)
#     #return buckets_str