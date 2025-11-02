"""Modul yang menyediakan kelas dan fungsi GUI PySide6"""


from pathlib import Path

from PySide6.QtCore import (
    Qt,
    QSize,
    Signal,
)

from PySide6.QtGui import (
    QPixmap,
    QIcon,
)

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QSizePolicy,
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
            # self.setMinimumSize(360, 640)

            self.main_stack = GuiApp.MainStack()
            self.bottom_bar = GuiApp.BottomBar()

            self.bottom_bar.switch_tab.connect(self.main_stack.set_tab)

            layout = QVBoxLayout()
            layout.addWidget(self.main_stack)
            layout.addWidget(self.bottom_bar)

            container = QWidget()
            container.setLayout(layout)

            self.setCentralWidget(container)

    class MainStack(QWidget):
        def __init__(self):
            super().__init__()
            self.stack = QStackedLayout()

            self.accounts_tab = GuiApp.AccountsTab()
            self.settings_tab = GuiApp.SettingsTab()

            self.stack.addWidget(self.accounts_tab)
            self.stack.addWidget(self.settings_tab)

            self.setLayout(self.stack)

        def set_tab(self, index: int):
            self.stack.setCurrentIndex(index)

    class BottomBar(QWidget):
        switch_tab = Signal(int)

        def __init__(self):
            super().__init__()

            icon_accounts = QIcon(str(BASE_PATH / "assets" / "key.png"))
            icon_settings = QIcon(str(BASE_PATH / "assets" / "gear.png"))

            button_accounts = QPushButton()
            button_accounts.setIcon(icon_accounts)
            button_accounts.setIconSize(QSize(24, 24))
            button_accounts.setFixedSize(72, 36)

            label_accounts = QLabel("Accounts", alignment=Qt.AlignHCenter)

            button_settings = QPushButton()
            button_settings.setIcon(icon_settings)
            button_settings.setIconSize(QSize(24, 24))
            button_settings.setFixedSize(72, 36)

            label_settings = QLabel("Settings", alignment=Qt.AlignHCenter)

            layout_button_accounts = QVBoxLayout()
            layout_button_accounts.addWidget(button_accounts)
            layout_button_accounts.addWidget(label_accounts)

            layout_button_settings = QVBoxLayout()
            layout_button_settings.addWidget(button_settings)
            layout_button_settings.addWidget(label_settings)

            layout = QHBoxLayout()
            layout.addLayout(layout_button_accounts)
            layout.addLayout(layout_button_settings)
            layout.setAlignment(Qt.AlignCenter)

            self.setLayout(layout)

            button_accounts.clicked.connect(lambda: self.switch_tab.emit(0))
            button_settings.clicked.connect(lambda: self.switch_tab.emit(1))

    class TopBar(QWidget):
        def __init__(self):
            super().__init__()

            image_path = QPixmap(str(BASE_PATH / "assets" / "padlock.png"))

            image = QLabel()
            image.setPixmap(image_path)
            image.setScaledContents(True)
            image.setFixedSize(30, 30)

            search = QLineEdit()
            search.setPlaceholderText("Search")
            search.setFixedHeight(30)

            layout = QHBoxLayout()
            layout.addWidget(image)
            layout.addWidget(search)
            layout.setSpacing(15)

            self.setLayout(layout)

    class AccountsAddStack(QWidget):
        switch_to_main = Signal()

        def __init__(self):
            super().__init__()

            back = QPushButton("Back to Accounts")
            back.clicked.connect(self.switch_to_main.emit)

            layout = QVBoxLayout()
            layout.addWidget(back)

            self.setLayout(layout)

        def set_tab(self, index: int):
            self.stack.setCurrentIndex(index)

    class AccountsAddContent(QWidget):
        def __init__(self):
            super().__init__()

            back = QPushButton("This button from AccountsAddContent")

            layout = QVBoxLayout()
            layout.addWidget(back)

            self.setLayout(layout)

    class AccountsEditStack(QWidget):
        pass

    class AccountsTab(QWidget):
        def __init__(self):
            super().__init__()

            self.stack = QStackedLayout()

            self.accounts_content = GuiApp.AccountsContent()
            self.accounts_content.switch_to_add.connect(
                lambda: self.stack.setCurrentIndex(1)
            )

            self.accounts_add_stack = GuiApp.AccountsAddStack()
            self.accounts_add_stack.switch_to_main.connect(
                lambda: self.stack.setCurrentIndex(0)
            )

            self.stack.addWidget(self.accounts_content)
            self.stack.addWidget(self.accounts_add_stack)

            self.setLayout(self.stack)

    class AccountsContent(QWidget):
        switch_to_add = Signal()

        def __init__(self):
            super().__init__()

            width = QSizePolicy.Expanding
            height = QSizePolicy.Fixed

            button_add_password = QPushButton("Add password")
            button_add_password.setSizePolicy(width, height)
            button_add_password.setFixedHeight(60)

            button_add_password.clicked.connect(self.switch_to_add.emit)

            # contoh
            button_github = QPushButton("Github")
            button_google = QPushButton("Google")
            button_spotify = QPushButton("Spotify")
            button_steam = QPushButton("Steam")
            button_instagram = QPushButton("Instagram")
            button_discord = QPushButton("Discord")

            layout_vbox = QVBoxLayout()
            layout_vbox.addWidget(GuiApp.TopBar())
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

    class SettingsTab(QWidget):
        def __init__(self):
            super().__init__()

            layout = QVBoxLayout()
            layout.addWidget(GuiApp.SettingsContent())

            self.setLayout(layout)

    class SettingsContent(QWidget):
        def __init__(self):
            super().__init__()

            theme = QLabel("Theme:")
            system_default = QRadioButton("System default")
            light = QRadioButton("Light")
            dark = QRadioButton("Dark")
            export_import = QPushButton("Export/Import")

            layout_vbox = QVBoxLayout()
            layout_theme = QHBoxLayout()

            layout_theme.addWidget(theme)
            layout_theme.addWidget(system_default)
            layout_theme.addWidget(light)
            layout_theme.addWidget(dark)

            layout_vbox.addWidget(export_import)
            layout_vbox.addLayout(layout_theme)

            self.setLayout(layout_vbox)

    def run(self):
        app = QApplication([])

        mainWindow = self.MainWindow()
        mainWindow.show()

        app.exec()
