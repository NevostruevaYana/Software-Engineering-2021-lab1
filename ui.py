from PyQt5 import QtCore, QtGui, QtWidgets

color = "#9c9c9c"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 550)
        MainWindow.setStyleSheet("background-color: ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e;")
        self.centralwidget.setObjectName("centralwidget")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 230, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: #22222e;\n"
                                        "border: 5px solid " + color + ";\n"
                                                                       "border-radius: 20;\n"
                                                                       "color: white;")
        self.input_amount.setText("")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(50, 370, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: #22222e;\n"
                                         "border: 5px solid " + color + ";\n"
                                                                        "border-radius: 20;\n"
                                                                        "color: white;")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 470, 380, 60))
        self.pushButton.setObjectName("button")
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "color: white;\n"
                                      "background-color: " + color + ";\n"
                                                                     "border-radius: 20;}\n"
                                                                     "QPushButton:pressed {\n"
                                                                     "background-color: " + color + ";}")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 130))
        self.frame.setStyleSheet("background-color: " + color + "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 180, 191, 171))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 0, 431, 91))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #16082f; font-size: 40px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 85, 421, 40))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 160, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: #22222e;\n"
                                          "border: 5px solid " + color + ";\n"
                                                                         "border-radius: 20;\n"
                                                                         "color: white;")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 300, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: #22222e;\n"
                                           "border: 5px solid " + color + ";\n"
                                                                          "border-radius: 20;\n"
                                                                          "color: white;")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CONVERT"))
        self.label_2.setText(_translate("MainWindow", "Currency Converter"))
        self.label_3.setText(_translate("MainWindow", "USD EUR AUD AZN AMD BYN BGN BRL HUF KRW HKD DKK INR KZT CAD KGS CNY\n"
                                                      "MDL TMT NOK PLN RON XDR SGD TJS TRY UZS UAH GBP CZK SEK CHF ZAR JPY"))
        self.label_3.setStyleSheet(''' font-size: 10px; color: white; ''')