"""
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. Температуры – 
целые числа и лежат вдиапазоне от –50 до 50
"""
days = int(input("Input quality of days: "))
count = 0
current_count = 0

for i in range(days):
    temperature = int(input("Input a temp of this day: "))

    if temperature > 0:
        current_count += 1
    elif current_count > count:
        count = current_count
        current_count = 0
    else:
        current_count = 0
if current_count > count:
    count = current_count

print("result is ",count)