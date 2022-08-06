from gui.gui import Ui_MainWindow
from gui.modules.core.blur import GlobalBlur
from gui.modules.initialize import styles
from PyQt5.QtWidgets import QMainWindow
from modules.config import Config
from gui.modules.core import items_list
from gui.modules.handlers.register import register_handlers
from gui.modules.filters.menu import refill_filters


def on_load(ui: Ui_MainWindow, MainWindow: QMainWindow):
    ui.logo_if_empty.hide()
    ui.logo_if_empty.setMaximumSize(16777215, 16777215)

    ui.content.setCurrentIndex(0)

    MainWindow.setStyleSheet(styles.centralwidget())
    if 'acrylic' in Config.get().theme:
        GlobalBlur(MainWindow.winId(), acrylic=True)

    refill_filters(ui)
    items_list.refill_list(ui)

    register_handlers(ui)
