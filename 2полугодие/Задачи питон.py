def f5():
for N in range(516):
    b=f'{N:b}'
    if n=N % 2 ==0:
        b+= '10'
    else:
        b= '1' +b+'01'
    if int(b, 2) > 516:
        print(N)
        break
def f5_1():
    for i in range(1, 100):
        s = bin(i)[2:] # перевод в двоичную систему
        s = str(s)
        if i % 2 == 0:
            s += "10"
        else:
            s = "1" + s + "01"
        if int(s, 2) > 441:
            print(i)
        
def f6():
    from turtle import *
    left(90)
    for i in range(7):
        forward(300)
        right(120)
    pu()
    for x in range(1,9):
        for y in range(1,10):
            goto(x*30,y*30)
            dot(5)
    done()
def f6_1():
    s = int(input())
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    print(n)
def f8():
    from itertools import product
    nums=product('01234567', repeat=5)
    k=0
    n='16 36 56 76 61 63 65 67'
    nn=n.split()
    for n in nums:
        numb=''.join(n)
        sp=[]
        if numb.count('6')==1 and numb[0]!='0':
            for x in nn:
                if x in numb:
                    sp.append(x)
            if not sp:
                k+=1
    print(k)

    
    
    с=0
for i in range(1,1000):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo=num[2:]+'101'

    if num.count('1')%2!=0:
        chislo=num[2:]+'011'
    if int(chislo,2)>200 and imt(chislo,2)%2==0:
        print (i, int(chislo,2))
        c+=1
        break
 if c==0
     print( 'нету')

    
  f6  
from turtle import *
left(90)
for i in range(1):
    forward(300)
    right(90)
    forward(300)
    right(135)
    forward(424)
pu()
for x in range(16):
    for y in range(16):
        goto(x*20,y*20)
        dot(5)
done()


   from turtle import *
for i in range(1):
    right(90)
    forward(300)
    left(90)
    forward(300)
    left(135)
    forward(424)
pu()
for x in range(0,17):
    for y in range(-16,1):
        goto(x*20,y*20)
        dot(5)
done()
