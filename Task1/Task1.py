# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import *

def determine_coefficient (coef_list):
    random_index = randint(0, len(coef_list) - 1)
    coefficient = coef_list[random_index]
    return str(coefficient)

def write_and_print(string):
    print(string, end='')
    file.write(string)

def write_print_and_line_break(string):
    print(string + '\n')
    file.write(string + '\n')

k = input('Введите значение степени: ')
while int(k)<1:
    if k=='0':
        print('>>>>>>> Многочленом нулевой степени является любое отличное от нуля число.')
    k = input('Введите значение степени (больше или равно 1): ')

print()

degree = int(k)
symbols = '+-'

file = open('Task1.txt', 'w')

coef_list = []
for i in range(randint(0,100)):
    coef_list.append(randint(0, 100))

free_number = randint(0,100)
coefficient = ''

# Создается основная часть первой строки по типу COEFx**k + COEFx**k-1 + ... + COEFx**3 + COEFx**2 + COEFx
for current_degree in range(degree, 0, -1):

    # Создаётся часть первой строки по типу COEFx**k + COEFx**k-1 + ... + COEFx**3 + COEFx**2
    if current_degree != 1:
        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0':
            write_and_print(coefficient + 'x**' + str(current_degree) + f' {choice(symbols)} ')
        elif coefficient == '1':
            write_and_print('x**' + str(current_degree) + f' {choice(symbols)} ')
        elif coefficient == '0':
            write_and_print('')

    # Создаётся часть первой строки по типу COEFx
    else:
        coefficient = determine_coefficient(coef_list)
        if free_number != 0:
            if coefficient != '1' and coefficient != '0':
                write_and_print(coefficient + 'x' + f' {choice(symbols)} ')
            elif coefficient == '1':
                write_and_print('x' + f' {choice(symbols)} ')
            elif coefficient == '0':
                write_and_print('')
        else:
            if coefficient != '1' and coefficient != '0':
                write_and_print(coefficient + 'x ')
            elif coefficient == '1':
                write_and_print('x ')
            elif coefficient == '0':
                write_and_print('')

# К первой строке добавляется (или не добавляется) свободный член, добавляется '= 0', или же выводится сообщение о нулевом коэффициенте при стени k, равной 1.
# Первая проверка добавляет свободный член к первой строке, если сам свободный член не равен нулю и степень k не равна нулю.
# Далее три проверки предотвращают некорректный вывод первой строки с многочленом первой степени (это частные случаи).
if free_number != 0 and k!='1':
    write_print_and_line_break(str(free_number) + ' = 0')
elif free_number != 0 and coefficient != '1' and coefficient != '0' and k=='1':
    write_print_and_line_break(str(free_number) + ' = 0')
elif free_number != 0 and coefficient == '1' and k=='1':
    write_print_and_line_break(str(free_number) + ' = 0')
elif free_number != 0 and coefficient == '0' and k=='1':
    print('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
else:
    write_print_and_line_break('= 0')

# Далее идёт генерация второй и третьей строк по типу 'COEFn**k + 25 = 0' и 'COEFn**k = 0'
# Главный оператор if проверяет, является ли свободный член нулевым. Если он окажется нулевым, то напечатается лишь одна строка,
# так как строка по типу 'COEFn**k + 0 = 0' смысла не имеет. Достаточно строки 'COEFn**k = 0'.
if free_number != 0:

    # Конкретно эта проверка предотвращает некорректный вывод в случае, если степень k равна 2 (так как в ходе генерации
    # первой строки при степени k, равной 2, она получается идентичной второй строке).
    if k == '2':

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0':
            write_print_and_line_break(coefficient + 'x**' + str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0')
        elif coefficient == '0':
            print('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            write_print_and_line_break('x**' +  str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0')

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0':
            write_print_and_line_break(coefficient + 'x**' + str(degree) + ' = 0')
        elif coefficient == '0':
            print('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            write_print_and_line_break('x**' + str(degree) + ' = 0')

    # Здесь создаются сразу две строки по типу 'COEFn**k + 25 = 0' и 'COEFn**k = 0' для всех степеней k, которые больше 1 и 2.
    elif k != '1' and k != '2':

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0':
            write_print_and_line_break(coefficient + 'x**' + str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0')
        elif coefficient == '0':
            print('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            write_print_and_line_break('x**' + str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0')

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0':
            write_print_and_line_break(coefficient + 'x**' + str(degree) + ' = 0')
        elif coefficient == '0':
            print('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            write_print_and_line_break('x**' + str(degree) + ' = 0')

    # Данная проверка выводит вторую строку в случае, если степень k равна 1. Вообще говоря, в этом случае выведутся лишь две строки по типу 
    # 'COEFx + 25 = 0' и 'COEFx = 0'. Конкретно эта проверка определяет, какой коэффициент будет стоять перед иксом в строке типа 'COEFx = 0'.
    elif k == '1':

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0':
            write_print_and_line_break(coefficient + 'x' + ' = 0')
        elif coefficient == '0':
            print('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            write_print_and_line_break('x' + ' = 0')
else:

    if k != '1':
        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0':
            write_print_and_line_break(coefficient + 'x**' + str(degree) + ' = 0')
        elif coefficient == '0':
            print('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            write_print_and_line_break('x**' + str(degree) + ' = 0')

    elif k == '1':
        print('', end='')

file.close()


