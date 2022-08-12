from gui.gui import Ui_MainWindow
from gui.modules.handlers import fill_info
from gui.modules.handlers import on_item_remove
from gui.modules.adding_item import on_add_click
from gui.modules.filters import menu
from gui.modules.core import items_list
from gui.modules import account
from gui.modules import settings
from gui.modules import edit


def register_handlers(ui: Ui_MainWindow):
    ui.items_list.itemClicked.connect(lambda: fill_info.on_item_click(ui, 'open'))
    ui.items_list.itemDoubleClicked.connect(lambda: fill_info.on_item_click(ui, 'close'))

    ui.delete_item_button.clicked.connect(lambda: on_item_remove.on_rm_click(ui))

    ui.add_item_button.clicked.connect(lambda: on_add_click.on_add_button_click(ui))

    ui.open_filter_button.clicked.connect(lambda: menu.on_open_close_click(ui))

    ui.filter_class_box.currentIndexChanged.connect(lambda: menu.refill_types(ui))
    ui.filters_apply_button.clicked.connect(lambda: items_list.refill_list(ui))

    ui.manage_profiles_button.clicked.connect(lambda: (ui.content.setCurrentWidget(ui.account_page),
                                                       account.accounts.fill_accounts(ui)))
    ui.cancel_account.clicked.connect(lambda: ui.content.setCurrentWidget(ui.main_page))

    ui.create_new_account.clicked.connect(lambda: account.manager.on_add_click(ui))
    ui.remove_selected_account.clicked.connect(lambda: account.manager.remove_account(ui))
    ui.cancel_account_creation.clicked.connect(lambda: account.manager.on_add_click(ui))
    ui.accept_account_name.clicked.connect(lambda: account.manager.create_account(ui))
    ui.use_this_account_button.clicked.connect(lambda: account.accounts.set_current_profile(ui))

    ui.own_button.clicked.connect(lambda: account.owning.on_change_owning_clicked(ui))

    ui.edit_item_button.clicked.connect(lambda: edit.on_edit.on_edit_item_click(ui))
    ui.cancel_edit_button.clicked.connect(lambda: (ui.content.setCurrentWidget(ui.main_page),
                                                   items_list.refill_list(ui)))
    ui.edit_box_item_class.currentTextChanged.connect(lambda: edit.on_edit.fill_type_box(ui))
    ui.edit_save_button.clicked.connect(lambda: edit.on_edit.on_save_edit(ui))

    on_add_click.register_add_handlers(ui)
    settings.register_handlers(ui)
