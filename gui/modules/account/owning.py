from gui.gui import Ui_MainWindow
from gui.modules.core import items_list
from modules.database import Database


def on_change_owning_clicked(ui: Ui_MainWindow):
    if items_list.selected_item(ui) not in Database.get_profile().owned_items:
        Database.set_owned(items_list.selected_item(ui))
        ui.own_button.setText("Mark this item as unowned")
        items_list.refill_list(ui)
    else:
        Database.set_unowned(items_list.selected_item(ui))
        ui.own_button.setText("Mark this item as owned")
        items_list.refill_list(ui)
