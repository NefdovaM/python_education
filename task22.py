"""
Задача 22. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

"""

numbers1 = list()
numbers2 = list()


count1 = int(input("Enter the number of elements of the first set: "))
for _ in range(count1):
    numbers1.append(int(input("Enter an element of the first set: ")))

count2 = int(input("Enter the number of elements of the second set: "))    
for _ in range(count2):
    numbers2.append(int(input("Enter an element of the second set: ")))


print(*numbers1)
print(*numbers2)
result = list(set(numbers1) & set(numbers2))
result.sort()
print(*result)


# from random  import randint
# list1 = list(randint(1, 40) for _ in range(int(input("Enter the number of elements of the first set: "))))
# list2 = list(randint(1, 40) for _ in range(int(input("Enter the number of elements of the second set: "))))
# print(list1, list2)
# result = list(set(list1) & set(list2))
# result.sort()
# print(*result)