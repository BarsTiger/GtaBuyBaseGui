from gui.gui import Ui_MainWindow
from modules.config import Config
from gui.modules.core import items_list


def on_save_visual_click(ui: Ui_MainWindow):
    Config.update("theme", ui.app_theme_box.currentText())
    Config.update("images", ui.show_images_check.isChecked())

    items_list.refill_list(ui)
