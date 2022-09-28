p = int(input('Введите кол-во чисел из ряда Фибоначчи '))
a_1 = int(1)
a_2 = int(2)
a_n = int()
print (a_1)
print (a_2)
for i in range (p-2):
    a_n = a_1 + a_2
    a_1 = a_2
    a_2 = a_n
    print (a_n)

