import requests
from gui.gui import Ui_MainWindow
from .blur import GlobalBlur
from gui.modules import styles
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from modules.config import Config
from modules.database import Database


def on_load(ui: Ui_MainWindow, MainWindow: QMainWindow):
    ui.logo_if_empty.hide()

    ui.content.setCurrentIndex(0)

    MainWindow.setStyleSheet(styles.centralwidget())
    if 'acrylic' in Config.get().theme:
        GlobalBlur(MainWindow.winId(), acrylic=True)

    if Database.get().items:
        for item in Database.get().items:
            item = Database.get().items[item]
            list_item = QtWidgets.QListWidgetItem()
            list_item.setText(f'{item.item_name} - ${"{:,}".format(item.price)}')
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(requests.get(item.image).content)
            list_item.setIcon(QtGui.QIcon(pixmap))
            ui.items_list.addItem(list_item)

    else:
        ui.logo_if_empty.show()
        ui.items_list.hide()
