from PySide6.QtWidgets import QStackedWidget


class WindowManager:  # TODO implement in further story
    """Used to control what is displayed in the main window"""

    def __init__(self, menuToWindowMap: dict, centralWidgetContainer: QStackedWidget):
        self.__menuWindowMap = menuToWindowMap
        self.__centralWidgetContainer = centralWidgetContainer

    def change_window(self, menuItemInde: int):
        pass
