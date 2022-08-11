import requests
from PyQt5 import QtWidgets, QtGui, QtCore
from gui.gui import Ui_MainWindow
from modules.database import Database
from modules.config import Config
from gui.modules.core import items_list


def on_item_click(ui: Ui_MainWindow, mode: str):
    if ui.items_list.currentItem():
        item = Database.get().items[items_list.selected_item(ui)]

        pixmap = QtGui.QPixmap()
        try:
            pixmap.loadFromData(requests.get(item.image).content)
            ui.properties_image.setPixmap(pixmap)
        except Exception as e:
            ui.properties_image.clear()
            print(f"Failed to load {item.image}, {e}")

        if Config.get().profile in list(Database.get().profiles):
            ui.own_button.setEnabled(True)

            if item.item_name in Database.get_profile().owned_items:
                ui.own_button.setText("Mark this item as unowned")
            else:
                ui.own_button.setText("Mark this item as owned")
        else:
            ui.own_button.setEnabled(False)
            ui.own_button.setText("Select profile first")

        ui.properties_name.setText(item.item_name)
        ui.properties_price.setText(f'${"{:,}".format(item.price)}')
        ui.properties_class_type.setText(f'{item.item_class} - {item.item_type}')
        ui.properties_shop.setText(item.shop)

    width = ui.item_properties_lay.geometry().width()
    Ui_MainWindow.animation = QtCore.QPropertyAnimation(ui.item_properties_lay, b"minimumWidth")
    Ui_MainWindow.animation.setDuration(300)

    if width == 0 and mode != 'close':
        Ui_MainWindow.animation.setStartValue(0)
        Ui_MainWindow.animation.setEndValue(480)

        Ui_MainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        Ui_MainWindow.animation.start()
    elif mode == 'close':
        Ui_MainWindow.animation.setStartValue(width)
        Ui_MainWindow.animation.setEndValue(0)

        Ui_MainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        Ui_MainWindow.animation.start()
