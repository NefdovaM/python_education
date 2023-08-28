# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

num_Of_Coins = 6 #int(input("Введите количество монет: "))
import random
arr = [random.randint(0,1) for i in range(num_Of_Coins)]
print(*arr)
eagle_count = 0
tails_count = 0
for i in range(num_Of_Coins):
    if arr[i] == 0:
        eagle_count += 1
    else:
        tails_count += 1
print(eagle_count, tails_count)

if eagle_count == 0 or tails_count == 0:
    print("все монеты перевернуты одной стороной")
elif eagle_count > tails_count:
    print(f"Минимальное количество монет - {tails_count}")
elif eagle_count < tails_count:
    print(f"Минимальное количество монет - {eagle_count}")
else:
    print("Количество монет равно")