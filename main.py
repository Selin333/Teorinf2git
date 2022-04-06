from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtWinExtras import QtWin
import binascii
myappid = 'kodirovka'
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
from calc import Ui_MainWindow  # импорт ui
import sys

summators_str = []
global b
b = 0
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
    def btnClicked(self):

        get_kol_sum(self.ui.lineEdit_2.text())

        print(get_summators(self.ui.lineEdit_4.text()))
        if b ==kol_sum:
            self.ui.lineEdit_3.setText(encoding(self.ui.lineEdit.text()))


    def btnClicked_2(self):
        self.ui.lineEdit_5.setText(decoding())


        # Ошибки
        def Error(info):
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Ошибка")
            error.setInformativeText(info)
            error.setWindowTitle("Ой-йой")
            error.exec_()
def encoding(primal_text):
    global spisok_text_to_bit


    def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    spisok_text_to_bit = text_to_bits(primal_text)
    print(spisok_text_to_bit)
    spisok_polinomov = []
    spisok_polinov_do_sumpomod2 = []
    spisok_indeksov_edinic = []

    # Из списка битов вытаскиваем индексы единиц для кодирования полиномами
    for i in range(len(spisok_text_to_bit)):
        if spisok_text_to_bit[i] == '1':
            spisok_indeksov_edinic.append(i)

    print(spisok_indeksov_edinic)
    print(summators)
    print("!!!")
# делам "умножение полиномов степени "
    for i in range(len(summators)):
        for j in range(len(summators[i])):
            for m in range(len(spisok_indeksov_edinic)):
                spisok_polinomov.append(spisok_indeksov_edinic[m] + summators[i][j])
        # возможно ненуджно
        # это Ci(x)
        spisok_polinov_do_sumpomod2.append(spisok_polinomov)
        spisok_polinomov = []

    # сложение по модулю 2 полиномов добавляет толко нечет кол раз встреачются эл
    for i in range(len(spisok_polinov_do_sumpomod2)):
        f = []
        for j in spisok_polinov_do_sumpomod2[i]:
            if (spisok_polinov_do_sumpomod2[i].count(j) % 2) != 0:
                f.append(j)
        f = list(set(f))
        spisok_polinomov.append(f)
    # с1(x) с2(x)
    print(spisok_polinomov)
    # нахождение макс элемента из массива полиномов
    encoded_string = []
    max_el = 0
    for i in spisok_polinomov:
        if max_el < max(i):
            max_el = max(i)
    i = 0
    # Если в одном из вложенных массивов встречается i-тое число то добавляем 1, иначе 0
    while i <= max_el:
        encoded_list = []
        for j in range(len(spisok_polinomov)):
            if i in spisok_polinomov[j]:
                encoded_list += ''.join('1')
            elif i not in spisok_polinomov[j]:
                encoded_list += ''.join('0')
        i += 1
        encoded_string.append(encoded_list)
    # Собираем в красивую конструкцию и выводим из под функции
    global encoded_string_finished
    encoded_string_finished = ''
    print(encoded_string)
    for j in range(len(encoded_string)):
        encoded_string_finished += ''.join(encoded_string[j])
    # каждый символ заносим в функцию возращая список закодированных символов
    encoded_string_finished2 = encoded_string_finished[:-1]

    encoded_string_finished = encoded_string_finished[:-1]
    print(encoded_string_finished)
    encoded_string_finished = encoded_string_finished.split('.')
    print(encoded_string_finished)

    return encoded_string_finished2
def decoding():
    # обьявляем переменные
    global registrs
    registrs = []
    kol_registrov = 0
    global decoded_string
    decoded_string = ''
    # находим кол-во регистров по максимальному элементу в сумматоре и обнуляем их
    for i in summators:
        if kol_registrov < max(i):
            kol_registrov = max(i)

    for i in range(kol_registrov + 1):
        registrs.append(0)
# функция сдвига регистров в парво
    def append_zero():
        for i in reversed(range(len(registrs))):
            registrs[i] = registrs[i - 1]
        registrs[0] = 0
        return registrs

    # функция создание проверочных битов
    def calc_prov_bits():
        global proverochnie_bits
        proverochnie_bits = ''
        for j in range(len(summators)):
            c = 0
            for m in range(len(summators[j])):
                c += registrs[summators[j][m]]
            if c % 2 == 1:
                proverochnie_bits += ''.join('1')
            elif c % 2 == 0:
                proverochnie_bits += ''.join('0')
        return proverochnie_bits

    # функция декодирование строки
    for i in range(len(encoded_string_finished)):
        append_zero()
        calc_prov_bits()
        if proverochnie_bits != encoded_string_finished[i]:
            registrs[0] = 1
            decoded_string += ''.join('1')
        elif proverochnie_bits == encoded_string_finished[i]:
            decoded_string += ''.join('0')

    print(decoded_string)
# функции перевода двоичной строки обратно в текст
    if decoded_string != spisok_text_to_bit:
        dlina = len(decoded_string) - len(spisok_text_to_bit)
        decoded_string = decoded_string[:-dlina]

    def text_from_bits(binstring, encoding='utf-8', errors='surrogatepass'):
        n = int(binstring, 2)
        return int2bytes(n).decode(encoding, errors)

    def int2bytes(i):
        hex_string = '%x' % i
        n = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

    decoded_primal_text = text_from_bits(decoded_string)

    print(decoded_primal_text)
    return decoded_primal_text