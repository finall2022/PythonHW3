# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

#     Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# РЕШЕНО!!!
print('Программа для перевода десятичного числа в двоичное')
print('Введите число')
numDec = int(input())

def decToBin(nd):
    list = []
    while nd != 0:
        nr = nd % 2
        list.append(str(nr))
        nd //= 2
    return list

print(''.join(reversed(decToBin(numDec))))