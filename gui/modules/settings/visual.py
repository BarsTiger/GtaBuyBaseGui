from gui.gui import Ui_MainWindow
from modules.config import Config


def on_save_visual_click(ui: Ui_MainWindow):
    Config.update("theme", ui.app_theme_box.currentText())
