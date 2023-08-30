"""
Задача 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
[1, 1, 2, 0, -1, 3, 4, 4] / output 6
Примечание: Пользователь может вводить значения списка или список задан изначально.
"""
#numbers = [1, 1, 2, 0, -1, 3, 4, 4] # type = list
numbers = list()
amount = int(input("Enter amount of values you want to input: "))
for _ in range(amount):
    numbers.append(int(input("Enter a value: ")))
print(len(set(numbers)))