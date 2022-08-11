from . import *
from gui.gui import Ui_MainWindow


def register_handlers(ui: Ui_MainWindow):
    ui.open_settings_button.clicked.connect(lambda: on_settings_open.on_settings_button_click(ui))
    ui.cancel_settings_button.clicked.connect(lambda: ui.content.setCurrentWidget(ui.main_page))

    ui.save_gui_setting_button.clicked.connect(lambda: visual.on_save_visual_click(ui))

    db.register_db_handlers(ui)
