from gui.gui import Ui_MainWindow
from data import common
from gui.modules.core import items_list
from modules.database import Database
from modules.database.model import Item


def fill_type_box(ui: Ui_MainWindow):
    if ui.edit_box_item_class.currentText() == "Vehicle":
        ui.edit_box_item_type.clear()
        ui.edit_box_item_type.addItems(common.vehicle_type)
    elif ui.edit_box_item_class.currentText() == "Property":
        ui.edit_box_item_type.clear()
        ui.edit_box_item_type.addItems(common.property_type)
    else:
        ui.edit_box_item_type.clear()
        ui.edit_box_item_type.addItem("Other")


def on_edit_item_click(ui: Ui_MainWindow):
    item_to_edit_name = items_list.selected_item(ui)

    if not item_to_edit_name:
        return

    item_to_edit = Database.get().items[item_to_edit_name]

    ui.edit_old_item_name.setText(item_to_edit_name)

    ui.edit_box_item_name.setText(item_to_edit.item_name)
    ui.edit_box_price.setValue(item_to_edit.price)
    ui.edit_box_item_class.addItems(common.items_class)
    ui.edit_box_item_class.setCurrentText(item_to_edit.item_class)
    ui.edit_box_item_type.addItem("Other")
    ui.edit_box_item_type.addItem(item_to_edit.item_type)
    ui.edit_box_item_type.setCurrentText(item_to_edit.item_type)
    ui.edit_box_shop.addItems(common.shop_sites)
    ui.edit_box_shop.setCurrentText(item_to_edit.shop)
    ui.edit_box_image.setText(item_to_edit.image)

    ui.content.setCurrentWidget(ui.edit_item_page)


def on_save_edit(ui: Ui_MainWindow):
    if {"", 0} & {ui.edit_box_item_name.text(), ui.edit_box_price.value()}:
        return

    db = Database.get()
    db.items[ui.edit_box_item_name.text()] = Item(
        ui.edit_box_item_name.text(),
        ui.edit_box_item_class.currentText(),
        ui.edit_box_item_type.currentText(),
        ui.edit_box_shop.currentText(),
        ui.edit_box_price.value(),
        ui.edit_box_image.text() if ui.edit_box_image.text() != "" else None
    )

    if ui.edit_box_item_name.text() != ui.edit_old_item_name.text():
        db.items.pop(ui.edit_old_item_name.text())

    Database.write(db)

    ui.content.setCurrentWidget(ui.main_page)
    items_list.refill_list(ui)
