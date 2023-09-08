# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = a1 = int(input("Enter the first element of arithmetic progression: "))
difference_elements = d = int(input("Enter the difference: "))
amount_elements = n = int(input("Enter the amount of elements: "))

for i in range(n):
    print(a1 + i * d, end=" ")