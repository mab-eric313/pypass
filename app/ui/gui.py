"""Modul yang menyediakan kelas dan fungsi GUI PySide6"""


from PySide6.QtCore import (
    Qt
)

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
)


class GuiApp:
    def __init__(self):
        pass

    class Window(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("PyPass")
            self.setMinimumSize(800, 600)

    def run(self):
        app = QApplication([])

        window = self.Window()
        window.show()

        app.exec()
