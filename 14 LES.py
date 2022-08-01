#f = open("test.txt", "r") # почему у меня не открываются режимы доступа
# f = open("test.txt", "w") #Запись в файл
# f.write(str(23) + "\n")
# f.write("world" + "\n")
# f.write("Круцких Алеся Алексеевна" + "\n")
# f.write("Фитнес" + "\n" + "Звоните ДиКаприо" + "\n" )
# f.close() # закрытие файла
# f = open("test.txt", "a") # дозапись в файл
# f.write("инженер-строитель" + "\n" + "Греция")
# f.close()
# считывание из файла
f = open("test.txt", "r")
s = f.read()
print(repr(s))
s = s.replace("\n"," ").rsplit()
print(repr(s))





