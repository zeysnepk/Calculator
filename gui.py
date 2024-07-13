
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(410, 670)
        MainWindow.setMinimumSize(QtCore.QSize(410, 670))
        MainWindow.setMaximumSize(QtCore.QSize(410, 670))
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color: rgb(227, 185, 174);\n"
"}")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 160, 80, 80))
        self.pushButton.setStyleSheet("#pushButton{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:34px;\n"
"}\n"
"#pushButton:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:24px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_pm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pm.setGeometry(QtCore.QRect(120, 160, 80, 80))
        self.pushButton_pm.setStyleSheet("#pushButton_pm{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:34px;\n"
"}\n"
"#pushButton_pm:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:24px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_pm.setObjectName("pushButton_pm")
        self.pushButton_per = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_per.setGeometry(QtCore.QRect(210, 160, 80, 80))
        self.pushButton_per.setStyleSheet("#pushButton_per{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:34px;\n"
"}\n"
"#pushButton_per:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:24px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_per.setObjectName("pushButton_per")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(300, 160, 80, 80))
        self.pushButton_div.setStyleSheet("#pushButton_div{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:46px;\n"
"}\n"
"#pushButton_div:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:36px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_multi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multi.setGeometry(QtCore.QRect(300, 250, 80, 80))
        self.pushButton_multi.setStyleSheet("#pushButton_multi{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:40px;\n"
"}\n"
"#pushButton_multi:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:30px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_multi.setObjectName("pushButton_multi")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(300, 340, 80, 80))
        self.pushButton_minus.setStyleSheet("#pushButton_minus{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:40px;\n"
"}\n"
"#pushButton_minus:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:30px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(300, 430, 80, 80))
        self.pushButton_plus.setStyleSheet("#pushButton_plus{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:40px;\n"
"}\n"
"#pushButton_plus:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:30px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_eq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eq.setGeometry(QtCore.QRect(300, 520, 80, 80))
        self.pushButton_eq.setStyleSheet("#pushButton_eq{\n"
"    background-color: rgb(148, 93, 101);\n"
"    border-radius: 25px;\n"
"    font-size:40px;\n"
"}\n"
"#pushButton_eq:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:30px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(210, 520, 80, 80))
        self.pushButton_dot.setStyleSheet("#pushButton_dot{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:40px;\n"
"}\n"
"#pushButton_dot:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:30px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_p = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_p.setGeometry(QtCore.QRect(30, 520, 80, 80))
        self.pushButton_p.setStyleSheet("#pushButton_p{\n"
"    background-color: rgb(195, 130, 139);\n"
"    border-radius: 25px;\n"
"    font-size:34px;\n"
"}\n"
"#pushButton_p:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:24px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_p.setObjectName("pushButton_p")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(120, 520, 80, 80))
        self.pushButton_0.setStyleSheet("#pushButton_0{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_0:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 430, 80, 80))
        self.pushButton_1.setStyleSheet("#pushButton_1{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_1:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 430, 80, 80))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_2:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 430, 80, 80))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_3:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 340, 80, 80))
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_4:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 340, 80, 80))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_5:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 340, 80, 80))
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_6:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 250, 80, 80))
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_7:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 250, 80, 80))
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_8:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 250, 80, 80))
        self.pushButton_9.setStyleSheet("#pushButton_9{\n"
"    background-color: rgb(249, 228, 227);\n"
"    color: rgb(226, 177, 180);\n"
"    border-radius: 25px;\n"
"    font-size:44px;\n"
"}\n"
"#pushButton_9:hover {\n"
"    background-color: rgb(237, 211, 212);\n"
"    font-size:34px; \n"
"    color: white;\n"
"\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_input = QtWidgets.QLabel(self.centralwidget)
        self.label_input.setGeometry(QtCore.QRect(30, 90, 340, 50))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_input.setFont(font)
        self.label_input.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_input.setScaledContents(False)
        self.label_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_input.setWordWrap(True)
        self.label_input.setIndent(-1)
        self.label_input.setObjectName("label_input")
        self.label_up = QtWidgets.QLabel(self.centralwidget)
        self.label_up.setGeometry(QtCore.QRect(30, 60, 340, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_up.setFont(font)
        self.label_up.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_up.setObjectName("label_up")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "C"))
        self.pushButton_pm.setText(_translate("MainWindow", "+/-"))
        self.pushButton_per.setText(_translate("MainWindow", "%"))
        self.pushButton_div.setText(_translate("MainWindow", "÷"))
        self.pushButton_multi.setText(_translate("MainWindow", "x"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_eq.setText(_translate("MainWindow", "="))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_p.setText(_translate("MainWindow", "( )"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.label_input.setText(_translate("MainWindow", ""))
        self.label_up.setText(_translate("MainWindow", ""))
import pic_rc
