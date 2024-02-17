# generator_pasword
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from random import randint
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate)
    def generate(self):
        if self.ui.check_str.isChecked() and self.ui.check_int.isChecked():
            n = randint(8,16)
            res = ""
            alf=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            for i in range(n):
                j = randint(1,2)
                if j == 1:
                    g = randint(0,9)
                    res+=str(g)
                else:
                    g = randint(0,len(alf)-1)
                    y = randint(1,2)
                    if y == 1:
                        res+=alf[g]
                    else:
                        res+=alf[g].lower()
            self.ui.result.setText(res)            
        elif self.ui.check_int.isChecked():
            n = randint(8,16)
            res = ""
            for i in range(n):
                j = randint(0,9)
                res+=str(j)
            self.ui.result.setText(res)
        elif self.ui.check_str.isChecked():
            alf=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            n = randint(8,16)
            res = ""
            for i in range(n):
                y = randint(1,2)
                j = randint(0,len(alf)-1)
                if y == 1:
                    res += alf[j]
                else:
                    res+=alf[j].lower()
            self.ui.result.setText(res)
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
