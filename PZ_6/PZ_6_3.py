# Дано множество A из N точек (точки заданы своими координатами х, у).
# Среди всех точек этого множества, лежащих во второй четверти, найти точку, наиболее удаленную от начала координат.
# Если таких точек нет, то вывести точку с нулевыми координатами.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс, второй — для хранения ординат.

from math import sqrt

N = 3

a = [2, -5, 3]
b = [-1, 3, 0]

def da(x,y):
    a = 0
    b = 0
    for i in x:
        if i < 0 and i < a:
            a = i
        if all(i > 0 for i in x):
            return "0 0"

    for j in y:
        if j > 0 and j > b:
            b = j
        if all(j < 0 for j in y):
            return "0 0"
    return a,b

print(da(a, b))