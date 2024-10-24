from PyQt6.QtWidgets import QApplication
from window import MainWindow
import sys
    
if __name__ == '__main__':
    # app instance (once per app)
    app = QApplication([])

    # window instance
    # .show() -> windows hidden by default
    window = MainWindow()
    window.show()

    try:
        # event loop
        sys.exit(app.exec())
    except SystemExit:
        print("Closing window..")        
