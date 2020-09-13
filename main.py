import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from conveter import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__() #возвращает метод супер возвращает рдительский класс currencyconv и вызывает конструктор
        self.conveter = Ui_MainWindow()
        self.conveter.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Конвертор валют')
        self.setWindowIcon(QIcon('lr.png')) #импорт иконки для приложения

        self.conveter.input_currency.setPlaceholderText('Из валюты:') #для 4х полей метод setPlaceholderText
        self.conveter.input_amount.setPlaceholderText('У меня есть:')
        self.conveter.output_currency.setPlaceholderText('В валюту:')
        self.conveter.output_amount.setPlaceholderText('Я получу:')
        self.conveter.pushButton.clicked.connect(self.converter1)

    def converter1(self):
        c = CurrencyConverter()
        input_currency = self.conveter.input_currency.text()
        output_carrency = self.conveter.output_currency.text()
        input_amount = int(self.conveter.input_amount.text())
       # output_amount = int(self.conveter.output_amount.text())
        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_carrency)), 2)

        self.conveter.output_amount.setText(str(output_amount))


#по умолчанию QApplication
app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
#основной цикл обработки и выход из него
sys.exit(app.exec())