n10 = int(input('n10 = '))
p = int(input('p = '))
k = 1
np = 0
while not n10 == 0:
    np = np + (n10 % p)*k
    k = k*10
    n10 = n10 // p
print (f'N{p} = {np}')
