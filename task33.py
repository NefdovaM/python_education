# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def input_num(msg: str):
    while True:
        num = input(msg)
        if num.isdigit():
            num = int(num)
            return num

amount = input_num("Enter amount of grades you want to input: ")
grade = [] # list()

for _ in range(amount):
    user_input = input_num("Enter a grade: ")
    grade.append(user_input)

def max_to_min(arr: list):
    max_num = max(arr)
    min_num = min(arr)
    # iterations = arr.count(max_num)
    # for _ in range(iterations):
    #     arr[arr.index(max_num)] = min_num 
    for i in range(len(arr)):
        if arr[i] == max_num:
            arr[i] = min_num

max_to_min(grade)
print(grade)