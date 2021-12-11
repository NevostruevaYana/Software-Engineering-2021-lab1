import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from converter import USDEURConverter


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Конвертер Валют")
        self.setWindowIcon(QIcon("my.png"))
        self.ui.input_currency.setPlaceholderText("from")
        self.ui.input_amount.setPlaceholderText("amount")
        self.ui.output_currency.setPlaceholderText("to")
        self.ui.output_amount.setPlaceholderText("answer")
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        input_currency = self.ui.input_currency.text()
        input_amount = int(self.ui.input_amount.text())
        output_currency = self.ui.output_currency.text()

        currency = USDEURConverter.check_currency(input_currency.lower(), output_currency.lower())
        if currency == "Invalid currency":
            self.ui.output_amount.setText(currency)
        else:
            float_currency = float(currency)
            answer = USDEURConverter.calculate_value(float_currency, float(input_amount))
            self.ui.output_amount.setText(str(answer))


if __name__ == "__main__":
    ui = QtWidgets.QApplication([])
    app = CurrencyConv()
    app.show()

    sys.exit(ui.exec_())