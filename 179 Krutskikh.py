# 1.Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке.
# lst = [1,3,5,6,3,5,6,7]
# lst1 = []
# for i in lst:
#     if lst.count(i) == 1:
#         lst1.append(i)
# print(lst1)
# 2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# lst = [12,12,3,4,5,6,6]
# count = 0
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)
# 3. Даны два кортежа:
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
# этих кортежей
# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# sum1 = sum(C_1)
# sum2 = sum(C_2)
# if sum1 > sum2:
#     print("Cумма больше в кортеже - C_1")
# else:
#     print("Cумма больше в кортеже - C_2")
# print(C_1.index(min(C_1)),C_1.index(max(C_1)))
# print(C_2.index(min(C_2)),C_2.index(max(C_2)))

# 4. Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.
# 5. Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания
# 6. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.
# a = [1, 2, 4, 5]
# b = [2, 3, 5, 6]
# a1 = set(a)
# b1 = set(b)
# new_st = a1.intersection(b1)
# print(len(new_st))
# 7. Напишите программу, ))демонстрирующую работу try\except\finally
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
#     finally:
#         print("конец")
# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по класс