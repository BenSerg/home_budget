from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from application_functions.create_widgets_functions import create_font, create_line_edit, create_label, \
    create_ok_button, create_msg_box
from application_functions.logger import logger
from application_functions.window_functions import set_window_geometry
from application_windows.main_window import MainWindow
from config.connection import conn


class AuthWindow(QWidget):
    def goto_main_window(self):
        cur = conn.cursor()
        query = f"select user_name, user_password from users where user_name = '{self.username_input.text()}' and user_password = md5('{self.password_input.text()}')"
        cur.execute(query)
        logger.debug(f"Введен запрос: {query}")
        if cur.rowcount > 0:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            msgbox = create_msg_box(title='Ошибка', message='Неправильный логин пользователя или пароль')
            msgbox.exec_()

    def __init__(self):
        super().__init__()
        self.main_window = None
        self.ok_button = None
        self.password_label = None
        self.password_input = None
        self.username_label = None
        self.username_input = None
        self.layout = QVBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Аутентификация')
        set_window_geometry(self)
        font = create_font()

        self.username_input = create_line_edit(self, 245, 120, 311, 31, font)

        self.password_input = create_line_edit(self, 245, 250, 311, 31, font)

        font.setBold(True)
        self.username_label = create_label(self, 245, 90, 350, 31, font, 'Логин пользователя')
        self.password_label = create_label(self, 245, 220, 350, 31, font, 'Пароль пользователя')

        self.ok_button = create_ok_button(self, font)
        self.ok_button.clicked.connect(self.goto_main_window)
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)

        self.setLayout(self.layout)


