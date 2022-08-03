import requests
from PyQt5 import QtWidgets, QtGui, QtCore
from gui.gui import Ui_MainWindow
from modules.database import Database


def on_item_click(ui: Ui_MainWindow, mode: str):
    if ui.items_list.currentItem():
        item = Database.get().items[
            ui.items_list.currentItem().text().removesuffix(' - ' + ui.items_list.currentItem().text().split(' - ')[-1])
        ]

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(item.image).content)
        ui.properties_image.setPixmap(pixmap)

        ui.properties_name.setText(item.item_name)
        ui.properties_price.setText(f'${"{:,}".format(item.price)}')
        ui.properties_class_type.setText(f'{item.item_class} - {item.item_type}')
        ui.properties_shop.setText(item.shop)

    width = ui.item_properties_lay.geometry().width()
    Ui_MainWindow.animation = QtCore.QPropertyAnimation(ui.item_properties_lay, b"minimumWidth")
    Ui_MainWindow.animation.setDuration(300)

    if width == 0:
        Ui_MainWindow.animation.setStartValue(0)
        Ui_MainWindow.animation.setEndValue(480)

        Ui_MainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        Ui_MainWindow.animation.start()
    elif mode == 'close':
        Ui_MainWindow.animation.setStartValue(width)
        Ui_MainWindow.animation.setEndValue(0)

        Ui_MainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        Ui_MainWindow.animation.start()
