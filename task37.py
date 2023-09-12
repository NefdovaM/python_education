# Задача №37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3 

def posled(n):
    if n == 0:
        return ""
    k = input("Enter your number: ")
    return posled(n-1) + " " + k

num = int(input("Enter a quantity of numbers: "))
print(posled(num))