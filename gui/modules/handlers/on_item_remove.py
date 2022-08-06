from gui.gui import Ui_MainWindow
from modules.database import Database
from gui.modules.core import items_list
from gui.modules.filters.menu import refill_filters


def on_rm_click(ui: Ui_MainWindow):
    from gui.modules.handlers import fill_info
    if ui.items_list.currentItem():
        Database.remove_item(
            ui.items_list.currentItem().text().removesuffix(' - ' + ui.items_list.currentItem().text().split(' - ')[-1])
        )
        items_list.refill_list(ui)
        refill_filters(ui)
        fill_info.on_item_click(ui, 'close')
