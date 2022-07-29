import threading
from PyQt5 import QtWidgets
from gui.gui import Ui_MainWindow
from modules.core.exceptions import hook, thread_hook
from gui.modules import setup_ui
import sys

sys.excepthook = hook
threading.excepthook = thread_hook

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
setup_ui.on_load(ui, MainWindow)

MainWindow.show()


sys.exit(app.exec_())
