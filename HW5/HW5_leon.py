# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

f = open("file#1.txt", 'w')

while not False:
    inp = input('введите : ')
    f.writelines(inp + '\n')
    if len(inp) == 0:
        break
f.close()
print('записано в файл "file#1.txt"')


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.

# f = open("file#2.txt")
# l = 0
# for line in f.readlines():
#     print(line[:-1])
# f.close()
# f = open("file#2.txt")
# print('Количество слов')
# for line in f.readlines():
#     l += 1
#     print(f'{l} : {len(line.split())}')
# print(f'строк: ', l)
# f.close()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
# сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

# sallarySum = 0
# workersCount = 0
# f = open("file#3.txt")
# print('имеет оклад менее 20 тыс:\n')
# for line in f.readlines():
#     Linelist = line.split()
#     Linelist[1] = Linelist[1].replace(",", ".")
#     sallarySum += float(Linelist[1])
#     workersCount += 1
#     if float(Linelist[1]) < 20000:
#         print(Linelist[0])
# print('\nсредний оклад: {:,.2f}'.format(sallarySum / workersCount).replace(',', ' '))
# f.close()

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

# dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# fIn = open("file#4.txt")
#
# with open("file#4_1.txt", 'w') as fOut:
#     for line in fIn.readlines():
#         Linelist = line.split()
#         Linelist[0] = dict[Linelist[0]]
#         fOut.writelines(Linelist[0] + " " + Linelist[1] + " " + Linelist[2] + '\n')
# fIn.close()

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами
# . Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def decDelim(nbr):
    '''переводит число в формат ХХХ ХХХ.ХХ для последующего вывода'''
    return '{0:,.2f}'.format(float(str(nbr).replace(',', '.'))).replace(',', ' ')

# import random
#
# with open("file#5.txt", 'w') as fOut:
#     i = 0                                     # запись чисел в файл
#     while i < 100:
#         i += 1
#         fOut.writelines(str('{:.2f}'.format(random.random()*100))+' ')
#
# with open("file#5.txt") as fOut:
#     sum = 0                                   # подсчет суммы чисел в файле
#     for i in fOut.readline().split():
#         sum += float(i)
#     print(' Сумма чиспел зз файла "file#5.txt" : ', decDelim(sum))

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# def is_digit(string):
#     if string.isdigit():
#         return True
#     else:
#         try:
#             float(string)
#             return True
#         except ValueError:
#             return False
#
# def splitHours(mess):
#     hours = {'(л)': 0, '(пр)': 0, '(лаб)': 0}
#     for Ltype in hours.keys():
#         i = 1
#         while is_digit(mess[mess.find(Ltype) - i - 1: mess.find(Ltype)]) and (mess.find(Ltype) != -1):
#             hours[Ltype] = int(mess[mess.find(Ltype) - i: mess.find(Ltype)])
#             i += 1
#     return hours
#
# disciplines = {'Информатика': 0,
#                'Пение': 0,
#                'Рисование': 0,
#                'Физика': 0,
#                'Физкультура': 0,
#                'Химия': 0}
# print()
# with open("file#6.txt") as f:
#     for line in f.readlines():
#         print(line[:-1])
#         sumHours = 0
#
#         for lessonType in splitHours(line.split(':')[1]):
#             sumHours += splitHours(line.split(':')[1])[lessonType]
#         disciplines[line.split(':')[0]] = sumHours
#     print()
#     for i in disciplines:
#         print(f'{i} : {disciplines[i]}')

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
# средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

# firmsProf = [{}, {'average_profit': 0}]
#
# import json
#
# sumProfit = 0   # суммарная прибыль прибыльных фирм
# Profitable = 0  # количество прибыльных фирм
# print(' Фирмы с прибылью :\n')
# with open("file#7.txt") as f:
#     for line in f.readlines():
#         firms = line.split()
#         profit = float(firms[2]) - float(firms[3])
#         firmsProf[0].update({firms[0]: profit})
#         if profit > 0:
#             sumProfit += profit
#             Profitable += 1
#             print(firms[0], decDelim(profit))
#             firmsProf[0].update()
#     firmsProf[1]['average_profit'] = sumProfit / Profitable
#     print('\nсредняя прибыль всех безубыточных фирм :', decDelim(firmsProf[1]['average_profit']))
#
# with open("file#8.txt", 'w') as f:
#     json.dump(firmsProf, f)
#     print('\nсоздан файл "file#8.txt" ')
