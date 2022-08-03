from gui.gui import Ui_MainWindow
from gui.modules.handlers import fill_info
from gui.modules.handlers import on_item_remove


def register_handlers(ui: Ui_MainWindow):
    ui.items_list.currentItemChanged.connect(lambda: fill_info.on_item_click(ui, 'open'))
    ui.items_list.itemDoubleClicked.connect(lambda: fill_info.on_item_click(ui, 'close'))

    ui.delete_item_button.clicked.connect(lambda: on_item_remove.on_rm_click(ui))
