
# напишите программу, которая проверяет последнюю цифру числа. Если последняя цифра числа 3,
# то вывести True иначе вывести False.
# number = int(input("Ввести число:", ))
# print(number % 10 == 3)
#Напишите программу которая выводит True если хотя бы одно из чисел A,B,C отрицательно.
#Если нет вывести False. Числа вводятся с клавиатуры в одной строке
# A, B, C = map(int, input("Введите числа: ",    ).split())
# # if A < 0 or B < 0 or C < 0:
# #     print("True")
# # else:
# #     print("False")
# Верно ли что целые m и k имеют одинаковую четность
# m,n = map(int,input('Введите m и n:',   ).split())
# if m%2 == 0 and n%2 == 0:
#     print("True")
# else:
#     print("False")
#Напишите программу которая выводит True если число х кратно 3 и заканчивается на 5
# число х вводится с клавиатуры
# x = int(input("Введите число:",   ))
# if x % 3 == 0 and x % 10 == 5:
#     print("True")
#5)Найти количество четных чисел среди заданных трех целых чисел.
# В ответе вывести количество четных чисел.
# = i % 2 == 1
# if i % 2 == 0:
#     chet = chet map(int,input("Введитеa,b,c = целое число: ").split())
# chet = i % 2 == 0
# nechet  + 1
# else:              !!!!!!!!!!!!!!!!!!!
#     nechet = nechet + 1
# print(chet , nechet)



# 6) Дано двузначное число. Определить является ли сумма его цифр двузначным числом.
# (Ответ: Да/Нет)
# n = int(input("введите двузначное число:   "))
# sum = n %100 // 10 + n % 10
# if sum >= 10:
#     print("сумма цифр двузначное число,", sum)
# else:
#     print("сумма цифр однозначное число", sum)
 # 7) Дано четырёхзначное число. Проверить, одинаковы ли все цифры в нём.
# n = int(input("Введите четырехзначное число: "))
# a1 = n % 10000 // 1000
# a2 = n % 1000 // 100
# a3 = n % 100 // 10
# a4 = n % 10
# print("правда ли что все цифры одинаковы",a1 == a2 == a3 == a4)
# 8) Напишите программу, принимающую на вход год и выводящую "Високосный",
# если в этом году действительно 366 дней, и "Не високосный" иначе.
# Год считается високосным, если его номер делится на 4,
# но не делится на 100 или же делится на 400.
# year = int(input("Enter year:  "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Високосный")
# else:
#     print("Не високосный")
# 9)Объяснить результат и вывести на экран результат логического выражения
# T = S для заданных значений логических переменных a, b, c.
# +   логическое сложение   (логическое «или») or
#·    логическое умножение (логическое «и») and
# ¯  логическое отрицание (логическое «не») not

# 10) Поле  шахматной доски определяется парой натуральных чисел,
# каждое из которых не превосходит 8:   первое – номер вертикали,
# второе – номер горизонтали. Заданы натуральные числа x1, y1, x2, y2.
# Определить, являются ли поля (x1, y1) и (x2, y2) одного  цвета?
# На поле (x1, y1) расположен ферзь. Угрожает ли он полю (x2, y2)?
# На поле (x1, y1) стоит ладья, на поле (x2, y2) – пешка. Определить,
# бьет ли ладья пешку, пешка – ладью или фигуры не угрожают друг другу.
# На поле (x1, y1) стоит слон, на поле (x2, y2) – конь. Определить,
# бьет ли слон коня, конь – слона или фигуры не угрожают друг другу.






# Урок 3
#2)Дано слово.Верно ли что оно начинается и заканчивается на одну и ту же букву
# str = str(input())
# if str[0] == str[-1]:
#     print("True")
# else:
#     print("False")
#3)Дано слово получить его часть образованную второй третьей и четвертой буквами
# word = input("введите слово:",  )
# print(word[1:4:1])
#4)из слова яблоко путем вырезок  и склеек его букв получить слова блок и око
# word = "яблоко"
# word1 = word[1:5:1]
# word2 = word[3::1]
# print(word1,"",word2)
#5)Дана строка"*" Получить строку состоящую из пяти звездочек
# str = "*"
# print(str*5)
#6)Проверить является ли строка полиндромом.(шалаш)
#str = "шалаш"
# if str[::1]==str[::-1]:
#     print("полиндром")
#7)Дана строка Если в этой строке буква f встречается только один раз выведите ее индекс
#Если она встречается два и более раз выведите индекс ее первого появления и количество
#букв f . Если буква f в данной строке не встречается ничего не выводите
# s = input("введите строку:",  )
# if s.count("f") == 1:
#     print(s.find("f"))
# if s.count("f") >= 2:
#     print(s.find("f"),s.count("f"))
#8)Дана строка найдите в этой строке второе вхождение буквы f и выведите индекс этого
#вхождения.Если буква f в данной строчке встречается только один раз выведите число-1 а
# если не встречается на разу выведите число -2.
# s = input("введите строку:",  )
# if s.count("f") == 1:
#     print(-1)
# elif s.count("f") <1:
#     print(-2)
# else:
#     print(s.find("f",s.find("f")+1))
# 9) дана строка замените в этой строке все цифры 1 на слово one.
# s = "11123"
# a = s.replace("1","one")
# print(a)
#10) Напишите программу которая вычисляет процентное содержание
#символов g и c в веденной строке(программа не должна зависеть от регистра вводимых
#символов
# s = "aCggtGttat"
# s1 = s.lower()
# a = s1.count("g")
# b = s1.count("c")
# print((a+b)*100/len(s1))
#11)уберите точки из введенного IP адреса.Выведите сначал четыре числа через пробел
#а затем сумму получившихся.
# ip = "192.168.0.1"
# print(ip.replace("."," "))
# x1 = int(ip[:3])
# x2 = int(ip[4:7])
# x3 = int(ip[8:9])
# x4 = int(ip[10:11])
# print(x1+x2+x3+x4)

#Урок 4
#1)вывести на экран число "10" 20 раз столбиком
# for i in range(20):
#     print("10")
#2)даны два числа a и b.Составить программу вывода на экран всех чисел от a до b .
# a,b = map(int,input().split())
# for i in range(a,b+1):
#     print(i)
#3)Дано число n.Составить программу выводящую кубы чисел от 1 до n в одну строку.
# n = int(input("Введите число n = ",  ))
# for i in range(1,n+1):
#     print(i**3, end = "  ")
#4)Выведите на экран в одну строку числа от 100 до -100 включительно
# for i in range(100,-100,-1):
#     print(i,end = " ")
#5)Необходимо вывести все четные числа на отрезке [a;a*10]
# a = int(input("введите число а= ",  ))
# for i in range(a,a*10):
#     if i%2 == 0:
#         print(i)
#6)Найти сумму всех целых чисел от 100 до 500 включительно
# summa = 0
# for i in range(100,500):
#     if i//10:
#         summa += i
#         print("summa",summa)
#7)Найти произведение всех целых чисел от 5 до 20 включительно
# multiply = 1
# for i in range(5,20):
#     multiply *= i
#     print("multiply",multiply)
#8)Дано натуральное число n Вывести на экран факториал числа
# n = int(input("введите натур число n=",   ))
# factorial = 1
# for i in range(1,n+1):
#     factorial *=i
#     print(factorial)
# Задача в классе
# Удалить в строке все буквы S непосредственно за которыми идет цифра
# str = "asdfs4fgjs4fg"
# str1 = " "
# for i  in range(len(str)):
#     if str[i] == "s" and str[i+1].isdigit():
#         continue #пропуск всего что ниже
#     str1 += str[i]
# print(str)
# print(str1)
#Удалить в строке все цифры 1 непосредственно за которыми идет буква
# str = "1231fgh21dfg"
# str1 = " "
# for i in range(len(str)):
#     if str[i]== "1" and str[i+1].isalpha():
#         continue
#     str1 += str[i]
# print(str)
# print(str1)
#удалить в строке все буквы m непосредственно перед  которыми идет цифра
# s = "adf2mn2mnd3kkm3"
# s1 = " "
# for i in range(len(s)):
#     if s[i] == "m" and s[i-1].isdigit():
#         continue
#     s1 += s[i]
# print(s1)
# ПРОВЕРИТЬ ДЕЛИМОСТЬ ЧИСЛА
# 2) ПРОСТОЕ ЛИ ЧИСЛО - (которое делится на 1 и на себя)
# number = int(input("Enter number: "))
# for i in range(1,number+1):# при удалении "1" теряется последнее значение number
#     if number % i == 0: # число number разделить на число из диапазона
#         print(i, end = " ")
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ПРОВЕРИМ ПРОСТОЕ ЛИ ЧИСЛО
# number = int(input("Enter number:"))
# count = 0
# for i in range(1,number+1):
#     if number%i == 0:
#         count += 1
#         print (i, end = " ")
# if count == 2:
#     print("простое")
# else:
#     print("составное")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# s = "hello"
# перебор строки по элементам
# for elem in s:
#     print(elem, end = " ")   # h e l l o
# перебор строки по индексам
# for i in range(0,len(s),1):  или range(len(s))
#       print(i,s[i]) # i - индекс, s[i] - элемент
# перебор строки по индексам и по элемементам ENUMERATE
# s = "hello"
# for ind,elem in enumerate(s):     # i = ind, elem = s [i]
#       print(ind,elem)

# Дан текст Слова в тексте разделены одним или несколькими пробелами
# Написать программу выводящую все различные слова текста.
# s = "dfaf dssa    asd"
# s1 = " "
# for i in range(len(s)):
#     if s[i]!= " ":
#         s1 += s[i]
#     elif s[i] == " " and len(s1)>=1:
#         print(s1)
#         s1 = " "

#9) Дан текст. Слова в тексте разделены одним или несколькими пробелами. Написать
#программу определяющую количество слов, заканчивающихся одной и той же буквой "c".
# s = "dsfg      asdc sdc"
# s += " "
# s1 = " "
# count = 0
# for i in range(len(s)):
#     if s[i]!= " ":
#         s1 += s[i]
#     elif s[i] == " ":
#         if s1[-1] == "c":
#             count +=1
#         s1 = " "
# print(count)
# Дан текст s и символ c. Все слова в тексте разделены одним или несколькими
# пробелами.Написать программу определяющую количество слов текста, в которых
# содержится заданный символ.
# s = "fdfhk cc dfcd ghjc   ffg"
# s1 = " "
# count = 0
# for i in range(len(s)):
#     if s[i] != " ":
#         s1 += s[i]
#     elif s[i] == " ":
#         if "c" in s1:
#             count +=1
#         s1 = ""
# print(count)

#10) Вывести строку удалив из нее повторные вхождения символов
# s = "dfghjakdlf"
# s1 = " "
# for i in range(len(s)):
#     if i >= 2:
#         s1 += s[i]
# print(s1)




# вложеные циклы
# for i in range(1,6): #внешний
#     print("i",i)
#     for j in range(1,4): # внутренний
#         print('j',j)1
# В классе. Найти все простые числа от 2 до 100. 1 не простое число
# for i in range(2,101):
#     count = 0
#     for j in range(1,i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i,end=" ")
# Натуральное число, записанное в десятичной системе
# счисления, называется сверхпростым, если оно остается простым при
# любой перестановке своих цифр.
# Найти двухзанчные сверхпростые числа.
# (13 31) (17 71) (37 73) (79 97) (11 11)
# for i in range(10,101):
#     count = 0 # проверяет простое ли число
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2: # если число простое: два делителя
#         number = str(i)[::-1] # переворачиваем число
#         number = int(number) # строку делаем числом
#         count1 = 0
#         for k in range(1,number+1):
#             if number % k == 0:
#                 count1 +=1
#         if count1 == 2 and number>i:
#             print(i,number)



# 11) Дана строка символов, состоящая из произвольных натуральных чисел,
# разделенных пробелами. Вывести четные числа этой строки.
# s = "2 234 5 34 90 2346"
# s += " "
# s1 = ""
# for i in range(len(s)):
#     if s[i] != "  ":
#         s1 += s[i]
#     elif s[i] == " " and len(s1) >= 1:
#         if int(s1) % 2 == 0:
#             print(s1)
#         s1 = ""
# s = "2f 23sd4 5 3gh4 90 23f46"
# s += " "
# s1 = ""
# for i in range(len(s)):
#     if s[i] != " ":
#         s1 += s[i]
#     elif s[i] == " " and len(s1) >= 1:
#         if s1.isdigit():
#             if int(s1) % 2 == 0:
#                 print(s1)
#         s1 = ""

# 12) Sample Input 1: Aaaabbcaa
#     Sample Output 1: a4b2c1a2
#     Sample Input 1: Abc
#     Sample Output 1: a1b1c1
#программа, которая считывает строку,кодирует ее предложенным алгоритмом
# и выводит закодированную последовательность на стандартный вывод.
# кодирование должно учитывать регистр символов.
# s = "Aaaabbcaa"
# s1 = " "
# s = input().lower()
# s += " "
# s1 = ""
# count = 1
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     else:
#         s1 += s[i] + str(count)  # добавляем текущий элемент + количество посчитанных элементов
#         count = 1
# print(s1)

# 13)С клавиатуры вводится натуральное число n <= 1000. Выведите n строк вида "На лугу n коров", склоняя слово "коров" в соответствии с числом n. Проверяем большие числа!!!
# Sample Input:
# 7
# Sample Output:
# На лугу 1 корова
# На лугу 2 коровы
# На лугу 3 коровы
# На лугу 4 коровы
# На лугу 5 коров
# На лугу 6 коров
# На лугу 7 коров
# 14) Числа Фибоначчи – известная числовая последовательность, в которой первые два члена равны единице, а каждый последующий получается сложением двух предыдущих. По введенному числу n выведите n чисел Фибоначчи через пробел.﻿
# Sample Input:
# 8
# Sample Output:
# 1 1 2 3 5 8 13 21

# 15) Найти натуральное число из диапазона [n, m] (n, m – натуральные числа),
# которое имеет наибольшее количество делителей.

# 16) Даны натуральные числа n, m. Получить все числа меньше m взаимно простые с n.


# УРОК № 5
# циклы WHILE
# number = 1
# while number <= 10:
#     print(number)
#     number += 1
# print("end")
# number = 10
# while number >= 1:
#     print(number)
#     number -= 1
# Ввод данных с клавиатуры пока не введен 0.
# Посчитать сумму введенных чисел.
# sum = 0
# number = int(input("Enter number:"))
# while number != 0:
#     sum += number
#     # number = int(input("Enter number:"))
# print("sum",sum)

# s = 0
# while True:
#     number = int(input("Enter number:"))
#     s += number
#     if number == 0:
#         print("s",s)
#         break
# дано n значное число вывести все его цифры
# n = input()
# for elem in n:
#     print(elem)   # это не для чисел а для строк
# n = int(input("Enter n:"))
# while n != 0:
#     if (n % 10) % 2 == 0:
#         print(n % 10)
#     n //= 10

# алгоритм Евклида
# поиск НОД
# a,b = map(int,input().split())
# a1 = a
# b1 = b
# count = 0 # чтобы посчитать количество итераций
# while a != 0 and b != 0:
#     if a > b:
#         a = a-b # можно - или %
#     else:
#         b = b-a # можно - или %
#         count += 1
# nod = a + b
# nok = (a1+b1)//nod
# print(nod)
# print(nok)
# print(count)

# перебор строки циклом while
# s = "Hello"
# i = 0
# while i < len(s):
#     print(s[i], end=" "  #  H e l l o
#     i += 1
# while True:
#     print(s[i], end = " ")
#     i += 1
#     if i == len(s):
#         break


# удалить повторные вхождения символов без использования еще одной строки
# s = "Hello wello"
# i = 0
# while i < len(s):
#     if s.find(s[i]) != i:
#         s = s[:i] + s[i + 1:]
#     else:
#         i +=1
# print(s)

# ДОмашнее задание
# 1)Дано число n. Вывести все числа от 1 до n.
# number = int(input("введите число n : "))
# i = 1
# while i <= number:
#     print(i, end =" ")
#     i += 1
# 2)Дано число n. Посчитать сумму всех чётных чисел от 0 до n.
# number = int(input("Введите число n:"))
# i = 0
# summa = 0
# while i <= number:
#     if i % 2 == 0:
#         summa += i
#         print(i, end = " ")
#     i += 1
# print(summa)
# 3)Дано натуральное число. Определить произведение цифр в нем которые кратны 2, кроме числа 0.
# num = int(input("Введите натур число: ")) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# i = 1
# mult = 1
# while i < len(num)   and i != 0:
#     if num % 2 == 0:
#         mult *= num
#         i *= 1
# print(mult)




