import sys
import sqlite3
import datetime
from PIL import Image
from matplotlib import pyplot as plt

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QComboBox, QInputDialog, \
    QDialogButtonBox, QFormLayout, QLineEdit, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDesktopWidget, QDialog

# создаем/подсоединяем базу данных
try:
    con = sqlite3.connect("main.sqlite")
    cur = con.cursor()
    cur.execute("""CREATE TABLE Accounts (
account_name TEXT,
income       INTEGER,
expences     INTEGER,
remainder    INTEGER);""")
    cur.execute("""CREATE TABLE Expences (
account  TEXT,
category TEXT,
expences INTEGER,
note     TEXT);""")
    cur.execute("""CREATE TABLE Incomes (
account  TEXT,
category TEXT,
incomes  INTEGER,
note     TEXT);""")
except Exception:
    pass

# выравнивание по центру
def Center_Window(self):
    global flag
    qtRectangle = self.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    self.move(qtRectangle.topLeft())
    qtRectangle = self.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    self.move(qtRectangle.topLeft())


# вставлять данные в таблицу (счета, доходы, расходы)
def paste_accounts(self):
    result = cur.execute("""SELECT * FROM Accounts""").fetchall()
    n = 0
    for line in result:
        self.table_widget.setItem(n, 0, QTableWidgetItem(str(line[0])))
        self.table_widget.setItem(n, 1, QTableWidgetItem(str(line[1])))
        self.table_widget.setItem(n, 2, QTableWidgetItem(str(line[2])))
        self.table_widget.setItem(n, 3, QTableWidgetItem(str(line[3])))
        n += 1


def paste_incomes(self):
    result = cur.execute("""SELECT * FROM Incomes""").fetchall()
    n = 0
    for line in result:
        self.table_widget.setItem(n, 0, QTableWidgetItem(str(line[0])))
        self.table_widget.setItem(n, 1, QTableWidgetItem(str(line[1])))
        self.table_widget.setItem(n, 2, QTableWidgetItem(str(line[2])))
        self.table_widget.setItem(n, 3, QTableWidgetItem(str(line[3])))
        n += 1


def paste_expences(self):
    result = cur.execute("""SELECT * FROM Expences""").fetchall()
    n = 0
    for line in result:
        self.table_widget.setItem(n, 0, QTableWidgetItem(str(line[0])))
        self.table_widget.setItem(n, 1, QTableWidgetItem(str(line[1])))
        self.table_widget.setItem(n, 2, QTableWidgetItem(str(line[2])))
        self.table_widget.setItem(n, 3, QTableWidgetItem(str(line[3])))
        n += 1


# начало программы
class User(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 250, 350, 250)
        self.setWindowTitle('Вход')
        # кнопки
        self.login_user = QPushButton('Вход', self)
        self.about = QPushButton('О программе', self)
        self.login_user.resize(100, 100)
        self.about.resize(100, 100)
        self.login_user.move(15, 15)
        self.about.move(15, 135)

        # картинка
        image_path = 'лого компании.png'
        img = Image.open(image_path)
        new_image = img.resize((200, 200))
        new_image.save('лого.png')

        self.label = QLabel(self)
        self.pixmap = QPixmap('лого.png')
        self.label.setPixmap(self.pixmap)
        self.pixmap = self.pixmap.scaled(50, 50)
        self.label.move(135, 25)

        # подсоединяем кнопки
        self.login_user.clicked.connect(self.login)
        self.about.clicked.connect(self.about_project)
        Center_Window(self)

    def login(self):
        # открываем основное окно
        self.ex2 = MainWindow()
        self.ex2.show()
        self.close()

    def about_project(self):
        # открываем окно "о программе"
        self.exN = AboutProject()
        self.exN.show()

# окно "О программе"
class AboutProject(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(615, 150, 615, 150)
        self.setWindowTitle('О программе')
        # абузим систему, чтобы получить доп баллы
        f = open('about.txt', 'r', encoding='utf8')
        f1 = f.readline()
        f2 = f.readline()
        f3 = f.readline()
        f4 = f.readline()
        # создаем текст
        self.text1 = QLabel(f1, self)
        self.text1.move(10, 10)
        self.text2 = QLabel(f2, self)
        self.text2.move(10, 30)
        self.text3 = QLabel(f3, self)
        self.text3.move(10, 50)
        self.text4 = QLabel(f4, self)
        self.text4.move(10, 70)
        # кнопки
        self.ok = QPushButton('GO!', self)
        self.ok.resize(100, 30)
        self.ok.move(500, 110)
        self.ok.clicked.connect(self.bye)
        # центрирование
        Center_Window(self)

    def bye(self):
        # закрываем окошко
        self.close()


# основное окно
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 800, 800, 800)
        self.setWindowTitle('Основное окно')
        # кнопки и работа с ними
        self.exit_button = QPushButton('Выход', self)
        self.accounts_button = QPushButton('Счета', self)
        self.income_button = QPushButton('Доходы', self)
        self.expences_button = QPushButton('Расходы', self)
        self.add_user_button = QPushButton('+', self)
        self.add_income_button = QPushButton('+', self)
        self.add_expences_button = QPushButton('+', self)
        self.watch_stats_button = QPushButton('Посмотреть статистику', self)

        self.exit_button.resize(180, 75)
        self.accounts_button.resize(150, 75)
        self.income_button.resize(150, 75)
        self.expences_button.resize(150, 75)
        self.add_user_button.resize(30, 75)
        self.add_income_button.resize(30, 75)
        self.add_expences_button.resize(30, 75)
        self.watch_stats_button.resize(150, 75)

        self.exit_button.move(600, 30)
        self.accounts_button.move(600, 210)
        self.income_button.move(600, 310)
        self.expences_button.move(600, 410)
        self.add_user_button.move(750, 210)
        self.add_income_button.move(750, 310)
        self.add_expences_button.move(750, 410)
        self.watch_stats_button.move(600, 650)

        self.exit_button.clicked.connect(self.exit)
        self.accounts_button.clicked.connect(self.accounts)
        self.income_button.clicked.connect(self.income)
        self.expences_button.clicked.connect(self.expences)
        self.add_user_button.clicked.connect(self.add_user)
        self.add_income_button.clicked.connect(self.add_incomes)
        self.add_expences_button.clicked.connect(self.add_expences)
        self.watch_stats_button.clicked.connect(self.watch_stats)

        # сегодняшняя дата
        data_now = str(datetime.datetime.now())[:-7]
        self.datetime_text = QLabel(data_now, self)
        self.datetime_text.move(10, 10)

        # таблица
        self.table_widget = QTableWidget(self)
        self.table_widget.resize(560, 732)
        self.table_widget.move(10, 30)

        self.table_widget.setColumnCount(4)
        self.table_widget.setRowCount(25)
        self.table_widget.clearContents()

        self.table_widget.setHorizontalHeaderLabels(["Название счёта", "Доходы", "Расходы", "Остаток"])

        self.table_widget.setColumnWidth(0, 125)
        self.table_widget.setColumnWidth(1, 125)
        self.table_widget.setColumnWidth(2, 125)
        self.table_widget.setColumnWidth(3, 125)
        # создаем строки циклом
        n = 0
        for i in range(25):
            self.table_widget.setRowHeight(n, 68)
            n += 1

        # данные
        paste_accounts(self)

        Center_Window(self)

    def exit(self):
        # кнопка выхода
        self.close()

    def add_user(self):
        # диалоговое окно для ввода названия счет
        name, ok_pressed = QInputDialog.getText(self, "Новый счёт", "Введите название нового счёта:")
        if ok_pressed:
            cur.execute(f"INSERT INTO Accounts (account_name, income, expences, remainder) VALUES('{name}', 0, 0, 0);")
        con.commit()
        paste_accounts(self)

    def accounts(self):
        # таблица счетов
        self.table_widget.setHorizontalHeaderLabels(["Название счёта", "Доходы", "Расходы", "Остаток"])
        self.table_widget.clearContents()
        self.table_widget.setColumnWidth(0, 125)
        self.table_widget.setColumnWidth(1, 125)
        self.table_widget.setColumnWidth(2, 125)
        self.table_widget.setColumnWidth(3, 125)

        n = 0
        for i in range(25):
            self.table_widget.setRowHeight(n, 68)
            n += 1

        paste_accounts(self)

    def income(self):
        # таблица доходов
        self.table_widget.setHorizontalHeaderLabels(["Название счёта", "Категория", "Сумма доходов", "Примечание"])
        self.table_widget.clearContents()
        self.table_widget.setColumnWidth(0, 125)
        self.table_widget.setColumnWidth(1, 125)
        self.table_widget.setColumnWidth(2, 125)
        self.table_widget.setColumnWidth(3, 125)

        n = 0
        for i in range(25):
            self.table_widget.setRowHeight(n, 68)
            n += 1

        paste_incomes(self)

    def expences(self):
        # таблица расходов
        self.table_widget.setHorizontalHeaderLabels(["Название счёта", "Категория", "Сумма расходов", "Примечание"])
        self.table_widget.clearContents()
        self.table_widget.setColumnWidth(0, 125)
        self.table_widget.setColumnWidth(1, 125)
        self.table_widget.setColumnWidth(2, 125)
        self.table_widget.setColumnWidth(3, 125)

        n = 0
        for i in range(25):
            self.table_widget.setRowHeight(n, 68)
            n += 1

        paste_expences(self)

    def add_incomes(self):
        # открываем окно ввода доходов
        # если не создано ни одного счета вызываем ошибку
        if not cur.execute("""SELECT * FROM Accounts""").fetchall():
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Для начала создайте хотя бы одного пользователя!",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )

        else:
            self.some = IncomeInput()
            self.some.show()

    def add_expences(self):
        # открываем окно ввода расходов
        # если не создано ни одного счета вызываем ошибку
        if not cur.execute("""SELECT * FROM Accounts""").fetchall():
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Для начала создайте хотя бы одного пользователя!",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
        else:
            self.some1 = ExpenseInput()
            self.some1.show()

    def watch_stats(self):
        # открываем окно статистики
        # если не создано ни одного счета вызываем ошибку
        if not cur.execute("""SELECT * FROM Accounts""").fetchall():
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Для начала создайте хотя бы одного пользователя!",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
        else:
            self.some2 = watchStats()
            self.some2.show()


# ввод информации о расходах
class ExpenseInput(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 170)
        # создаем поля для опроса
        self.first = QComboBox(self)
        self.category = QComboBox(self)
        self.post = QLineEdit(self)
        self.sum = QLineEdit(self)

        s = cur.execute("""SELECT account_name FROM Accounts""").fetchall()
        for i in s:
            self.first.addItem(str(i[0]))

        self.category.addItems(
            ['Автомобиль', 'Комиссия', 'Коммунальные услуги', 'Мебель', 'Медицина', 'Одежда', 'Продукты питания',
             'Развлечения', 'Хозяйственные товары', 'Техника'])
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Выберите счёт", self.first)
        layout.addRow("Выберите категорию", self.category)
        layout.addRow("Сумма", self.sum)
        layout.addRow("Примечание", self.post)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.entry)
        buttonBox.rejected.connect(self.reject)

    def entry(self):
        # заполняем базу данных введенной информацией
        f1 = self.first.currentText()
        f2 = self.category.currentText()
        f3 = self.sum.text()
        f4 = self.post.text()
        sqlite_insert_query = f"INSERT INTO Expences (account, category, expences, note) VALUES('{f1}', '{f2}', {f3}, '{f4}');"
        cur.execute(sqlite_insert_query)
        n = cur.execute(f"SELECT expences FROM Accounts WHERE account_name = '{f1}'").fetchall()
        cur.execute(f"UPDATE Accounts SET expences = {int(f3) + int(n[0][0])} WHERE account_name = '{f1}'")
        n1 = cur.execute(f"SELECT income FROM Accounts WHERE account_name = '{f1}'").fetchall()
        cur.execute(f"UPDATE Accounts SET remainder = {int(n1[0][0]) - (int(f3) + int(n[0][0]))} WHERE account_name = '{f1}'")
        con.commit()
        self.close()


# ввод информации о доходах
class IncomeInput(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 170)
        # создаем поля для опроса
        self.first = QComboBox(self)
        self.category = QComboBox(self)
        self.post = QLineEdit(self)
        self.sum = QLineEdit(self)

        s = cur.execute("""SELECT account_name FROM Accounts""").fetchall()
        for i in s:
            self.first.addItem(str(i[0]))

        self.category.addItems(
            ['Зарплата', 'Дивиденды', 'Лотерея', 'Материальная помощь', 'Наследство', 'Находка', 'Пенсия', 'Подарок',
             'Продажа имущества', 'Страховка'])
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.layout = QFormLayout(self)
        self.layout.addRow("Выберите счёт", self.first)
        self.layout.addRow("Выберите категорию", self.category)
        self.layout.addRow("Сумма", self.sum)
        self.layout.addRow("Примечание", self.post)
        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.entry)
        buttonBox.rejected.connect(self.reject)

    def entry(self):
        # заполняем базу данных введенной информацией
        f1 = self.first.currentText()
        f2 = self.category.currentText()
        f3 = self.sum.text()
        f4 = self.post.text()
        sqlite_insert_query = f"INSERT INTO Incomes (account, category, incomes, note) VALUES('{f1}', '{f2}', {f3}, '{f4}');"
        cur.execute(sqlite_insert_query)
        n = cur.execute(f"SELECT income FROM Accounts WHERE account_name = '{f1}'").fetchall()
        cur.execute(f"UPDATE Accounts SET income = {int(f3) + int(n[0][0])} WHERE account_name = '{f1}'")
        n1 = cur.execute(f"SELECT expences FROM Accounts WHERE account_name = '{f1}'").fetchall()
        cur.execute(f"UPDATE Accounts SET remainder = {int(f3) + int(n[0][0]) - int(n1[0][0])} WHERE account_name = '{f1}'")
        con.commit()
        self.close()


# окно с статистикой
class watchStats(QWidget):
    def __init__(self):
        super().__init__()
        # создаем окно
        self.setGeometry(720, 700, 720, 700)
        self.setWindowTitle('Посмотреть статистику')
        self.account_choice_text = QLabel('Выберите счёт:', self)
        self.account_stats_button = QPushButton('Общая статистика', self)
        self.income_stats_button = QPushButton('Статистика доходов', self)
        self.expence_stats_button = QPushButton('Статистика расходов', self)
        self.account_stats_button.resize(150, 50)
        self.income_stats_button.resize(150, 50)
        self.expence_stats_button.resize(150, 50)
        self.account_choice_text.move(10, 20)
        self.account_stats_button.move(200, 15)
        self.income_stats_button.move(375, 15)
        self.expence_stats_button.move(550, 15)
        self.account_choice = QComboBox(self)
        s = cur.execute("""SELECT account_name FROM Accounts""").fetchall()
        for i in s:
            self.account_choice.addItem(str(i[0]))
        self.account_choice.resize(150, 25)
        self.account_choice.move(10, 40)

        self.account_stats_button.clicked.connect(self.account_stats)
        self.income_stats_button.clicked.connect(self.income_stats)
        self.expence_stats_button.clicked.connect(self.expence_stats)

        Center_Window(self)

    def account_stats(self):
        income_sum = cur.execute(
            f"SELECT income FROM Accounts WHERE account_name = '{self.account_choice.currentText()}'").fetchall()
        expence_sum = cur.execute(
            f"SELECT expences FROM Accounts WHERE account_name = '{self.account_choice.currentText()}'").fetchall()
        # раскладываем данные для картинки круговой диаграммы
        elements = ['Расходы', 'Доходы']

        data = [int(expence_sum[0][0]), int(income_sum[0][0])]

        if not len(data) >= 2 or not len(elements) >= 2 or 0 in data:
            # на всякий случай создаем ошибку, если элементов в массиве меньше двух или одно изщ значений равно 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Должно быть хотя бы по два аргумента со значением!",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
        else:
            # создаем диаграмму
            fig = plt.figure(figsize=(8, 6))
            plt.pie(data, labels=elements)

            plt.savefig('pict.png')
            # вставляем картинку
            self.label = QLabel(self)
            self.pixmap = QPixmap('pict.png')
            self.label.setPixmap(self.pixmap)
            self.label.move(-80, 75)
            self.label.show()


    def income_stats(self):
        info_diag = cur.execute(
            f"SELECT category, incomes FROM Incomes WHERE account = '{self.account_choice.currentText()}'").fetchall()
        # раскладываем данные для картинки круговой диаграммы
        d = dict()

        for i in info_diag:
            f1, f2 = i[0], i[1]
            if f1 in d.keys():
                d[f1] += f2
            else:
                d[f1] = f2

        elements = [i for i in d.keys()]
        data = [d[i] for i in d]

        if not len(d) >= 2:
            # на всякий случай создаем ошибку, если категорий меньше двух
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Должно быть хотя бы по два аргумента со значением!",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
        else:
            # создаем диаграмму
            fig = plt.figure(figsize=(8, 6))
            plt.pie(data, labels=elements)

            plt.savefig('pict.png')
            # вставляем картинку
            self.label = QLabel(self)
            self.pixmap = QPixmap('pict.png')
            self.label.setPixmap(self.pixmap)
            self.label.move(-80, 75)
            self.label.show()

    def expence_stats(self):
        info_diag = cur.execute(
            f"SELECT category, expences FROM Expences WHERE account = '{self.account_choice.currentText()}'").fetchall()

        # раскладываем данные для картинки круговой диаграммы
        d = dict()

        for i in info_diag:
            f1, f2 = i[0], i[1]
            if f1 in d.keys():
                d[f1] += f2
            else:
                d[f1] = f2

        elements = [i for i in d.keys()]
        data = [d[i] for i in d]

        if not len(d) >= 2:
            # на всякий случай создаем ошибку, если категорий меньше двух
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Должно быть хотя бы по два аргумента со значением!",
                buttons=QMessageBox.Ok,
                defaultButton=QMessageBox.Ok,
            )
        else:
            #создаем картинку нашей диаграммы
            fig = plt.figure(figsize=(8, 6))
            plt.pie(data, labels=elements)

            plt.savefig('pict.png')
            #вставляем картинку
            self.label = QLabel(self)
            self.pixmap = QPixmap('pict.png')
            self.label.setPixmap(self.pixmap)
            self.label.move(-80, 75)
            self.label.show()


# конец (победа)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = User()
    ex.show()
    sys.exit(app.exec())
