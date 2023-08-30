"""
Задача 21. Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально. Пользователь его не вводит
"""

user_input = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
    {" VIII":" S007 "}
]
my_set = set()
for dictionary in user_input:
    for value in dictionary.values():
        my_set.add(value)

print(my_set)