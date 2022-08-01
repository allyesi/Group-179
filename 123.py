# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

# gl = "aeyuio"
# count_gl = count_sgl = 0
#
# lst = [15, 48, 'hello', 692, 19, 'world']
# for i in range(len(lst)):
#     if type(lst[i]) == int:
#         if lst[i] % 2 == 0:
#             k = list(str(lst[i]))
#             summa = sum(list(map(int, k)))
#             print(summa)
#         else:
#             lst[i] = 1
#     if type(lst[i]) == str:
#         for elem in lst[i]:
#             if elem in gl:
#                 count_gl += 1
#             elif elem.isalpha():
#                 count_sgl += 1
# print(lst)
# print(count_gl, count_sgl)
# 4.Дан список, упорядоченный по не убыванию элементов в нем. Определите, сколько в нем различных элементов

# lst = [1, 1, 2, 4, 7, 7, 7, 8, 9, 9, 9, 11, 15]
# count = 1
# for i in range(len(lst) - 1):
#     if lst[i] != lst[i + 1]:
#         count += 1
# print(count)
# 5.   Программа получает на вход три числа через пробел — начало и конец диапазона,
# а также степень, в которую нужно возвести каждое число из диапазона.
# Выведите числа получившегося списка через пробел.
# a, b, step = map(int, input().split())
# 6.
# lst = [1]
#
# if len(lst) == 1:
#     print(lst[0])
# else:
#     for i in range(len(lst)):
#         if i ==len(lst)-1:
#             print(lst[0]+lst[i-1],end=' ')
#             continue
#         print(lst[i-1]+lst[i+1],end=' ')

# 8.   Дан список, состоящий из строк. Отсортировать его по длине слов.
# Сначала должны идти длинные слова затем короткие.
# lst = ["dasdas", 'asdas', 'das', 'sdadasfasf', 's']
# lst.sort(key=len, reverse=True)
# print(lst)
# 9.Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'
# lst = ['sdsa','fdsaaa',"dgf",'saege']
# lst.sort(key = lambda x: x.count("a"))
# print(lst)
# 10
# lst = [4, 8, 0, 3, 4, 2, 0, 3]
# for i in range(len(lst)):
#     if lst.count(lst[i]) >= 2 and lst.index(lst[i]) == i:
#         print(lst[i], end=" ")
# Сгенерировать список всех простых чисел до  100 с помощью генератора.
# lst = [i for i in range(2, 100) if i == 2 or i == 3 or i == 5 or i == 7 or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0)]
# print(lst)
# lst = [i for i in range(2, 100) if len([j for j in range(2, i) if i % j == 0]) == 0]
# print(lst)
# Дан список , преобразуйте исходный список, вставив 0 между числами. Дополнительный список не создавать!
# lst = [1, 2]
# i = 0
# while len(lst) > i:
#     if i % 2 == 1:
#         lst.insert(i,0)
#     i+=1
# print(lst)
# lst = []
# n = int(input())
# for i in range(1,n):
#     if len(lst) >=n:
#         lst = lst[:n]
#         print(lst)
#         break
#     print(i)
#     k = str(i) * i
#     lst.extend(list(map(int,k)))