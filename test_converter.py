import unittest
from converter import USDEURConverter
from main import CurrencyConv
import sys
from PyQt5 import QtCore, QtWidgets, QtTest

app = QtWidgets.QApplication(sys.argv)


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.form = CurrencyConv()

    def test_ui(self):
        self.assertEqual(self.form.ui.output_amount.text(), "")
        self.assertEqual(self.form.ui.input_amount.text(), "")
        self.assertEqual(self.form.ui.output_currency.text(), "")
        self.assertEqual(self.form.ui.input_currency.text(), "")
        self.assertEqual(self.form.ui.label_2.text(), "Currency Converter")
        self.assertEqual(self.form.ui.label_3.text(), "USD EUR AUD AZN AMD BYN BGN BRL HUF KRW HKD DKK INR KZT CAD KGS CNY\n"
                                                      "MDL TMT NOK PLN RON XDR SGD TJS TRY UZS UAH GBP CZK SEK CHF ZAR JPY")
        self.assertEqual(self.form.ui.pushButton.text(), "CONVERT")

    def test_ui_1(self):
        self.form.ui.input_currency.setText("usd")
        self.form.ui.input_amount.setText("45")
        self.form.ui.output_currency.setText("eur")
        QtTest.QTest.mouseClick(self.form.ui.pushButton, QtCore.Qt.LeftButton)
        self.assertEqual(self.form.ui.output_amount.text(), "40.5")

    def test_ui_2(self):
        self.form.ui.input_currency.setText("USD")
        self.form.ui.input_amount.setText("45")
        self.form.ui.output_currency.setText("TRY")
        QtTest.QTest.mouseClick(self.form.ui.pushButton, QtCore.Qt.LeftButton)
        self.assertEqual(self.form.ui.output_amount.text(), "576.0")

    def test_ui_3(self):
        self.form.ui.input_currency.setText("gfh")
        self.form.ui.input_amount.setText("45")
        self.form.ui.output_currency.setText("fff")
        QtTest.QTest.mouseClick(self.form.ui.pushButton, QtCore.Qt.LeftButton)
        self.assertEqual(self.form.ui.output_amount.text(), "Invalid currency")

    def test_ui_4(self):
        self.form.ui.input_currency.setText("USD")
        self.form.ui.input_amount.setText("hhh")
        self.form.ui.output_currency.setText("TRY")
        QtTest.QTest.mouseClick(self.form.ui.pushButton, QtCore.Qt.LeftButton)
        self.assertEqual(self.form.ui.output_amount.text(), "Invalid amount")

    def test_ui_5(self):
        self.form.ui.input_currency.setText("USD")
        self.form.ui.input_amount.setText("45")
        self.form.ui.output_currency.setText("TRY")
        QtTest.QTest.mouseClick(self.form.ui.pushButton, QtCore.Qt.LeftButton)
        self.assertEqual(self.form.ui.output_amount.text(), "576.0")

    def test_calculate_value(self):
        self.assertEqual(USDEURConverter.calculate_value(3, 4), 12)
        self.assertEqual(USDEURConverter.calculate_value(13, 2), 26)
        self.assertEqual(USDEURConverter.calculate_value(3, 8), 24)

    def test_check_curr(self):
        self.assertEqual(USDEURConverter.check_currency("USD", "EU"), "Invalid currency")
        self.assertEqual(USDEURConverter.check_currency("try", "aud"), "0.1")
        self.assertEqual(USDEURConverter.check_currency("usd", "eur"), "0.9")
