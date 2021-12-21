import sqlite3
import sys
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow

db = sqlite3.connect('marksdb.db.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    id INT
)''')
db.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS purchase(
    user_name TEXT,
    dat TEXT,
    shopname TEXT,
    money INT
)''')
db.commit()

globalid = 0

class Ui_EnterWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 436)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                 "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ent_but = QtWidgets.QPushButton(self.centralwidget)
        self.ent_but.setGeometry(QtCore.QRect(200, 320, 141, 41))
        self.ent_but.setStyleSheet("border-radius: 20px;\n"
                                   "background-color: rgb(255, 213, 246);")
        self.ent_but.setObjectName("ent_but")
        self.nameline = QtWidgets.QLineEdit(self.centralwidget)
        self.nameline.setGeometry(QtCore.QRect(70, 110, 261, 22))
        self.nameline.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nameline.setStyleSheet("background-color: rgb(255, 213, 246);")
        self.nameline.setObjectName("nameline")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 51, 21))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label.setStyleSheet("\n"
                                 "font: 8pt \"Poor Richard\";\n"
                                 "background-color: rgb(255, 213, 246);\n"
                                 "")
        self.label.setObjectName("label")
        self.passwordline = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordline.setGeometry(QtCore.QRect(70, 170, 261, 22))
        self.passwordline.setStyleSheet("background-color: rgb(255, 213, 246);")
        self.passwordline.setObjectName("passwordline")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 51, 21))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_2.setStyleSheet("\n"
                                   "font: 8pt \"Poor Richard\";\n"
                                   "background-color: rgb(255, 213, 246);")
        self.label_2.setObjectName("label_2")
        self.reg_but = QtWidgets.QPushButton(self.centralwidget)
        self.reg_but.setGeometry(QtCore.QRect(20, 320, 141, 41))
        self.reg_but.setStyleSheet("border-radius: 20px;\n"
                                   "background-color: rgb(255, 213, 246);")
        self.reg_but.setObjectName("reg_but")
        self.wronglabel = QtWidgets.QLabel(self.centralwidget)
        self.wronglabel.setGeometry(QtCore.QRect(90, 210, 191, 16))
        self.wronglabel.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";")
        self.wronglabel.setText("")
        self.wronglabel.setObjectName("wronglabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 101, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("zatratyi.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, -10, 171, 101))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-5W8ZfE8ZErANiKv.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 230, 101, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-i8RSpUNl7S.jpg"))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ent_but.setText(_translate("MainWindow", "Войти"))
        self.label.setText(_translate("MainWindow", "Имя:"))
        self.label_2.setText(_translate("MainWindow", "Пароль:"))
        self.reg_but.setText(_translate("MainWindow", "Регистрация"))


class Ui_RegWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 454)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                 "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameregline = QtWidgets.QLineEdit(self.centralwidget)
        self.nameregline.setGeometry(QtCore.QRect(70, 110, 261, 31))
        self.nameregline.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nameregline.setStyleSheet("background-color: rgb(255, 213, 246);")
        self.nameregline.setObjectName("nameregline")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 51, 21))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label.setStyleSheet("\n"
                                 "font: 8pt \"Poor Richard\";\n"
                                 "background-color: rgb(255, 213, 246);\n"
                                 "")
        self.label.setObjectName("label")
        self.passwordregline = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordregline.setGeometry(QtCore.QRect(70, 170, 261, 31))
        self.passwordregline.setStyleSheet("background-color: rgb(255, 213, 246);")
        self.passwordregline.setObjectName("passwordregline")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 51, 21))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_2.setStyleSheet("\n"
                                   "font: 8pt \"Poor Richard\";\n"
                                   "background-color: rgb(255, 213, 246);")
        self.label_2.setObjectName("label_2")
        self.reg2_but = QtWidgets.QPushButton(self.centralwidget)
        self.reg2_but.setGeometry(QtCore.QRect(100, 320, 141, 41))
        self.reg2_but.setStyleSheet("border-radius: 20px;\n"
                                    "background-color: rgb(255, 213, 246);")
        self.reg2_but.setObjectName("reg2_but")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, -20, 91, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/imgonline-com-ua-Resize-aOo4K6gmkq6X2ZG.jpg"))
        self.label_3.setObjectName("label_3")
        self.stronglabel = QtWidgets.QLabel(self.centralwidget)
        self.stronglabel.setGeometry(QtCore.QRect(90, 210, 191, 16))
        self.stronglabel.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";")
        self.stronglabel.setText("")
        self.stronglabel.setObjectName("stronglabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ИМЯ:"))
        self.label_2.setText(_translate("MainWindow", "Пароль:"))
        self.reg2_but.setText(_translate("MainWindow", "Регистрация"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 652)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                 "font: 8pt \"Segoe Print\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 391, 321))
        self.tableWidget.setStyleSheet("border-radius: 20px;\n"
                                       "background-color: rgb(208, 217, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 540, 121, 51))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: rgb(131, 255, 204);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 460, 331, 41))
        self.label.setStyleSheet("border-radius: 10px;\n"
                                 "background-color: rgb(131, 255, 204);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(90, 380, 82, 17))
        self.radioButton.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: rgb(131, 255, 204);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 380, 101, 17))
        self.radioButton_2.setStyleSheet("border-radius: 20px;\n"
                                         "background-color: rgb(131, 255, 204);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 0, 151, 21))
        self.label_2.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: rgb(131, 255, 204);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 440, 151, 16))
        self.label_3.setStyleSheet("border-radius: 20px;\n"
                                   "background-color: rgb(131, 255, 204);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ПОКУПКА"))
        self.radioButton.setText(_translate("MainWindow", "месяц"))
        self.radioButton_2.setText(_translate("MainWindow", "все вермя"))
        self.label_2.setText(_translate("MainWindow", "История покупок"))
        self.label_3.setText(_translate("MainWindow", "итог:"))


class EnterWindow(QMainWindow, Ui_EnterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect("marksdb.db")
        self.cur = self.db.cursor()
        self.ent_but.clicked.connect(self.enter)
        self.reg_but.clicked.connect(self.register)

    def enter(self):
        user_login = self.nameline.text()
        user_password = self.passwordline.text()
        self.cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        if not self.cur.fetchone() is None:
            res = self.cur.execute("""SELECT password FROM users WHERE login like ?""",
                                                   (user_login,)).fetchall()
            if res[0][0] == user_password:
                res = self.cur.execute("""SELECT id FROM users WHERE login like ?""",
                                       (user_login,)).fetchall()
                global globalid
                globalid = res[0][0]
                self.window = MainWindow()
                self.ui = Ui_MainWindow()
                self.setupUi(MainWindow())
                self.window.show()
                self.hide()
            else:
                self.wronglabel.setText("неверный пароль")

        else:
            self.wronglabel.setText("такого имя пользователя в базе данных нет")

    def register(self):
        self.window = RegWindow()
        self.ui = Ui_RegWindow()
        self.setupUi(RegWindow())
        self.window.show()
        self.hide()


class RegWindow(QMainWindow, Ui_RegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect("marksdb.db")
        self.reg2_but.clicked.connect(self.register)

    def register(self):
        cur = self.db.cursor()
        user_login = self.nameregline.text()
        user_password = self.passwordregline.text()
        if user_password != "" and user_password != "":
            user_id = randint(1, 100000)
            f = False
            while not f:
                cur.execute(f"SELECT login FROM users WHERE id = '{user_id}'")
                if cur.fetchone() is None:
                    f = True
                else:
                    user_id = randint(1, 100000)
            cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
            if cur.fetchone() is None:
                cur.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, user_id))
                self.db.commit()
                global globalid
                globalid = user_id
                self.window = MainWindow()
                self.ui = Ui_MainWindow()
                self.setupUi(MainWindow())
                self.window.show()
                self.hide()

            else:
                self.stronglabel.setText("такой пользователь уже существует")
        else:
            pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect("marksdb.db")
        self.cur = self.db.cursor()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EnterWindow()
    ex.show()
    sys.exit(app.exec())

# def get_result(name):
#     con = sqlite3.connect(name)
#
#     cur = con.cursor()
#     result = cur.execute("""DELETE from films
#                             where genre = (SELECT id FROM genres WHERE
#                              title = "фантастика") AND year < 2000 AND duration > 90""").fetchall()
#
#     con.commit()
#     con.close()
# def open_create_widget(self):
#       ex1 = AddFilm(self)
#       ex1.show()
#       self.rendering_table()
# def open_delete_widget(self):
#       ex1 = DeleteFilm(self)
#       self.rendering_table()

#   def open_create_genre(self):
#       ex1 = AddGenre(self)
#       ex1.show()
#       self.rendering_table()
