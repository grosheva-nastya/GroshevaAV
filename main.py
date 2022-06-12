from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import sys
from PyQt5.QtGui import QIcon
import os

class Window(QMainWindow, QWidget):
    """" """
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Текстовый редактор")
        self.setWindowIcon(QtGui.QIcon('lo.png'))
        self.setGeometry(420, 250, 500, 350)

        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)
        self.createMenuBar()

        self.flag = 0
        self.flag2 = 0


    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(self.fileMenu)

        self.fileMenu2 = QMenu("&Формат", self)
        self.menuBar.addMenu(self.fileMenu2)

        self.fileMenu3 = QMenu("&Действия", self)
        self.menuBar.addMenu(self.fileMenu3)

        self.fileMenu4 = QMenu("&Тема", self)
        self.menuBar.addMenu(self.fileMenu4)

        self.fileMenu.addAction("Новый файл", self.action_clicked)
        self.fileMenu.addAction("Открыть", self.action_clicked)
        self.fileMenu.addAction("Сохранить", self.action_clicked)
        self.fileMenu.addAction("Печать", self.action_clicked)

        self.fileMenu2.addAction("Шрифт", self.action_clicked)
        self.fileMenu2.addAction("Цвет шрифта", self.action_clicked)

        self.background_color = self.fileMenu2.addMenu("&Цвет фона")
        self.fileMenu3.addAction("Копировать", self.action_clicked)
        self.fileMenu3.addAction("Вставить", self.action_clicked)

        self.background_color.addAction("Черный", self.action_clicked)
        self.background_color.addAction("Зеленый", self.action_clicked)
        self.background_color.addAction("Красный", self.action_clicked)
        self.background_color.addAction("Синий", self.action_clicked)
        self.background_color.addAction("Оранжевый", self.action_clicked)
        self.background_color.addAction("Белый", self.action_clicked)

        self.fileMenu4.addAction("Светлая", self.action_clicked)
        self.fileMenu4.addAction("Темная", self.action_clicked)


    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":
            fname, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                            "Text documents (*.txt)")
            try:
                with open(fname, 'r') as f:
                    data = f.read()
                    self.text.setText(data)

            except FileNotFoundError:
                return

        elif action.text() == "Сохранить":
            fname, _ = QFileDialog.getSaveFileName(self, "Save file", "",
                            "Text documents (*.txt)")
            try:
                with open(fname, 'w') as f:
                    save_text = self.text.toPlainText()
                    f.write(save_text)

            except FileNotFoundError:
                return

        elif action.text() == "Новый файл":
            self.text.setText("")

        elif action.text() == "Шрифт":
            font, ok = QtWidgets.QFontDialog.getFont(self.text.currentFont(), self)
            if not ok:
                return
            self.text.setFont(font)

        elif action.text() == "Печать":
            dlg = QPrintDialog()
            try:
                if dlg.exec_():
                    self.editor.print_(dlg.printer())
            except:
                QMessageBox.about(self, "Ошибка!", "Невозможно начать печать. \nДля продолжения работы закройте это окно.\t")

        elif action.text() == "Черный":
            self.text.setStyleSheet("background-color: #000000;")
            self.text.setAutoFillBackground(True)
            self.flag = 1
            self.flag2 = 1

        elif action.text() == "Красный":
            self.text.setStyleSheet("background-color: #EB0707;")
            self.text.setAutoFillBackground(True)
            self.flag = 2
            self.flag2 = 1

        elif action.text() == "Зеленый":
            self.text.setStyleSheet("background-color: #11A94E;")
            self.text.setAutoFillBackground(True)
            self.flag = 3
            self.flag2 = 1

        elif action.text() == "Белый":
            self.text.setStyleSheet("background-color: #FFFFFF;")
            self.text.setAutoFillBackground(True)
            self.flag = 4
            self.flag2 = 1


        elif action.text() == "Синий":
            self.text.setStyleSheet("background-color: #1749CA;")
            self.text.setAutoFillBackground(True)
            self.flag = 5
            self.flag2 = 1


        elif action.text() == "Оранжевый":
            self.text.setStyleSheet("background-color: #FA9C2F;")
            self.text.setAutoFillBackground(True)
            self.flag = 6
            self.flag2 = 1


        elif action.text() == "Цвет шрифта":
            if self.flag2 == 0:
                QMessageBox.about(self, "Ошибка!",
                                  "Сначала выберите цвет фона.\t")
            else:
                col = QColorDialog.getColor()
                if col.isValid():
                    if self.flag == 6:
                        self.text.setStyleSheet("QWidget { color: %s; background-color: #FA9C2F}" % col.name())
                    elif self.flag == 5:
                        self.text.setStyleSheet("QWidget { color: %s; background-color: #1749CA}" % col.name())
                    elif self.flag == 4 or self.flag == 0:
                        self.text.setStyleSheet("QWidget { color: %s; background-color: #FFFFFF}" % col.name())
                    elif self.flag == 3:
                        self.text.setStyleSheet("QWidget { color: %s; background-color: #11A94E}" % col.name())
                    elif self.flag == 2:
                        self.text.setStyleSheet("QWidget { color: %s; background-color: #EB0707}" % col.name())
                    elif self.flag == 1:
                        self.text.setStyleSheet("QWidget { color: %s; background-color: #000000}" % col.name())
                    else:
                        self.text.setStyleSheet("QWidget { color: %s; background-color: #FFFFFF}" % col.name())


        elif action.text() == "Темная":
            self.text.setStyleSheet("QWidget { color: #35E917; background-color: #111111}")

        elif action.text() == "Светлая":
            self.text.setStyleSheet("QWidget { color: #000000; background-color: #FFFFFF}")

        elif action.text() == "Копировать":
            save_text = self.text.toPlainText()
            clipboard = QApplication.clipboard()
            clipboard.setText(save_text)

        elif action.text() == "Вставить":
            textt = QApplication.clipboard().text()
            self.text.insertPlainText(textt + '\n')

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()