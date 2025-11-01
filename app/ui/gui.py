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
    QGridLayout,
    QStackedLayout,
    QWidget,
    QLabel,
    QPushButton,
    QRadioButton,
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
            # Resolusi desktop
            self.setMinimumSize(600, 400)
            # Resolusi mobile
            # self.setMinimumSize(720, 1280)

            layout_vbox = QVBoxLayout()
            layout_content_hbox = QHBoxLayout()
            self.layout_stack = QStackedLayout()

            layout_vbox.addLayout(self.layout_stack)
            layout_vbox.addLayout(layout_content_hbox)

            button = QPushButton("Accounts")
            button.pressed.connect(self.accounts_tab)
            layout_content_hbox.addWidget(button)
            self.layout_stack.addWidget(GuiApp.AccountsTab())

            button = QPushButton("Settings")
            button.pressed.connect(self.settings_tab)
            layout_content_hbox.addWidget(button)
            self.layout_stack.addWidget(GuiApp.SettingsTab())

            container = QWidget()
            container.setLayout(layout_vbox)

            self.setCentralWidget(container)

        def accounts_tab(self):
            self.layout_stack.setCurrentIndex(0)

        def settings_tab(self):
            self.layout_stack.setCurrentIndex(1)

    class AccountsTab(QWidget):
        def __init__(self):
            super().__init__()

            top_bar = GuiApp.TopBar()
            content = GuiApp.Content()
            # bottom_bar = GuiApp.BottomBar()

            layout = QVBoxLayout()
            layout.addWidget(top_bar)
            layout.addWidget(content)
            # layout.addWidget(bottom_bar)

            self.setLayout(layout)

    class SettingsTab(QWidget):
        def __init__(self):
            super().__init__()

            # bottom_bar = GuiApp.BottomBar()

            theme = QLabel("Theme:")
            system_default = QRadioButton("System default")
            light = QRadioButton("Light")
            dark = QRadioButton("Dark")

            layout_vbox = QVBoxLayout()
            layout_theme = QHBoxLayout()

            layout_theme.addWidget(theme)
            layout_theme.addWidget(system_default)
            layout_theme.addWidget(light)
            layout_theme.addWidget(dark)

            layout_vbox.addLayout(layout_theme)
            # layout_vbox.addWidget(bottom_bar)

            self.setLayout(layout_vbox)

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

            export_import = QPushButton("Export/Import")

            layout = QHBoxLayout()
            layout.addWidget(image)
            layout.addWidget(search)
            layout.addWidget(export_import)

            self.setLayout(layout)

    class Content(QWidget):
        def __init__(self):
            super().__init__()

            button_add_password = QPushButton("Add password")

            # contoh
            button_github = QPushButton("Github")
            button_google = QPushButton("Google")
            button_spotify = QPushButton("Spotify")
            button_steam = QPushButton("Steam")
            button_instagram = QPushButton("Instagram")
            button_discord = QPushButton("Discord")

            layout_vbox = QVBoxLayout()
            layout_vbox.addWidget(button_add_password)

            layout_grid = QGridLayout()
            layout_grid.addWidget(button_github, 0, 0)
            layout_grid.addWidget(button_google, 0, 1)
            layout_grid.addWidget(button_spotify, 0, 2)
            layout_grid.addWidget(button_steam, 1, 0)
            layout_grid.addWidget(button_instagram, 1, 1)
            layout_grid.addWidget(button_discord, 1, 2)

            layout_vbox.addLayout(layout_grid)

            self.setLayout(layout_vbox)

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
            button_accounts.setFixedSize(72, 36)

            label_accounts = QLabel("Accounts")
            label_accounts.setAlignment(Qt.AlignHCenter)

            button_settings = QPushButton()
            button_settings.setIcon(image_settings_path)
            button_settings.setIconSize(QSize(24, 24))
            button_settings.setFixedSize(72, 36)

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
            layout.setAlignment(Qt.AlignCenter)

            self.setLayout(layout)

    def run(self):
        app = QApplication([])

        mainWindow = self.MainWindow()
        mainWindow.show()

        app.exec()
