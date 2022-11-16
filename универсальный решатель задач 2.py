from math import log2


def info():
    var_to_find = input('Что не известно? \n1)N \n2)i \n3)I \n4)K \nНеизвестно: ')
    if var_to_find.strip() == '1':
        i = int(input('Введи i: '))
        print(2 ** i)
    elif var_to_find == '2':
        what_to_use = input('Что вы хотите использовать? \n1)N \n2)I,K \nИспользую: ')
        if what_to_use == '1':
            N = int(input('Введи N: '))
            print(log2(N))
        elif what_to_use == '2':
            K=int(input('Введите K: '))
            I=int(input('Введите I: '))
            print(f'i={I / K}')
    elif var_to_find == '3':
        what_to_use = input('Что вы хотите использовать? \n1)N,K \n2)i,K \nИспользую: ')
        if what_to_use == "1":
            K=int(input('Введите K: '))
            N=int(input('Введите N: '))
            i = log2(N)
            print(f'I={K * i}')
        else:
            K=int(input('Введите K: '))
            i=int(input('Введите i: '))
            print(f'I={K * i}')
    elif var_to_find == '4':
        what_to_use = input('Что вы хотите использовать? \n1)N,I \n2)i,I \nИспользую: ')
        if what_to_use == '1':
            K=int(input('Введите K: '))
            I=int(input('Введите I: '))
            i = log2(N)
            print(f'I={I / i}')
        else:
            i=int(input('Введите i: '))
            I=int(input('Введите I: '))
            print(f'K={I / i}')


def image():
    var_to_find = input('Что не известно? \n1)K \n2)b \nНеизвестно: ')
    if var_to_find == '1':
        b = int(input('Введи b: '))
        print(f'k = {2 ** b}')
    elif var_to_find == '2':
        K = int(input('Введи K: '))
        print(f'b = {log2(K)}')


def sound():
    var_to_find = input('Что не известно? \n1)H \n2)t \nНеизвестно: ')
    if var_to_find == '1':
        t = int(input('Введи t: '))
        print(f'H = {1 / t}')
    elif var_to_find == '2':
        H = int(input('Введи H: '))
        print(f't = {1 / H}')


def f11():
    type_of_data = input("С каким типом данным хотите работать?\n1)Изображение \n2)Звук \n3)Информация \nЯ хочу работать с: ")
    if type_of_data.lower().strip() == "1":
        image()
    elif type_of_data.lower().strip() == "2":
        sound()
    elif type_of_data.lower().strip() == "3":
        info()


if __name__ == '__main__':
    f11()
