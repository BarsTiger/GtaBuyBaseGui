from gui.gui import Ui_MainWindow
from modules.config import Config
from gui.modules.core import items_list


def on_load_another_db_click(ui: Ui_MainWindow):
    Config.update("database", ui.database_list_box.currentText())
    items_list.refill_list(ui)


def register_db_handlers(ui: Ui_MainWindow):
    ui.load_this_db_button.clicked.connect(lambda: on_load_another_db_click(ui))
