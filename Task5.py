# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

#     Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#РЕШЕНО!!!

x = int(input('Введите число '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def nfib(n):
    if n in [0, 1]:
        return 1
    else:
        return nfib(n-2) - nfib(n-1)


a = []
b = []
for e in range(2, x+3):
    a.append(nfib(e))
a.reverse()

for e in range(1, x+1):
    b.append(fib(e))
print(a + b)  
