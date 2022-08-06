from gui.gui import Ui_MainWindow
from gui.modules.handlers import fill_info
from gui.modules.handlers import on_item_remove
from gui.modules.adding_item import on_add_click
from gui.modules.filters import menu


def register_handlers(ui: Ui_MainWindow):
    ui.items_list.currentItemChanged.connect(lambda: fill_info.on_item_click(ui, 'open'))
    ui.items_list.itemDoubleClicked.connect(lambda: fill_info.on_item_click(ui, 'close'))

    ui.delete_item_button.clicked.connect(lambda: on_item_remove.on_rm_click(ui))

    ui.add_item_button.clicked.connect(lambda: on_add_click.on_add_button_click(ui))

    ui.open_filter_button.clicked.connect(lambda: menu.on_open_close_click(ui))

    ui.filter_class_box.currentIndexChanged.connect(lambda: menu.refill_types(ui))

    on_add_click.register_add_handlers(ui)
