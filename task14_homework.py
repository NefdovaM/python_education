# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

n = int(input('Введите число: '))
two_squared = 1
count = 0
while two_squared <= n:
    two_squared *= 2
    count += 1
    print(two_squared//2, end=" ")