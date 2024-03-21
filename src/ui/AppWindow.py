from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from ui.configuration.Constants import APP_NAME
from ui.components.NavigationMenu import NavigationMenu


class AppWindow(QMainWindow):

    """The Main App widget. Any widgets that is part of the 'main window' should be direct descendant of this widget or of
    an already nested one"""
    def __init__(self):
        super().__init__()
        self.__set_window_layout()
        self.__set_window_configuration()

    def __set_window_layout(self):
        self.__set_docks()

    def __set_window_configuration(self):
        self.setWindowTitle(APP_NAME)
        self.window().showMaximized()

    def __set_docks(self):
        self.navigation_menu = NavigationMenu()
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.navigation_menu)