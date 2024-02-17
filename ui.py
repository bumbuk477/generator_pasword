from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 400)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:gray;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(170, 70, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(190, 150, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.check_str = QtWidgets.QCheckBox(self.centralwidget)
        self.check_str.setGeometry(QtCore.QRect(180, 220, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_str.setFont(font)
        self.check_str.setObjectName("check_str")
        self.check_int = QtWidgets.QCheckBox(self.centralwidget)
        self.check_int.setGeometry(QtCore.QRect(180, 180, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.check_int.setFont(font)
        self.check_int.setObjectName("check_int")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 260, 111, 31))
        self.pushButton.setStyleSheet("border:2px solid red;\n"
"border-radius:10px;\n"
"backgrund- color:purple;\n"
"color: red;\n"
"padding:5px;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generate pasword"))
        self.text.setText(_translate("MainWindow", "генератор паролів"))
        self.result.setText(_translate("MainWindow", "тут буде результат"))
        self.check_str.setText(_translate("MainWindow", "використовувати алфавіт"))
        self.check_int.setText(_translate("MainWindow", "використовувати числа"))
        self.pushButton.setText(_translate("MainWindow", "згенерувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
