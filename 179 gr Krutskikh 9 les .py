# list comprehension
# [что положить в список for из чего положить in диапазон значений(итерируемый объект)]
# [что положить в список for из чего положить in диапазон значений(итерируемый объект)
# if условие верно]
# [что положить в списое if условие верно else что положить for из чего положить
# in диапазон значений(итерируемый объект)]

import random

# lst = [i for i in range(1,11)]
# lst2 = [i for i in "hello world"]
# lst3 = [int(input()) for i in range(5)]
# lst4 = [random.randint(1,100) for i in range(5)]
# lst5 = [int(i) for i in input().split()]
# lst2 = [i for i in "hello2319 12 world" if i.isalpha() or i ==" "]
# lst = [i for i in range(1, 101) if i % 2 == 0 and i % 5 == 0]
# lst = [i if i % 2 == 0 else i ** 3 for i in range(1, 11)]
# print(lst)

#1)Сгенерировать список нечётных двузначных  чисел.
import random
# lst = [i for i in range(1,100) if i % 2 == 1]
# print(lst)
#2)Сгенерировать список из 10 чисел степени 2. От 1 до 10.
# lst = [i**2 for i in range(1,11) ]
# print(lst)
#3)Сгенерировать список всех трёхзначных чисел кратных 5 и 3.
# lst = [i for i in range(100,1000) if i % 5 == 0 and i % 3 == 0]
# print(lst)
#4)Дан список, упорядоченный по не убыванию элементов в нем.
# Определите, сколько в нем различных элементов. Set не использовать.





# 5)Программа получает на вход три числа через пробел — начало
# и конец диапазона, а также степень, в которую нужно возвести
# каждое число из диапазона. Выведите числа получившегося списка через пробел.
# Sample Input:
# 5 12 3
# Sample Output:
# 125 216 343 512 729 1000 1331
# lst = [i**3 for i in range(5,12)]
# lst1 = " ".join(str(lst).split(","))
# print(lst1)

#6)Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка. Например, если на вход подаётся
# список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же. Вывод должен содержать
# одну строку с числами нового списка, разделёнными пробелом.
# Sample Input 1:
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7
# Sample Input 2:
# 10
# Sample Output 2:
# 10
# Sample Input 3:
# 10 2
# Sample Output 3:
# 4 20

# 7)Числа вводятся в список в одной строке. Отсортировать их по убыванию их абсолютных значений.
# Почему не вводятся минусовые занчения?
# lst = list(map(int, input("Введите числа: ").split()))
# lst.sort(key=abs, reverse=True)
# print(lst)

# 8)Дан список, состоящий из строк. Отсортировать его по длине слов. Сначала должны идти длинные
# слова затем короткие.
# lst = ["apple","kiwi","strawberry","apricot"]
# lst.sort( key=len, reverse = True)
# print(lst)


# # 9)Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a' ??????
# lst = ["cake", "bee", "sad", "blackboard"]
# lst[i] = a
# lst.sort(key=lambda a: lst.count(a))
# print(lst)


# Дополнительные задачи:
# 10)Напишите программу, которая принимает на вход список чисел в одной строке
# и выводит на экран в одну строку значения, которые повторяются в нём более
# одного раза. Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
# Sample Input 1:
# 4 8 0 3 4 2 0 3
# Sample Output 1:
# 0 3 4
# Sample Input 2:
# 10
# Sample Sample Input 3:
# 1 1 2 2 3 3
# Sample Output 3:
# 1 2 3
# 11) *Сгенерировать список всех простых чисел до 100 с помощью генератора.
# lst = [i for i in range(1,100)]
# print(lst)
# 12) Дан список , преобразуйте исходный список, вставив 0 между числами.
# Дополнительный список не создавать!
# Sample Input:
# 7 4 1
# Sample Output:
# 7 0 4 0 1
# lst = [7,4,1]
# for elem in lst:



#13) Напишите программу, которая выводит часть последовательности
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
# На вход программе передаётся неотрицательное целое число n — столько элементов
# последовательности должна отобразить программа. На выходе ожидается последовательность чисел,
# записанных через пробел в одну строку.
#
# Sample Input:
# 7
# Sample Output:
# 1 2 2 3 3 3 4
# Sample Input 2:
# 10
# Sample Output 2:
# 1 2 2 3 3 3 4 4 4 4

# создайте кортеж с числами от 0 до 9 и посчитайте сумму
for i in r
# Выведите статистику частности букв в кортеже
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,
#            'и', 'и', 'т', 'т', 'а', 'и', 'и',
#            'и', 'и', 'и', 'т', 'и’)
# Допишите скрипт для расчета средней температуры
# # Постарайтесь посчитать количество дней на основе week_temp.
# # Так наш скрипт сможет работать c данными за любой период
#
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp =
# days =
# mean_temp = sum_temp / days
# print(int(mean_temp))


