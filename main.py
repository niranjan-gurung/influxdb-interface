from PyQt6.QtWidgets import QApplication

from window import MainWindow

#bucket_name = input('Enter bucket name: ')
#bucket_ret_days = input('Enter retention policy (days): ')

# app instance (once per app)
app = QApplication([])

# window instance
# .show() -> windows hidden by default
window = MainWindow()
window.show()

# event loop
app.exec()
