# #      0  1     2
# # lst = [5, 2, [6, 2, 1]]
# #           0          1
# #        0  1  2    0  1  2
# # lst2 = [[5, 2, 1], [6, 1, 8]]
# # print(lst2[0])
# # print(lst2[0][2])
# # for i in range(len(lst2)):
# #     for j in range(len(lst2[i])):
# #         print(lst2[i][j],end=" ")
# #     print()
# # 1 cпособ
# # lst = []
# # for i in range(3):
# #     lst2 = [int(i) for i in input().split()]
# #     lst.append(lst2)
# # print(lst)
# # 2 способ
# # lst = [[int(i) for i in input().split()] for i in range(3)]
# # print(lst)
# # 3 способ
# # lst = [list(map(int,input().split())) for i in range(3)]
# # print(lst)
# # row = column = 4
# # lst = [[1 for _ in range(column)] for _ in range(row)]
# # lst2 = [[1]*column for _ in range(row)]
# # print(lst)
# # print(lst2)
# # lst = [[i * j for i in range(3) if j % 2 == 0] for j in range(5)]
# # print(lst)
# # lst = [[int(i) for i in input().split()] for i in range(3)]
# # for i in range(len(lst)):
# #     for j in range(len(lst[i])):
# #         if i > j:
# #             print(lst[i][j], end=" ")
#
# # lst = [[int(i) for i in input().split()] for i in range(4)]
# # summa = 0
# # for i in range(4):
# #     summa +=sum(lst[i])
# # print(summa)
# # поиск строки с максимальным числом чётных элементов
# lst = [[int(i) for i in input().split()] for i in range(4)]
# number_row = -1
# flag = False
# max_count = 0
# for i in range(len(lst)):
#     count = 0
#     for j in range(len(lst[i])):
#         if lst[i][j] % 2 == 0:
#             count += 1
#     if count > max_count:
#         flag = True
#         max_count = count
#         number_row = i
#
# if flag:
#     print("row:",number_row)
# else:
#     print("no row")
# # поиск столбца с максимальным числом чётных элементов
# # max_count = 0
# # number_row = -1
# # flag = False
# # lst = [[int(i) for i in input().split()] for i in range(4)]
# # for i in range(len(lst)):
# #     count = 0
# #     for j in range(len(lst[i])):
# #         if lst[j][i] % 2 == 0:
# #             count += 1
# #     if count > max_count:
# #         flag = True
# #         max_count = count
# #         number_row = i
# # if flag:
# #     print("row:",number_row)
# # else:
# #     print("no row")
# # нахождение всех простых чисел матрицы
# # import random
# # import random
# #
# # lst = [[random.randint(2,20) for i in range(5)] for j in range(5)]
# # lst2 = []
# # for i in range(len(lst)):
# #     for j in range(len(lst[i])):
# #         print(lst[i][j],end=" ")
# #         for k in range(2,lst[i][j]):
# #             if lst[i][j] % k == 0:
# #                 break
# #         else:
# #             lst2.append(lst[i][j])
# #     print()
# #
# # print(lst2)
# # exception
# # lst = [2,5,1]
# # try:
# #     print(6/0)
# # except ZeroDivisionError:
# #     print("ZeroDivisionError :(")
# # except TypeError:
# #     print("Type Error ;(")
# # except IndexError:
# #     print("Index Error :(")
# # except Exception as e:
# #     print(e)
# #     print(type(e))
# # else:
# #     print("all good")
# # finally:
# #     print("always")
# # raise - кидает ошибку
# # while True:
# #     try:
# #         name = input()
# #         if name[0].islower():
# #             raise NameError("Имя должно быть написано с большой буквы")
# #         else:
# #             print(f"hello {name}")
# #             break
# #     except NameError:
# #         print("Введите имя заново")
# # 5 задача
# # lst = [str(i) for i in input().split()]
# # print(len(lst) - len(set(lst)))
# # 6 задача
# # import random
# #
# # number = int(input())
# # n = random.randint(1, number)
# # set1 = set(range(1, number + 1))
# # print(n)
# # count = 0
# # while True:
# #     print(*set1)
# #     guess = {int(i) for i in input("Enter guess:").split()}
# #     if n in guess and len(set1) > 1:
# #         print("Yes:", end="")
# #         set1 = guess
# #         count += 1
# #     else:
# #         set1.difference_update(guess)
# #         count += 1
# #     if len(set1) == 1:
# #         print(f"you guess for {count} time")
# #         break
# # 4 задача
# # lst = [int(i) for i in input().split()]
# # set1 = set()
# # for elem in lst:
# #     if elem not in set1:
# #         print("NO")
# #         set1.add(elem)
# #     else:
# #         print("YES")
#
# #
# 1.	Сгенерировать двумерный список. Среди строк заданной матрицы, cодержащих только
# нечетные элементы, найти строку с максимальной по модулю суммой элементов.
# 2.	Дано нечетное число n. Создайте двумерный список из n×n элементов, заполнив его
# # символами "." (каждый элемент списка является строкой из одного символа). Затем заполните
# # символами "*" среднюю строку списка, средний столбец массива, главную диагональ и побочную
# # диагональ. В результате  в списке должна получиться снежинка. Выведите полученный список
# # на экран, разделяя элементы списка пробелами.
# 3.	Даны два числа n и m. Создайте двумерный список размером n×m и заполните его
# символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.

# n = 3
# m = 4
# A = []
# for i in range(n):
#     A.append([0]*m)
#     print(A)
# [[0, 0, 0, 0]]
# [[0, 0, 0, 0], [0, 0, 0, 0]]
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# n = 3
# m = 2
# A = [[0] * m for i in range(n)]
# print(A)
# [[0, 0], [0, 0], [0, 0]]
import random

# A = [[1,4,5,12],
#      [-5,8,9,0],
#      [-6,7,11,19]]
# print("A=",A) # A= [[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]]
# print("A[1]=",A[1]) #A[1]= [-5, 8, 9, 0]
# print("A[1][2]=",A[1][2]) # A[1][2]= 9
# print("A[0][-1]=",A[0][-1]) #A[0][-1]= 12
# column = []
# for row in A:
#     column.append(row[2])
# print("3rd colomn =",column) #3rd colomn = [5, 9, 11]
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=" ")
#     print()
# n = 3
# m = 4
# A = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         A[i][j] = 2
#     print(A)
# [[2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
# [[2, 2, 2, 2], [2, 2, 2, 2], [0, 0, 0, 0]]
# [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
# Задание №1
# Создать матрицу M x N, где M и N вводятся с клавиатуры.
# Элементы матрицы заполнить случайными числами. Сделать
# читабельный вывод матрицы.
# import random
# # ???????????????????????????
# N = int(input("Введите N (row):"))
# M = int(input("Введите M (colomn):"))
#
# A = [[0] * N for i in range(M)]
# for i in range(M):
#     for j in range(N):
#         A[i][j] = random.randint(1, 100)
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j], end="")
#     print(A)
# Введите N (row):3
# Введите M (colomn):3
# 516696[[51, 66, 96], [51, 53, 95], [32, 82, 54]]
# 515395[[51, 66, 96], [51, 53, 95], [32, 82, 54]]
# 328254[[51, 66, 96], [51, 53, 95], [32, 82, 54]]


# Задание №2
# Матрица N x M, можно задать статически. Элементы заполняются
# случайными числами. Вводить с клавиатуры число и если оно
# есть в матрице, то вывести индекс строки и колонки в которой
# оно находится.
# random randint
# N = 4
# M = 5
# A = [[0] * N for i in range(M)]
# for i in range(N):
#     for j in range(M):
#         A[i][j] = random.randint(10,90)
# for i in range(len(A)):
#     for j in range(len(A[i]):
#         print(A[i][j], end = " ")
#     print()
# item = int(input("Введите число:"))
# for



# 1.	Сгенерировать двумерный список. Среди строк заданной матрицы, cодержащих только
# нечетные элементы, найти строку с максимальной по модулю суммой элементов.
# lst = [[int(i) for i in input().split()] for i in range(5)]
# number_row = -1
# flag = False
# max_count = 0
# for i in range(len(lst)):
#      count = 0
#      for j in range(len(lst[i])):
#           if lst[i][j] % 2 == 1:
#                count += 1
#      if count > max_count:
#           flag = True
#           max_count = count       # как указать максимальная по модулю ?
#           number_row = i
# if flag:
#      print("row", number_row)
# else:
#      print("no row")
# 2. Дано нечетное число n. Создайте двумерный список из n×n элементов, заполнив его
# символами "." (каждый элемент списка является строкой из одного символа). Затем заполните
# символами "*"	строку списка среднюю , средний столбец массива, главную диагональ и побочную
# диагональ. В результате  в списке должна получиться снежинка. Выведите полученный список
# на экран, разделяя элементы списка пробелами.
# colomn = row = n = int(input("введите нечетное число n:  "))
# A = [["."] * n for j in range(n)]
# for i in range(n):
#     A[n//2][i] = "*"
#     A[i][n // 2] = "*"
#     A[i][i] = "*"
#     A[n-1-i][i] = "*"
# for row in A:
#     print(" ".join(row))
# 3.	Даны два числа n и m. Создайте двумерный список размером n×m и заполните его
# символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
# n, m = [int(i) for i in input("Введите число n, m:").split()]
# lst = []
# for i in range(n):
#     lst.append([]) # почему [] ?????????????????
#     for j in range(m):
#         if (i + j) % 2 == 0:
#             lst[i].append('.')
#         else:
#             lst[i].append('*')
# for row in lst:
#     print(' '.join(row))
# 4.	Сгенерируйте список как показано ниже.
#   j
#   0    1    2    3     4     5
#i0 1    1    1    1     1     1 n
# 1 1    2    3    4     5     6
# 2 1    3    6   10     15    21
# 3 1    4   10   20     35    56
# 4 1    5   15   35     70    126
# 5 1    6   21   56     126   252
# главная диагональ i=j , i+j = n - 1: (n = i + j + 1)
# n = int(input("Введите количество элементов n: "))
# lst = [[1]*n for j in range(n)]
# for i in range(1,n):
#     for j in range(1,n):
#         lst[i][j] = lst[i-1][j]+lst[i][j-1]
#
# for i in lst:
#     print(*i)  # Почему выводить надо i ?

# 5.	Сгенерируйте список как показано ниже.
#  1    2    3    4     5
#  1    4    9    16   25
#  1    8    27  64   125
#  1	16   81  256  625
# n = int(input("Введите количество элементов n: "))
# m = int(input("Введите количество элементов m: "))
# lst = [[1]*m for j in range(n)]
# # # for row in lst:      # Почему в данном случае не могу применить ?
# # print(lst)
# for i in range(n):
#     for j in range(m):

#         lst.append(j*j)
#
#     print(*lst)  # Почему выводить надо i ?
# n, m = [int(i) for i in input("Введите число n, m:").split()]
# n = int(input("Введите количество элементов n: "))
# m = int(input("Введите количество элементов m: "))
# lst = [[1]*m for j in range(n)]
# lst1 = []
# for i in range(n):
#     lst1.append([1]) # почему [] ?????????????????
#     for j in range(len(lst[i])):
#         if lst[j][i] == j*j:
#             lst1[i].append(lst[j][i])
# print(lst1)
# # for row in lst1:
#     print(' '.join(row))


# 6.	Дано число n, и массив размером n × n. Проверьте, является ли палиндромом хоть
# одно число состоящее из цифр стоящих в  строке массива. Выведите слово “YES”, если
# есть такое число и слово “NO” в противном случае.
# n = m = int(input("введите размер: "))
# lst = [[int(i) for i in input().split()] for j in range(n)]
# for i in range(len(lst)):
#     if lst[i] == lst[i][::-1]:
#         print("yes")
#     else:
#         print("no")  # как написать что во всем массиве нет этого элемента

# Sample Input:
# 4
# 2 1 2 1
# 1 3 3 1
# 2 3 4 5
# 4 5 1 2
# Sample Output:
# YES
# Sample Input:
# 3
# 2 1 1
# 1 2 3
# 2 3 4
# Sample Output:
# NO
#
#
# Exeption:
#
# 7.	Опишите конструкцию отлова ошибок, так чтобы выводило,
# какую ошибку вы сделали. Код представлен ниже:
# try:
#     x = (1, 2, 5, 7)
#     x = x / 2
#     print(x)
# except IndexError:
#     print("Index error")
# except TypeError:
#     print("TypeError")

# 8. Напишите программу которые будет ловить IndexError, когда вы
# пытаетесь взять индекс элемента, которого нет в списке.
# try:
#     lst = [1,4,7,56]
#     print("The index of lst:",lst[5])
# except IndexError:
#     print("Index error")

# lst = [1, 2, 3, 4, 5]
# i = 0
# while True:
#     try:
#         print(lst[i])
#     except IndexError:
#         print("Done!")
#         break
#     i += 1
# 9.	Напишите программу которые будет ловить TypeError, когда вы
# пытаетесь скаткатенировать строку и число.
# try:
#     s = "Text"
#     elem = 2
#     print(s+elem)
# except TypeError:
#     print("TypeError")
# 10.	Напишите программу которая вычисляет площадь треугольника
# по формуле Герона, однако если пользователь введёт длину хоть
# одной стороны треугольника равную 0, то программа должна
# бросить исключение ArithmeticError.
# while True:
#     try:
#         a = float(input("Сторона a:"))
#         b = float(input("Сторона b:"))
#         c = float(input("Сторона c:"))
#         p = (a+b+c)/2         #полуперим треуг
#         S = (p*(p-a)*(p-b)*(p-c))**0.5
#         # import math
#         # S = math.sqrt(p * (p - a) * (p - b) * (p - c)) # не работало
#         if a == 0 or b == 0 or c == 0:
#             raise ArithmeticError("Cторона не может быть равна 0")
#         else:
#             print("Площадь S = ",S)
#             break
#     except ArithmeticError:
#         print("Введите стороны снова")

# 11.	Дан список. Пользователь не знает его размер. Программа должна
# бросить исключение TypeError, когда пользователь пытается удалить
# элемент которого нет в списке.
# lst = [1, 5, 6, 7, 8, 9]
# del lst[9]
# print(lst)
# 12.	Дана строка. Пользователь ищет в ней подстроку. Если подстрока
# найдена то бросьте ValueError. ???????????
# try:
#     s = input("введите строку: ")
#     elem = input("Введите подстроку: ")
#     if elem in s:
#         print("Подстрока найдена")
# except ValueError:
#     print("Подстрока найдена")



# 13.	Дана строка. Проверьте есть ли в ней цифры,
# иначе бросьте ValueError.
# while True:
#     try:
#         s = input("Введите стр: ")
#         if s.isalpha():
#             raise ValueError("В строке буквы")
#         else:
#             print("В строке цифры")
#             break
#     except ValueError:
#         print("Введите строку снова")
# 14.	Дан словарь, который содержит некоторые ключи и значения по этим ключам,
# пользователь не знает этих ключей. Бросьте ошибку KeyError в том случае когда
# пользователь пытается просмотреть значение по ключу, которого нет в словаре.
#
#
#Дополнительные задачи:
#
# 15.Разработать программу, запрашивающую у пользователя матрицу размером M x N.
# Выполнить поворот ее на 90° против часовой стрелки . Размерность матрицы
# задаётся случайными значениями. Результаты вывести на консоль.
# Sample Input:
# 2 1 2 1
# 1 3 3 1
# 2 3 4 5
# Sample Output:
# 1 1 5
# 2 3 4
# 1 3 3
# 2 1 2
# lst = [[int(i) for i in input().split()] for i in range(N)]



# 16.	Выведите таблицу размером n×n, заполненную числами от 1 до n*n “змейкой”,
# выходящей из левого верхнего угла, как показано в примере (здесь n=5):

# Sample Input:
# 5
# Sample Output:
# 1     2    3    4    5
# 10   9    8    7    6
# 11   12  13  14  15
# 20   19  18  17  16
# 21   22  23  24  25

