from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal
from gui import Ui_MainWindow
import sys

class Main(QMainWindow):
    signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculator")
        
        self.plain()
        self.reset_buttons()
        
        self.max_length = 14
        self.int = ""
        self.result = ""
        self.i = 0
        self.isEqualed = False
    
    def reset_buttons(self, enable=False):
        self.ui.pushButton_per.setEnabled(enable)
        self.ui.pushButton_div.setEnabled(enable)
        self.ui.pushButton_multi.setEnabled(enable)
        self.ui.pushButton_minus.setEnabled(enable)
        self.ui.pushButton_plus.setEnabled(enable)
        self.ui.pushButton_eq.setEnabled(enable)
        self.ui.pushButton_p.setEnabled(enable)
        self.ui.pushButton_pm.setEnabled(enable)
        self.ui.pushButton_dot.setEnabled(enable)
        
    def reset_numbers(self, enable=False):
        self.ui.pushButton_0.setEnabled(enable)
        self.ui.pushButton_1.setEnabled(enable)
        self.ui.pushButton_2.setEnabled(enable)
        self.ui.pushButton_3.setEnabled(enable)
        self.ui.pushButton_4.setEnabled(enable)
        self.ui.pushButton_5.setEnabled(enable)
        self.ui.pushButton_6.setEnabled(enable)
        self.ui.pushButton_7.setEnabled(enable)
        self.ui.pushButton_8.setEnabled(enable)
        self.ui.pushButton_9.setEnabled(enable)
        
    def plain(self):
        self.ui.pushButton.clicked.connect(self.clear_all)
        
        self.ui.pushButton_0.clicked.connect(lambda: self.get_number('0'))
        self.ui.pushButton_1.clicked.connect(lambda: self.get_number('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.get_number('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.get_number('3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.get_number('4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.get_number('5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.get_number('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.get_number('7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.get_number('8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.get_number('9'))
        
        self.ui.pushButton_dot.clicked.connect(lambda: self.operator('.'))
        self.ui.pushButton_plus.clicked.connect(lambda: self.operator('+'))
        self.ui.pushButton_minus.clicked.connect(lambda: self.operator('-'))
        self.ui.pushButton_multi.clicked.connect(lambda: self.operator('×'))
        self.ui.pushButton_div.clicked.connect(lambda: self.operator('÷'))
        self.ui.pushButton_per.clicked.connect(lambda: self.operator('%'))
        self.ui.pushButton_pm.clicked.connect(self.plus_minus)
        self.ui.pushButton_p.clicked.connect(self.parantheses)
        self.ui.pushButton_eq.clicked.connect(lambda: self.operator('='))
        
        self.signal.connect(self.calculate)
        
    def clear_all(self):
        self.ui.label_input.setText("")
        self.ui.label_up.setText("")
        self.result = ""
        self.i = 0
        self.reset_buttons()
        self.reset_numbers(True)
        
    def get_number(self, number):
        self.length_label_text()
        if self.isEqualed:
            self.ui.label_input.setText("")
            self.isEqualed = False
        self.ui.label_input.setText(self.ui.label_input.text() + number)
        self.reset_buttons(True)
        self.int += number
        self.signal.emit(number)
        
    def operator(self, op):
        self.length_label_text()
        self.ui.pushButton_per.setEnabled(False)
        self.ui.label_input.setText(self.ui.label_input.text() + op)
        if op == '×':
            op = '*'
        if op == '÷':
            op = '/'
        self.signal.emit(op)
        
    def calculate(self, expression):
        self.length_label_text()
        self.result += expression
        try:
            if self.ui.label_input.text() == '0':
                self.ui.pushButton_0.setEnabled(False)
                
            if expression == '=':
                if self.i % 2 == 1:
                    self.result = self.result[:-1] + ')'
                    self.total = eval(self.result)
                self.isEqualed = True
                self.ui.label_input.setText(str(self.total))
                self.ui.label_up.setText("")
                self.result = ""
                self.reset_buttons()
            if expression == '%':
                self.result = self.result[:-1] + '/100*'
                self.input = self.ui.label_input.text() + '×'
                self.ui.label_input.setText(self.input)
                self.total = eval(self.result)
            if len(self.result) > 1 and self.result[-2] == '0':
                self.result = self.result[:-2] + expression
                self.total = eval(self.result)
            if expression == '+' or expression == '-' or expression == '*' or expression == '/':
                self.int = ""
                self.ui.pushButton_per.setEnabled(False)
                if self.result[-2] in ['+', '-', '*', '/']:
                    self.result = self.result[:-2] + expression
                    if expression == '*':
                        self.input = self.ui.label_input.text()[:-2] + '×'
                    elif expression == '/':
                        self.input = self.ui.label_input.text()[:-2] + '÷'
                    else:
                        self.input = self.ui.label_input.text()[:-2] + expression
                    self.ui.label_input.setText(self.input)
            else:
                if self.result[-2] == ')':
                    self.result = self.result[:-1] + '*' + expression 
                    self.ui.label_input.setText(self.ui.label_input.text()[:-1] + '×' + expression)
                self.total = eval(self.result)
            self.ui.label_up.setText(str(self.total)) 
        except Exception:
            self.ui.label_up.setText("")
            
    def parantheses(self):
        self.ui.pushButton_dot.setEnabled(False)
        self.length_label_text()
        self.i += 1
        if self.ui.label_input.text() == "":
            self.ui.label_input.setText("(")
            self.result += "("
        else:
            if self.i % 2 == 0:
                self.ui.label_input.setText(self.ui.label_input.text() + ")")
                self.result += ")"
            elif self.result[-1] == '*':
                self.ui.label_input.setText(self.ui.label_input.text() + "(")
                self.result += "("
            else:
                self.ui.pushButton_eq.setEnabled(False)
                self.ui.label_input.setText(self.ui.label_input.text() + "×(")
                self.result += "*("
        try:
            self.total = eval(self.result)
            self.ui.label_up.setText(str(self.total)) 
        except Exception:
            self.ui.label_up.setText("")
            
    def plus_minus(self):
        self.length_label_text()
        if self.ui.label_input.text() == "" or self.ui.label_up.text() == "0":
            self.ui.label_input.setText("(-")
            self.result += "(-"
        else:
            if self.result[-1] in ['+', '-', '*', '/', '%']:
                self.ui.label_input.setText(self.ui.label_input.text() + "(-")
                self.result += "(-"
                
            else:
                self.input = self.ui.label_input.text()[:-(len(self.int))] + "(-" + self.int
                self.ui.label_input.setText(self.input)
                self.result = self.result[:-(len(self.int))] + "(-" + self.int
        self.i += 1
        try:
            self.total = eval(self.result)
            self.ui.label_up.setText(str(self.total)) 
        except Exception:
            self.ui.label_up.setText("")
            
    def length_label_text(self):
        text = self.ui.label_input.text()
        if len(text) > self.max_length:
            text = text[:self.max_length+1]
            self.reset_buttons()
            self.reset_numbers(False)
            self.ui.pushButton_pm.setEnabled(False)
            self.ui.pushButton_eq.setEnabled(True)
            if self.i % 2 == 0:
                self.ui.pushButton_p.setEnabled(False)
        self.ui.label_input.setText(text)
    
    def format_large_number(number):
        if abs(number) >= 1e15 or (number != 0 and abs(number) < 1e-15):
            return "{:.5e}".format(number)
        return str(number)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())