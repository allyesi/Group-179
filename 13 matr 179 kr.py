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

# n = int(input("Введите количество элементов n: "))
# m = int(input("Введите количество элементов m: "))
# lst = [[1]*m for j in range(n)]
# lst1 = []
# i = 1
# for i in range(1,n):
#     lst1.append([])
#     for j in range(1,n):
#         lst1.append(i)
#         i += 1
# for j in lst:
#     print(*j)  # Почему выводить надо i ?
# n = int(input("Введите количество элементов n: "))
# m = int(input("Введите количество элементов m: "))
# lst = [[[1]*m for j in range(n)] for i in range(n)]
# print(lst)
#
# lst[i][j] = i * j.
# print(lst)
# n, m = [[1] for i in input("Введите число n, m:").split()]
# lst = []
# for i in range(n):
#     lst.append(lst[i+1][j]) # почему [] ?????????????????
# print(lst)
#     for j in range(m):
#         if (i + j) % 2 == 0:
#             lst[i].append('.')
#         else:
#             lst[i].append('*')
# for row in lst:
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