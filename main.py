import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/Зерновой', 'Вкус', 'Цена', 'Объем(мл.)'])
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setRowCount(len(result))
        for x, row in enumerate(result):
            for y, col in enumerate(row):
                self.tableWidget.setItem(x, y, QTableWidgetItem(str(col)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

