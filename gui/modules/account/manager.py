from PyQt5 import QtCore
from gui.gui import Ui_MainWindow
from gui.modules import account
from modules.config import Config
from modules.database import Database
from modules.database.model import Profile


def on_add_click(ui: Ui_MainWindow):
    height = ui.adding_new_item_lay.geometry().height()
    Ui_MainWindow.animation = QtCore.QPropertyAnimation(ui.adding_new_item_lay, b"maximumHeight")
    Ui_MainWindow.animation.setDuration(300)

    if height == 0:
        Ui_MainWindow.animation.setStartValue(0)
        Ui_MainWindow.animation.setEndValue(16777215)

    else:
        Ui_MainWindow.animation.setStartValue(height)
        Ui_MainWindow.animation.setEndValue(0)

    Ui_MainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    Ui_MainWindow.animation.start()


def create_account(ui: Ui_MainWindow):
    if ui.new_account_name_box.text() != "" and \
            ui.new_account_name_box.text() not in list(Database.get().profiles):
        Database.add_profile(Profile(ui.new_account_name_box.text(), []))
        account.accounts.fill_accounts(ui)


def remove_account(ui: Ui_MainWindow):
    if ui.accounts_list.currentItem():
        to_be_removed = ui.accounts_list.currentItem().text()
        Database.remove_profile(to_be_removed)
        account.accounts.fill_accounts(ui)
        if Config.get().profile == to_be_removed:
            if ui.accounts_list.currentItem():
                Config.update("profile", ui.accounts_list.currentItem().text())
            else:
                Config.update("profile", None)
