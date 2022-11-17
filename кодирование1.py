from math import log2

    
def info():
    var_to_find = input('\nЧто не известно? \n1)N \n2)i \n3)I \n4)K \nНеизвестно: ')
    if var_to_find.strip() == '1':
        i = int(input('\nВведи i: '))
        print(f'\nN={2 ** i}')
        vopros()
        
    elif var_to_find == '2':
        var_to_find_2()

    elif var_to_find == '3':
        var_to_find_3()
        
    elif var_to_find == '4':
        what_to_use_4()

    else:
        print("\nВводить значения только от 1 до 4!")
        info_not_1_to_4()
        

def image():
    var_to_find = input('\nЧто не известно? \n1)K \n2)b \nНеизвестно: ')

    if var_to_find == '1':
        b = int(input('\nВведи b: '))
        print(f'\nk = {2 ** b}')
        vopros()

    elif var_to_find == '2':
        K = int(input('\nВведи K: '))
        print(f'\nb = {log2(K)}')
        vopros()
    else:
        print("\nВводить только значения 1 или 2!")
        image_not12()


def sound():
    var_to_find = input('\nЧто не известно? \n1)H \n2)ꚍ \n3)I \n4)t \n5)K \nНеизвестно: ')

    if var_to_find == '1':
        ꚍ = int(input('\nВведи ꚍ: '))
        print(f'\nH = {1 / ꚍ}')
        vopros()

    elif var_to_find == '2':
        H = int(input('\nВведи H: '))
        print(f'\nt = {1 / H}')
        vopros()

    elif var_to_find ==  "3":
        H = int(input('\nВведи H: '))
        t = int(input('\nВведи t: '))
        b = int(input('\nВведи b: '))
        print(f'\nI = {H * t * b}')
        vopros()

    elif var_to_find == "4":
        I = int(input('\nВведи I: '))
        H = int(input('\nВведи H: '))
        b = int(input('\nВведи b: '))
        print(f'\nt = {I / (H * b)}' )
        vopros()

    elif var_to_find == "5":
        b = int(input('\nВведи: b: '))
        print(f'\nK = {2**b}' )
        vopros()
    else:
        print("\nВводить значения только от 1 до 5!")
        sound_not15()
        
        

def f11():
    type_of_data = input("\nС каким типом данным хотите работать?\n1)Изображение \n2)Звук \n3)Информация \n4)Выйти из программы \nВведите цифру: ")
    if type_of_data == "1":
        image()
    elif type_of_data == "2":
        sound()
    elif type_of_data == "3":
        info()
    elif type_of_data == "4":
        print()
    else:
        print("\nВводи значения только от 1 до 4!")
        f11_not15()

def vopros():
    vopros = input('\nВы хотите решить ещё одну задачу? \n1)Да \n2)Нет \nВведите нужную вам цифру: ')
    if vopros == '1':
        f11()
    elif vopros == '2':
        vopros_no()
    elif vopros !=(1,2):
        print("\nВводить значения только 1 или 2!")
        vopros_not_1_2()

def vopros_no():
    print()

def vopros_not_1_2():
    vopros()

def info_not_1_to_4():
    info()

def var_to_find_2_not12():
    var_to_find_2()

def var_to_find_3_not12():
    var_to_find_3()

def what_to_use_4_not12():
    what_to_use_4()

def image_not12():
    image()

def sound_not15():
    sound()

def f11_not15():
    f11()

def var_to_find_2():
    what_to_use = input('\nЧто вы хотите использовать? \n1)N \n2)I,K \nИспользую: ')

    if what_to_use == '1':
        N = int(input('\nВведи N: '))
        print(f'\ni={log2(N)}')
        vopros()

    elif what_to_use == '2':
        K=int(input('\nВведите K: '))
        I=int(input('\nВведите I: '))
        print(f'\ni={I / K}')
        vopros()
    elif what_to_use !="1" "2":
        print('\nВводить значения только 1 или 2!')
        var_to_find_2_not12()

def var_to_find_3():
    what_to_use = input('\nЧто вы хотите использовать? \n1)N,K \n2)i,K \nИспользую: ')

    if what_to_use == "1":
        K=int(input('\nВведите K: '))
        N=int(input('\nВведите N: '))
        i = log2(N)
        print(f'\nI={K * i}')
        vopros()

    elif what_to_use == "2":
        K=int(input('\nВведите K: '))
        i=int(input('Введите i: '))
        print(f'\nI={K * i}')
        vopros()
                
    else:
        print('\nВводить значения только 1 или 2!')
        var_to_find_3_not12()

def what_to_use_4():
    what_to_use = input('\nЧто вы хотите использовать? \n1)N,I \n2)i,I \nИспользую: ')

    if what_to_use == '1':
        N=int(input('\nВведите N: '))
        I=int(input('\nВведите I: '))
        i = log2(N)
        print(f'\nK={I / N}')
        vopros()

    elif what_to_use == '2':
        i=int(input('\nВведите i: '))
        I=int(input('\nВведите I: '))
        print(f'\nK={I / i}')
        vopros()
    else:
        print("\nВводить значения только 1 или 2!")
        what_to_use_4_not12()




if __name__ == '__main__':
    f11()
