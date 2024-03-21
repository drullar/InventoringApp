from PySide6 import QtWidgets
import sys
from ui.AppWindow import AppWindow


def main():
    app = QtWidgets.QApplication()
    app_window = AppWindow()
    app_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
