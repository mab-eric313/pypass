"""Modul yang menyediakan kelas dan fungsi GUI PySide6"""


from pathlib import Path

from PySide6.QtCore import (
    Qt,
    QSize,
)

from PySide6.QtGui import (
    QPixmap,
    QIcon,
)

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
)

BASE_PATH = Path(__file__).resolve().parent


class GuiApp:
    def __init__(self):
        pass

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("PyPass")
            self.setMinimumSize(600, 400)

            top_bar = GuiApp.TopBar()
            # content = GuiApp.Content()
            bottom_bar = GuiApp.BottomBar()

            layout = QVBoxLayout()
            layout.addWidget(top_bar)
            # layout.addWidget(content)
            layout.addWidget(bottom_bar)

            container = QWidget()
            container.setLayout(layout)

            self.setCentralWidget(container)

    class TopBar(QWidget):
        def __init__(self):
            super().__init__()

            image_path = QPixmap(str(BASE_PATH / "assets" / "padlock.png"))
            if image_path.isNull():
                print("Error: Image top bar is not found")

            image = QLabel()
            image.setPixmap(image_path)
            image.setScaledContents(True)
            image.setFixedSize(30, 30)

            search = QLineEdit()
            search.setPlaceholderText("Search")
            search.setFixedSize(300, 40)

            layout = QHBoxLayout()
            layout.addWidget(image)
            layout.addWidget(search)

            self.setLayout(layout)

    class Content(QWidget):
        def __init__(self):
            pass

    class BottomBar(QWidget):
        def __init__(self):
            super().__init__()

            image_button_path = QIcon(str(BASE_PATH / "assets" / "key.png"))
            if image_button_path.isNull():
                print("Error: Image button key is not found")

            image_settings_path = QIcon(str(BASE_PATH / "assets" / "gear.png"))
            if image_settings_path.isNull():
                print("Error: Image settings key is not found")

            button_accounts = QPushButton()
            button_accounts.setIcon(image_button_path)
            button_accounts.setIconSize(QSize(24, 24))

            label_accounts = QLabel("Accounts")
            label_accounts.setAlignment(Qt.AlignHCenter)

            button_settings = QPushButton()
            button_settings.setIcon(image_settings_path)
            button_settings.setIconSize(QSize(24, 24))

            label_settings = QLabel("Settings")
            label_settings.setAlignment(Qt.AlignHCenter)

            layout_button_accounts = QVBoxLayout()
            layout_button_accounts.addWidget(button_accounts)
            layout_button_accounts.addWidget(label_accounts)
            layout_button_accounts.setAlignment(Qt.AlignHCenter)

            layout_button_settings = QVBoxLayout()
            layout_button_settings.addWidget(button_settings)
            layout_button_settings.addWidget(label_settings)
            layout_button_accounts.setAlignment(Qt.AlignHCenter)

            layout = QHBoxLayout()
            layout.addLayout(layout_button_accounts)
            layout.addLayout(layout_button_settings)
            layout.setSpacing(40)
            layout.setAlignment(Qt.AlignCenter)

            self.setLayout(layout)

    def run(self):
        app = QApplication([])

        mainWindow = self.MainWindow()
        mainWindow.show()

        app.exec()
