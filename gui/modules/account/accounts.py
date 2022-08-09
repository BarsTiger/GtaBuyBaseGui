from gui.gui import Ui_MainWindow
from modules.database import Database
from modules.config import Config


def fill_accounts(ui: Ui_MainWindow):
    ui.accounts_list.clear()
    if not Database.get().profiles:
        return

    for i in range(len(Database.get().profiles)):
        ui.accounts_list.addItem(list(Database.get().profiles)[i])
        if list(Database.get().profiles)[i] == Config.get().profile:
            ui.accounts_list.setCurrentRow(i)


def set_current_profile(ui: Ui_MainWindow):
    if ui.accounts_list.currentItem():
        Config.update("profile", ui.accounts_list.currentItem().text())
