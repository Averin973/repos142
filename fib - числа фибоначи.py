fib1 = 0
fib2 = 1
p = input("номер элемента: ")
p = int(p)
i = 0
while i < p:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    print(fib2)
