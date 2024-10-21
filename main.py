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