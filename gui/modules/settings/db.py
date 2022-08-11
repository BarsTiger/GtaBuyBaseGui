import os
from gui.modules.core.popup import popup
from gui.gui import Ui_MainWindow
from modules.config import Config
from gui.modules.core import items_list


def on_load_another_db_click(ui: Ui_MainWindow):
    Config.update("database", ui.database_list_box.currentText())
    items_list.refill_list(ui)


def create_backup():
    with open(os.path.splitext(Config.get().database)[0] + '.gtaback', 'w') as f:
        f.write(open(Config.get().database).read())


def load_backup(ui: Ui_MainWindow):
    if os.path.isfile(os.path.splitext(Config.get().database)[0] + '.gtaback'):
        if popup('Loading backup', 'Do you really want to rollback you database to newest backup state?', 4) == 6:
            with open(Config.get().database, 'w') as f:
                try:
                    f.write(open(os.path.splitext(Config.get().database)[0] + '.gtaback').read())
                except Exception as e:
                    popup("Error", f"Error happened: {e}")
            items_list.refill_list(ui)

    else:
        popup('Error', 'No backup found')


def remove_db(ui: Ui_MainWindow):
    if popup('Removing database', 'Do you really want to remove selected database?', 4) != 6:
        return

    os.remove(ui.database_list_box.currentText())
    ui.database_list_box.removeItem(ui.database_list_box.currentIndex())
    if ui.database_list_box.currentText() != "":
        Config.update("database", ui.database_list_box.currentText())
        items_list.refill_list(ui)
    else:
        Config.update("database", "default.gtabase")
        ui.database_list_box.addItem("default.gtabase")
        items_list.refill_list(ui)


def create_db(ui: Ui_MainWindow):
    Config.update("database", ui.new_db_name_box.text() + ".gtabase")
    ui.database_list_box.addItem(Config.get().database)
    ui.database_list_box.setCurrentText(Config.get().database)
    items_list.refill_list(ui)


def register_db_handlers(ui: Ui_MainWindow):
    ui.load_this_db_button.clicked.connect(lambda: on_load_another_db_click(ui))
    ui.create_backup_button.clicked.connect(create_backup)
    ui.load_backup_button.clicked.connect(lambda: load_backup(ui))
    ui.delete_db_button.clicked.connect(lambda: remove_db(ui))
    ui.new_db_create_button.clicked.connect(lambda: create_db(ui))
