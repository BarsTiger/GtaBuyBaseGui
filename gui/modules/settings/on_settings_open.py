from gui.gui import Ui_MainWindow
from modules.config import Config
import glob


def on_settings_button_click(ui: Ui_MainWindow):
    ui.database_list_box.clear()
    ui.database_list_box.addItems(glob.glob("*.gtabase"))
    ui.database_list_box.setCurrentText(Config.get().database)
    ui.app_theme_box.setCurrentText(Config.get().theme)

    ui.content.setCurrentWidget(ui.settings_page)
