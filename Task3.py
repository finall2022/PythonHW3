# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

#     Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# РЕШЕНО!!!

def fmin(x):
    xmin = x[0]
    for j in range(len(x)):
        if xmin > x[j] and x[j] != 0:
            xmin = x[j]
    return xmin

def fmax(x):
    xmax = x[0]
    for j in range(len(x)):
        if xmax < x[j] and x[j] != 0:
            xmax = x[j]
    return xmax

def frem(x):
    y = []
    for i in range(len(x)):
        rem = round((x[i] - int(x[i])), 2)
        y.append(rem)
    print(f'\na = {x}')
    print(f'b = {y}')
    return y

a = [1.1, 1.2, 3.1, 5, 10.01]

b = frem(a)
min = fmin(b)
max = fmax(b)

print(f'\nминимальная дробная часть = {min}\nмаксимальная дробная часть = {max}\n')
print(f'Разница между максимальным и минимальным значением дробной части элементов = {max - min}')