from gui.gui import Ui_MainWindow
from gui.modules.core.blur import GlobalBlur
from gui.modules.initialize import styles
from PyQt5.QtWidgets import QMainWindow
from modules.config import Config
from gui.modules.core import items_list
from modules.database import Database
from modules.database.model import Item


def on_load(ui: Ui_MainWindow, MainWindow: QMainWindow):
    ui.logo_if_empty.hide()
    ui.logo_if_empty.setMaximumSize(16777215, 16777215)

    ui.content.setCurrentIndex(0)

    MainWindow.setStyleSheet(styles.centralwidget())
    if 'acrylic' in Config.get().theme:
        GlobalBlur(MainWindow.winId(), acrylic=True)

    items_list.refill_list(ui)
    Database.add_item(Item("aa", "aa", "aa", "aa", 10, "aa"))
