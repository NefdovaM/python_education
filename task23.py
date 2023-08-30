"""
Задача 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения списка или список задан изначально.
"""
amount = int(input("Enter amount of number you want to insert: "))
numbers = list()
for _ in range(amount):
    numbers.append(int(input("Enter a number: ")))
count = 0
for i in range(1, len(numbers)):
    if numbers[i-1]<numbers[i]:
        count += 1
print(f"{numbers}, amount of numbers: {count}")