# Расширить значение коэффициентов до [-100..100]

from random import *

def determine_coefficient (coef_list):
    random_index = randint(0, len(coef_list) - 1)
    coefficient = coef_list[random_index]
    return str(coefficient)

k = input('Введите значение степени: ')
while int(k)<1:
    if k=='0':
        print('>>>>>>> Многочленом нулевой степени является любое отличное от нуля число.')
    k = input('Введите значение степени (больше или равно 1): ')

print()

degree = int(k)
symbols = '+-'

file = open('Task3.txt', 'w')

# Создаются коэффициенты от -100 до 100
coef_list = []
for i in range(randint(0,100)):
    coef_list.append(randint(-100, 100))

free_number = randint(0,100)
coefficient = ''

# Создается основная часть первой строки по типу COEFx**k + COEFx**k-1 + ... + COEFx**3 + COEFx**2 + COEFx
for current_degree in range(degree, 0, -1):

    # Создаётся часть первой строки по типу COEFx**k + COEFx**k-1 + ... + COEFx**3 + COEFx**2
    if current_degree != 1:
        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0' and coefficient != '-1':
            file.write(coefficient + 'x**' + str(current_degree) + f' {choice(symbols)} ')
        elif coefficient == '1':
            file.write('x**' + str(current_degree) + f' {choice(symbols)} ')
        elif coefficient == '-1':
            file.write('-x**' + str(current_degree) + f' {choice(symbols)} ')
        elif coefficient == '0':
            file.write('')

    # Создаётся часть первой строки по типу COEFx
    else:
        coefficient = determine_coefficient(coef_list)
        if free_number != 0:
            if coefficient != '1' and coefficient != '0' and coefficient != '-1':
                file.write(coefficient + 'x' + f' {choice(symbols)} ')
            elif coefficient == '1':
                file.write('x' + f' {choice(symbols)} ')
            elif coefficient == '-1':
                file.write('x' + f' {choice(symbols)} ')
            elif coefficient == '0':
                file.write('')
        else:
            if coefficient != '1' and coefficient != '0':
                file.write(coefficient + 'x ')
            elif coefficient == '1':
                file.write('x ')
            elif coefficient == '0':
                file.write('')

# К первой строке добавляется (или не добавляется) свободный член, добавляется '= 0', или же выводится сообщение о нулевом коэффициенте при стени k, равной 1.
# Первая проверка добавляет свободный член к первой строке, если сам свободный член не равен нулю и степень k не равна нулю.
# Далее три проверки предотвращают некорректный вывод первой строки с многочленом первой степени (это частные случаи).
if free_number != 0 and k!='1':
    file.write(str(free_number) + ' = 0\n')
elif free_number != 0 and coefficient != '1' and coefficient != '0' and k=='1':
    file.write(str(free_number) + ' = 0\n')
elif free_number != 0 and coefficient == '1' and k=='1':
    file.write(str(free_number) + ' = 0\n')
elif free_number != 0 and coefficient == '0' and k=='1':
    file.write('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
else:
    file.write('= 0\n')

# Далее идёт генерация второй и третьей строк по типу 'COEFn**k + 25 = 0' и 'COEFn**k = 0'
# Главный оператор if проверяет, является ли свободный член нулевым. Если он окажется нулевым, то напечатается лишь одна строка,
# так как строка по типу 'COEFn**k + 0 = 0' смысла не имеет. Достаточно строки 'COEFn**k = 0'.
if free_number != 0:

    # Конкретно эта проверка предотвращает некорректный вывод в случае, если степень k равна 2 (так как в ходе генерации
    # первой строки при степени k, равной 2, она получается идентичной второй строке).
    if k == '2':

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0' and coefficient != '-1':
            file.write(coefficient + 'x**' + str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0\n')
        elif coefficient == '0':
            file.write('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            file.write('x**' +  str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0\n')
        elif coefficient == '-1':
            file.write('-x**' +  str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0\n')

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0' and coefficient != '-1':
            file.write(coefficient + 'x**' + str(degree) + ' = 0\n')
        elif coefficient == '0':
            file.write('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            file.write('x**' + str(degree) + ' = 0\n')
        elif coefficient == '-1':
            file.write('-x**' + str(degree) + ' = 0\n')

    # Здесь создаются сразу две строки по типу 'COEFn**k + 25 = 0' и 'COEFn**k = 0' для всех степеней k, которые больше 1 и 2.
    elif k != '1' and k != '2':

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0' and coefficient != '-1':
            file.write(coefficient + 'x**' + str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0\n')
        elif coefficient == '0':
            file.write('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            file.write('x**' + str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0\n')
        elif coefficient == '-1':
            file.write('-x**' + str(degree) + f' {choice(symbols)} ' + str(free_number) + ' = 0\n')

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0' and coefficient != '-1':
            file.write(coefficient + 'x**' + str(degree) + ' = 0\n')
        elif coefficient == '0':
            file.write('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            file.write('x**' + str(degree) + ' = 0\n')
        elif coefficient == '-1':
            file.write('-x**' + str(degree) + ' = 0\n')

    # Данная проверка выводит вторую строку в случае, если степень k равна 1. Вообще говоря, в этом случае выведутся лишь две строки по типу 
    # 'COEFx + 25 = 0' и 'COEFx = 0'. Конкретно эта проверка определяет, какой коэффициент будет стоять перед иксом в строке типа 'COEFx = 0'.
    elif k == '1':

        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0' and coefficient != '-1':
            file.write(coefficient + 'x' + ' = 0\n')
        elif coefficient == '0':
            file.write('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            file.write('x' + ' = 0\n')
        elif coefficient == '-1':
            file.write('-x' + ' = 0\n')
else:

    if k != '1':
        coefficient = determine_coefficient(coef_list)
        if coefficient != '1' and coefficient != '0' and coefficient != '-1':
            file.write(coefficient + 'x**' + str(degree) + ' = 0\n')
        elif coefficient == '0':
            file.write('Программа выдала нулевой коэффициент, невозможно записать выражение в файл\n')
        elif coefficient == '1':
            file.write('x**' + str(degree) + ' = 0\n')
        elif coefficient == '1':
            file.write('-x**' + str(degree) + ' = 0\n')


file.close()

file = open('Task3.txt', 'r')
file_strings = []

# Считываю пока ещё неотформатированные строки из текстового файла. Форматирую повторяющиеся минусы (один минус пока что является арифметическим знаком,
# второй минус пока принадлежит отрицательному коэффициенту) и идущие сразу после друг друга плюс и минус.
# Конечный результат выводится в программе, а затем уже отформатированные строки по новой заносятся в текстовый файл.
while True:
    line = file.readline().replace('- -', '+ ').replace('+ -', '- ')
    if not line:
        break
    file_strings.append(line)
    print(line)

file = open('Task3.txt', 'w')

for string in file_strings:
    file.write(string)

file.close()