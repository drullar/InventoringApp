from PySide6.QtWidgets import QListWidget, QListWidgetItem, QDockWidget


class NavigationMenu(QDockWidget):
    """Navigation menu widget used for switching between the main window central widgets"""

    def __init__(self):
        super().__init__()
        self.__configure()

        self.products_button = QListWidgetItem("Products")
        self.distributors_button = QListWidgetItem("Distributors")

        self.navigationContainer = QListWidget()
        self.setWidget(self.navigationContainer)

        self.navigationContainer.addItem(self.products_button)
        self.navigationContainer.addItem(self.distributors_button)

    def __configure(self):
        self.setWindowTitle("Menu")
        self.setMaximumWidth(MAX_WIDTH)
        self.setMaximumHeight(900)
        self.setFloating(False)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures) # Don't allow the dock to be manually resized/minimized/moved


# Constants
MAX_WIDTH = 300
