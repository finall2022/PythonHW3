# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

#     Пример:

# - [2, 3, 5, 9, 3] ->
# на нечётных позициях элементы 3 и 9, ответ: 12
# РЕШЕНО!!!
list = [2, 3, 5, 9, 3, 7, 12, 6]

def fsumm(x):
    s = 0
    for i in range(1, len(x), 2):
        s += x[i]
    return s

print(list)
summ = fsumm(list)
print(summ)