# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

polynomial1 = open('Task2 (file 1).txt', 'r')
polynomial2 = open('Task2 (file 2).txt', 'r')

print('Первый исходный многочлен: ' + polynomial1.readline())
print('Второй исходный многочлен: ' + polynomial2.readline())

# Сразу разделяю строки из документов по символам ' + '. Убираю равно и ноль. Если множителю предществует минус, то ' - ' превращается в ' + -'.
# Это поможет сделать так, чтобы коэффициент добавился сразу отрицательным.
polynomial1 = open('Task2 (file 1).txt', 'r').readline().replace(' = 0', '').replace(' - ', ' + -').split(' + ')
polynomial2 = open('Task2 (file 2).txt', 'r').readline().replace(' = 0', '').replace(' - ', ' + -').split(' + ')

dict_1 = {}
dict_2 = {}
coefs_sum_list = []
symbols = '+-'

min_length = 0
max_length = 0
min_polynomial = []
max_polynomial = []

# Определение, какой из многочленов имеет больше множителей
if len(polynomial1) < len(polynomial2):
    min_length = len(polynomial1)
    max_length = len(polynomial2)
    min_polynomial = polynomial1
    max_polynomial = polynomial2
else:
    min_length = len(polynomial2)
    max_length = len(polynomial1)
    min_polynomial = polynomial2
    max_polynomial = polynomial1

# Сборка словарей
for degree in range(len(polynomial1)-1, -1, -1):
    member = len(polynomial1)-1-degree
    dict_1[degree] = polynomial1[member].replace(f'x**{degree}', '').replace(f'x', '')

for degree in range(len(polynomial2)-1, -1, -1):
    member = len(polynomial2)-1-degree
    dict_2[degree] = polynomial2[member].replace(f'x**{degree}', '').replace(f'x', '')

# Сборка списка
for degree in range(min_length-1, -1, -1):
    value_1 = str(dict_1[degree])
    value_2 = str(dict_2[degree])
    if value_1 != '' and value_2 != '':
        coefs_sum_list.append(int(value_1) + int(value_2))
    elif value_1 != '' and value_2.isdigit() == '':
        coefs_sum_list.append(int(value_1))
    elif value_1 == '' and value_2 != '':
        coefs_sum_list.append(int(value_2))

# Добавление первых элементов из многочлена с большим количеством множителей к строке с суммой коэффициентов (например, если в одном многочлене 7 множителей, а в другом - 5, 
# то строка с суммой коэффициентов сложится сначала из суммы пяти коэффициентов, а потом в начало строки добавятся ещё два коэффициента от членов со степенями 5 и 6.
# Именно со степенями 5 и 6, потому что свободный член умножается на икс в какой-либо степени)
for i in range(max_length-min_length-1, -1, -1):
    coefs_sum_list.insert(0, str(max_polynomial[i].replace(f'x**{max_length-1-i}', '')))

# Добавление к коэффициентам в списке хвоста 'x**{степень}' или 'x'
for i in range(len(coefs_sum_list)):
    member = len(coefs_sum_list) - 1 - i
    if member != 1 and member != 0:
        coefs_sum_list[i] = str(coefs_sum_list[i]) + f'x**{member}'
    elif member == 1:
        coefs_sum_list[i] = str(coefs_sum_list[i]) + f'x'
    elif member == 0:
        coefs_sum_list[i] = str(coefs_sum_list[i])

# Формирование строки с итоговой суммой множителей
result = ' + '.join(coefs_sum_list) + ' = 0'

result = result.replace(' 0x', ' x')
result = result.replace(' 1x', ' x')

print('Сумма многочленов: ' + result)