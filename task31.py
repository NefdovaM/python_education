# Задача №31. 
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def find_nth_fib(n):
    if n in [1,2]:
        return 1 
    return find_nth_fib(n -1) + find_nth_fib(n - 2)
print(find_nth_fib(7))