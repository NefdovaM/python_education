"""
Задача 18. Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
list_1 = [1, 2, 3, 4, 5]
k = 6
"""
list_1 = [1, 12, 6, 7, 8, 15]
k = 11
number = 0
for i in range(len(list_1)):
    if (k - list_1[i]) < k - number:
        number = i
print(list_1[number])