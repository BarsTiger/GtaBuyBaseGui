import requests
from gui.gui import Ui_MainWindow
from modules.database import Database
from PyQt5 import QtWidgets, QtGui


def refill_list(ui: Ui_MainWindow):
    ui.items_list.clear()
    if Database.get().items:
        ui.logo_if_empty.hide()
        ui.items_list.show()
        for item in Database.get().items:
            item = Database.get().items[item]
            list_item = QtWidgets.QListWidgetItem()
            list_item.setText(f'{item.item_name} - ${"{:,}".format(item.price)}')
            pixmap = QtGui.QPixmap()
            try:
                pixmap.loadFromData(requests.get(item.image).content)
                list_item.setIcon(QtGui.QIcon(pixmap))
            except Exception as e:
                print(f"Failed to load {item.image}, {e}")

            ui.items_list.addItem(list_item)

    else:
        ui.logo_if_empty.show()
        ui.items_list.hide()
