from PyQt5 import QtGui, QtCore
from gui.gui import Ui_MainWindow
from modules.database import Database
from data import common


def refill_types(ui: Ui_MainWindow):
    ui.filter_type_box.clear()
    ui.filter_type_box.addItem('All')
    ui.filter_type_box.setCurrentIndex(0)

    string_db = str(Database.get().to_json())

    match ui.filter_class_box.currentText():
        case 'All':
            for type_ in common.vehicle_type:
                if type_ in string_db:
                    ui.filter_type_box.addItem(type_)

            for type_ in common.property_type:
                if type_ in string_db:
                    ui.filter_type_box.addItem(type_)

        case 'Vehicle':
            for type_ in common.vehicle_type:
                if type_ in string_db:
                    ui.filter_type_box.addItem(type_)

        case 'Property':
            for type_ in common.property_type:
                if type_ in string_db:
                    ui.filter_type_box.addItem(type_)

        case 'Other':
            ui.filter_type_box.addItem('Other')


def refill_filters(ui: Ui_MainWindow):
    ui.filter_class_box.clear()
    ui.filter_class_box.addItem('All')
    ui.filter_class_box.setCurrentIndex(0)
    ui.filter_type_box.clear()
    ui.filter_type_box.addItem('All')
    ui.filter_type_box.setCurrentIndex(0)
    ui.filter_shop_box.clear()
    ui.filter_shop_box.addItem('All')
    ui.filter_shop_box.setCurrentIndex(0)

    string_db = str(Database.get().to_json())

    for class_ in common.items_class:
        if class_ in string_db:
            ui.filter_class_box.addItem(class_)

    for type_ in common.vehicle_type:
        if type_ in string_db:
            ui.filter_type_box.addItem(type_)

    for type_ in common.property_type:
        if type_ in string_db:
            ui.filter_type_box.addItem(type_)

    for shop in common.shop_sites:
        if shop in string_db:
            ui.filter_shop_box.addItem(shop)


def on_open_close_click(ui: Ui_MainWindow):
    width = ui.filter_lay.geometry().width()
    Ui_MainWindow.animation = QtCore.QPropertyAnimation(ui.filter_lay, b"minimumWidth")
    Ui_MainWindow.animation.setDuration(300)

    if width == 0:
        Ui_MainWindow.animation.setStartValue(0)
        Ui_MainWindow.animation.setEndValue(250)

        Ui_MainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        Ui_MainWindow.animation.start()
    else:
        Ui_MainWindow.animation.setStartValue(width)
        Ui_MainWindow.animation.setEndValue(0)

        Ui_MainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        Ui_MainWindow.animation.start()
