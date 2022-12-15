def morze():
    morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}
    word=input("Введите слово на английском языке: ")
    morze_word=' '
    for letter in word:
        letter=letter.lower()
        print(f"{letter}: {morze[letter]}")

def n10():
    n10 = int(input('n10 = '))
    p = int(input('p = '))
    k = 1
    np = 0
    while not n10 == 0:
        np = np + (n10 % p)*k
        k = k*10
        n10 = n10 // p
    print (f'N{p} = {np}')

def tabl():
    p = int(input('Введите p (2<p<=10): '))
    print (f'{p}-ичная таблица умножения')
    for x in range (1,p):
        for y in range (1,p):
            z = (x*y // p)*10+(x*y)%p
            print (z, end = ' ')
        print ()


