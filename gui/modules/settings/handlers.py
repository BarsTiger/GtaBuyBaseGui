from . import *


def register_handlers(ui: Ui_MainWindow):
    ui.open_settings_button.clicked.connect(lambda: on_settings_button_click(ui))
    ui.cancel_settings_button.clicked.connect(lambda: ui.content.setCurrentWidget(ui.main_page))
