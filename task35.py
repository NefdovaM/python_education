# Задача №35. Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def simple(n):
    for div in range(2, int(n**0.5)+1):
        if n % div == 0:
            return "Not prime"
    return "Prime"

num = int(input("Enter your number: "))
print(simple(num))


# def prime(n):
#     i = 2
#     flag = True
#     while i < n and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return "yes"
#     return "no"
# n = num = int(input("Enter your number: "))
# print(prime(n))