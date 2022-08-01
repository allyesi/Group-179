# Задание 1
# Создайте кортеж из случайных 10 чисел. Найдите его максимальный и минимальный элемент
# import random
# tup = tuple([random.randint(1,10) for i in range(10)])
# print(tup)
# print("min:",min(tup),"max:",max(tup))
# Задание 2
# Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0.
# Объедините два кортежа с помощью оператора +, создав тем самым третий
# кортеж. С помощью метода кортежа count() определите в нем количество
# нулей. Выведите на экран третий кортеж и количество нулей в нем.
# tup1 = tuple([random.randint(0,5) for _ in range(10)])
# tup2 = tuple([random.randint(-5,0) for _ in range(10)])
# tup3 = tup1 + tup2
# print(tup3," \nколичество нулей", tup3.count(0))   # \n - перенос в консоли на следующую строчку

# Задание 3
# Вывести данные кортежа без скобок, через запятую.
# Обязательно: элементы кортежа – строки.
# tup = ("fun","bad", "fat")
# print(tup)
# c = "  ".join(tup)
# print(c)

# Даны два кортежа:
# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран ( Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных элементов этих
# кортежей
# sum_A = sum(A)
# sum_B = sum(B)
# if sum_B > sum_A:
#     print("Cумма больше в котреже B:",sum_B)
# else:
#     print("Cумма больше в котреже А:",sum_A)
# print("minA:", min(A),"индекс" , A.index(min(A)),"min B:" , min(B), B.index(min(B)))

# 1)Создайте  кортеж с цифрами от 0 до 9 и посчитайте сумму
# import random
# tup = tuple([random.randint(0,9) for i in range(20)])
# print(tup)
# print("Сумма кортежа:", sum(tup))
# 2)Выведите статистику частности букв в кортеже
# long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и','и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
# from collections import Counter
# c = Counter(long_word)
# print(c)
# lst = list(long_word)
# lst2 = [i for i in lst if i.isalpha() lst.count(i)]
# print(lst.count(elem))

# 3)Допишите скрипт для расчета средней температуры
# # Постарайтесь посчитать количество дней на основе week_temp.
# # Так наш скрипт сможет работать c данными за любой период
#
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp =
# days =
# mean_temp = sum_temp / days
# print(int(mean_temp))
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp = sum(week_temp)
# days = len(week_temp)
# mean_temp = sum_temp / days
# print(int(mean_temp))

# Задание №1
#
# Найти самое длинное слово в строке.
# s = input("введите строку:").split()
# L = 0
# for i in range(len(s)):
#     if len(s[i]) > L:
#         L = len(s[i])
#         elem = s[i]
# print("самое длинное слово в строке:", elem,", длина", L)

# Задание №2
#
# Преобразовать текст в список слов с удалением знаков препинания.
# text = input("введите текст:").split()
# lst = list(text)
# # print(lst)
# # print("  ".join(lst))

# Д/Р ===========================================================================
# 1.	Дан кортеж. Вывести все его совершенные числа. 6 = 1 + 2 + 3
# 28 = 1 + 2 +4 + 7 +14 то считает то нет 100000 ввожу не считает 10000  то да то нет
# print(*(i for i in range(1, int(input())) if sum(j for j in range(1, i) if i % j == 0) == i))
#
# tup1 = tuple(range(2,100000))
# for elem in tup1:
#     s = 0
#     for i in range(1, elem):
#         if elem % i == 0:
#             s += i
#     if s == elem:
#         print(elem)
# 2.Элементы кортежа числа и строки. Все строки в кортеже сделать
# перевёртышами а числа умножить на два.

# tup = (123, "home", 23, "task")
# lst = list(tup)
# for i in range(len(lst)):
#     if type(lst[i]) == int:
#             lst[i] *= 2
#     if type(lst[i]) == str:
#             k = lst[i][::-1]
#             lst[i] = k
# tup1 = tuple(lst)
# print(tup1)
# 3.	Дан кортеж. Найти разность между его максимальным и
# минимальный элементом.
# import random
# tup = ([random.randint(1,100) for _ in range(15)])
# print(tup)
# max_A = max(tup)
# min_A = min(tup)
# dif = max_A - min_A
# print("min_A: ",min(tup),"max_A: ",max(tup), "разность: ", dif)

# 4.	Ввести список с клавиатуры. Список преобразовать в кортеж.
# Посчитать количество элементов между максимальным и минимальным.
# (5,2,8,9,6,8,3,4) 1 элемент
# lst = [5,2,8,9,6,8,3,4]
# tup = tuple(lst)
# print(tup)
# min = tup.index(min(tup))
# max = tup.index(max(tup))
# elem_count = len(tup[slice(min, max-1)])
# print("Количество элементов списка, между макс и мин:",elem_count)

# 5.	Дан кортеж. Написать программу, определяющую сколько раз
# менялся знак в кортеже. (5,2,-2,7,-8,-9,1) 4 раза
# tup = (5,2,-2,7,-8,-9,1)
# count = 0
# for elem,elem1 in tup:
#     if elem > 0:
#         count += 1
# print("положительное",count)
# через lambda можно сделать ?

# 6.	Дан кортеж. Вывести на экран все простые числа в данном кортеже
# tup = [1,20,2,16,4,6]
# newtup = ([i for i in range(2, len(tup)) if i == 2 or i == 3 or i == 5 or i == 7 or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0)])
# print(newtup)

# 7.	Дан кортеж. Посчитать сумму элементов между максимальным
# и минимальным не включая эти элементы. (1,5,2,8,9,6,8,3,4) sum= 15

# tup = (1, 5, 2, 8, 9, 6, 8, 3, 4)
# minim = tup.index(min(tup))
# maxim = tup.index(max(tup))
# if minim < maxim:
#     print("Сумма между max и min элементом:",sum(tup[minim+1: maxim])) # Почему здесь надо добавить 1 ?
# else:
#     print("Сумма между max и min элементом:",sum(tup[maxim+1: minim]))

# 8.	Дан кортеж. Найти максимальную по длине монотонную последовательность
# ( убывающую или возрастающую) чисел.# (5,2,6,8,9,7,5,7,8)
# tup1 = (5, 2, 6, 8, 9, 11, 7, 5, 4, 3, 2, 7, 8)
# len_numb = 1
# maxlength = 1
# for i in range(1, len(tup1)):
#     if tup1[i] > tup1[i - 1]:
#         len_numb += 1
#     else:
#         if len_numb > maxlength:
#             maxlength = len_numb
#             len_numb = 1
# len_numb = 1
# maxlength2 = 1
# for i in range(1, len(tup1)):
#     if tup1[i] < tup1[i - 1]:
#         len_numb += 1
#     else:
#         if len_numb > maxlength2:
#             maxlength2 = len_numb
#             len_numb = 1
# print(maxlength, maxlength2)
# 9.	Дан кортеж. Без функций и дополнительных списков вывести все
# повторяющиеся элементы. (count не использовать).
# import random # РЕШЕНИЕ с функцией count
# tup = tuple([random.randint(1,9) for i in range(20)])
# print(tup)
# for i in range(len(tup)):
#     if tup.count(tup[i]) >= 2 and tup.index(tup[i]) == i:
#         print(tup[i], end=" ")
# ПРАВИЛЬНОЕ РЕШЕНИЕ
# tup1 = (2, 2, 6, 8, 2, 9, 2, 7, 9, 3, 8)
# for i in range(11):
#     for j in range(i+1,11):
#         if tup1[i]==tup1[j] and tup1[j] not in tup1[:i]:
#             print(tup1[i])
#             break

# tup = (6, 3, 2, [6, 3, 1])
# tup1 = ()
# tup[3].clear()
# tup = tup[:-1]
# print(tup1.__sizeof__())
# tup = (5, 6, "hello", [5, 2, 6], (7, 8, 9), 5)
# print(tup)
# for i in range(len(tup)):
#     print(tup[i])
# for elem in tup:
#     print(elem)
# for ind,elem in enumerate(tup):
#     print(ind,elem)
# print(tup.count(5))
# print(tup.index([5, 2, 6]) )
# print(len(tup[3]))
# if 4 in tup:
#     print("yes")
# else:
#     print("no")
# s = "hello world"
# tup1 = tuple(list(map(int,input().split())))
# tup2 = tuple(s)
# tup3 = tuple(range(1,11))
# tup4 = tuple([i**3 for i in range(1,6)])
#
# print(tup1)
# print(tup2)
# print(tup3)
# print(tup4)
# tup1 = (1,2,4)
# tup2 = (5,6,2)
# tup3 = tup1 + tuple("221321")
# print(tup3)
# tup4 = tup2*3
# print(tup4)
# a = (input ("enter a"))
# Tup = tuple(a)
# print(Tup)
# s = input()
# tup = tuple(s.split())
# print(tup)
# tup = ("Vasya", "Pupkin", 5.23)
# name, surname, age = tup
# print(name, surname, age)
# Создайте кортеж из случайных 10 чисел. Найдите его максимальный минимальный элемент
# import random
# tup = tuple([random.randint(1,10) for i in range(10)])
# print(tup)
# print(max(tup),min(tup))

# КОРТЕЖИ
import random

# tup = (6, 3, 2, [6, 3, 1])
# print(tup[3]) # [6,3,1] вложенный список
# print(tup[3][1]) # 3
# tup[3][1] = 2 # присваеваем другое знечение 3 - [2]
# print(tup) # (6,3,2,[6,2,1])
# tup[3].append(5) # добавляем в список 5 (6,3,2,[6,2,1,5]
# print(tup)
# tup[3].clear()
# print(tup) # (6,3,2,[])
# tup1=()
# print(tup1.__sizeof__()) # размер ячейки
# x = (1,2,3)
# y = (4,5,6)
# tup = x + y # объединение кортежей
# print(tup)
# tup1 = x * 3 # дублирование кортежей
# print(tup1)

# tup = tup[:-1] # срез удаление
# print(tup)
# a = (1,2,3,4,5,2,4)
# print(a.count(2),len(a)) # функция подсчета и длины
#
# tup = (5, 6, "Hello", [2, 4, 5], (3, 5, 7))
# for i in range(len(tup)):
#     print(tup[i])  # перебор по индексам
# Ответ
#     5
#     6
#     Hello
#     [2, 4, 5]
#     (3, 5, 7)

# for elem in tup:
#     print(elem)
# Ответ
# 5
# 6
# Hello
# [2, 4, 5]
# (3, 5, 7)
# for ind,elem in enumerate(tup):
#     print(ind,elem)
# Ответ
#     0 5
#     1 6
#     2 Hello
#     3[2, 4, 5]
#     4(3, 5, 7)
# print(tup.count(5)) # количество считает
# print(tup.index([2,4,5])) # индекс находит
# print(len(tup[3])) # длина списка т.е. 3 позиции по индексу
# if 5 in tup:        #операторы пренадлежности
#     print("yes")
# else:
#     print("no")
# Как ввести кортеж с клавиатуры
# k = tuple(list(input()))
# print(k)
# 2 3 4
# ('2', ' ', '3', ' ', '4')
# k = tuple(list(map(int,input().split())))
# print(k)
# 1 2 5
# (1, 2, 5)
# s = "Hell world"
# tup2 = tuple(s)
# print(tup2)
# ('H', 'e', 'l', 'l', ' ', 'w', 'o', 'r', 'l', 'd')
# tup3 = tuple(range(1,11))
# print(tup3)
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tup4 = tuple([i**3 for i in range(1,6)])
# print(tup4)
# (1, 8, 27, 64, 125)
# tup1 = (1,2,3)
# s = "2345"
# tup2 = tup1 + tuple(s)   # конкатенация со строкой
# print(tup2)
# (1, 2, 3, '2', '3', '4', '5')

# s = input()  # преобразование строки в кортеж
# tup = tuple(s.split())
# print(tup)
# hrlll
# ('hrlll',)

# tup = ("vasya","pupkin",5.4)
# name,surname,mark = tup
# print(name,surname,mark)
