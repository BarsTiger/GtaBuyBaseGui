from modules.database import Database
from modules.database.model import Item
from gui.gui import Ui_MainWindow


def add_item_if_can(ui: Ui_MainWindow):
    if {"", 0} & {ui.new_item_name_box.text(), ui.new_item_price_box.value()}:
        return

    Database.add_item(Item(
        ui.new_item_name_box.text(),
        ui.new_item_class_box.currentText(),
        ui.new_item_type_box.currentText(),
        ui.new_item_shop_box.currentText(),
        ui.new_item_price_box.value(),
        ui.new_item_image_box.text() if ui.new_item_image_box.text() != "" else None
    ))
