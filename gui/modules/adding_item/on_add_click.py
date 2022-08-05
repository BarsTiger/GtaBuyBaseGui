from gui.gui import Ui_MainWindow
from gui.modules.adding_item.write_item import add_item_if_can
from data import common


def on_add_button_click(ui: Ui_MainWindow):
    sender_page = ui.content.currentWidget()

    ui.content.setCurrentWidget(ui.add_page)
    ui.adding_item_main_layout.setCurrentIndex(0)

    ui.new_item_finish_label.setText("Fill all fields first")

    ui.new_item_name_box.clear()
    ui.new_item_price_box.setValue(0)
    ui.new_item_class_box.clear()
    ui.new_item_type_box.clear()
    ui.new_item_type_box.addItem("Other")
    ui.new_item_shop_box.clear()
    ui.new_item_image_box.clear()

    ui.new_item_class_box.addItems(common.items_class)
    ui.new_item_class_box.setCurrentIndex(len(common.items_class) - 1)
    ui.new_item_class_box.currentIndexChanged.connect(
        lambda: (
            ui.new_item_type_box.clear(),
            ui.new_item_type_box.addItems(
                common.vehicle_type if ui.new_item_class_box.currentText() == "Vehicle"
                else common.property_type if ui.new_item_class_box.currentText() == "Property"
                else ["Other"]
            )
        )
    )
    ui.new_item_shop_box.addItems(common.shop_sites)
    ui.new_item_shop_box.setCurrentIndex(len(common.shop_sites) - 1)

    ui.next_adding_item_button.clicked.connect(
        lambda: (
            ui.adding_item_main_layout.setCurrentIndex(
                (lambda x: x if x <= ui.adding_item_main_layout.count() else ui.adding_item_main_layout.count())
                (ui.adding_item_main_layout.currentIndex() + 1)),
            ui.new_item_finish_label.setText("Item registered. Press exit button on left side" if
                                             ui.new_item_name_box.text() != "" and
                                             ui.new_item_price_box.value() != 0
                                             else "Fill all fields first! (Image is not required)"
                                             ),
            add_item_if_can(ui)
        )
    )

    ui.back_adding_item_button.clicked.connect(
        lambda: ui.adding_item_main_layout.setCurrentIndex(
            (lambda x: x if x >= 0 else 0)(ui.adding_item_main_layout.currentIndex() - 1)
        )
    )

    ui.cancel_adding_item_button.clicked.connect(lambda: ui.content.setCurrentWidget(sender_page))
