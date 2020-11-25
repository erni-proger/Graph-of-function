import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets

N = '1234567890'
OPER = [['^'], ['*', '/'], ['+', '-']]


def col():
    return random.choice('rgbw')


def math(a, op, b):
    try:
        if op == '*':
            return a * b
        if op == '/':
            return a / b
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '^':
            return a ** b
    except Exception:
        return 0


def y_from_x(x, func):
    func = list(''.join(func.split()))

    # подставляем x
    for i in range(len(func)):
        if func[i] == 'x':
            func[i] = x

    # подсчет функции
    for el in OPER:
        try:
            for i in range(len(func)):
                if func[i] in el:
                    func[i] = math(float(func[i - 1]), func[i], float(func[i + 1]))
                    del func[i - 1]
                    del func[i]
        except IndexError:
            pass

    return float(func[0])


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 511, 251))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 310, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 320, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 310, 201, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 270, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 20))
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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "F(x)="))
        self.label_2.setText(_translate("MainWindow", "Доступные символы: x 0123456789 ^ * / + -"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.graphicsView.clear()
        self.graphicsView.plot([i for i in range(-10, 11)],
                               [y_from_x(i, self.lineEdit.text()) for i in range(-10, 11)],
                               pen=col())


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
