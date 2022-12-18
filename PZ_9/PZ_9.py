# Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние температуры по месяцам в году.
# Преобразовать информацию из строки в словарь, с использованием функции найти среднюю и минимальные температуры,
# результаты вывести на экран.

from statistics import mean
a = {}
b = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15 '
b = b.split()
a["2020год"] = b[0]
a['температура'] = []
for i in b[1:12]:
    a['температура'].append(int(i))
F = mean(a['температура'])
print("Средняя температура за год:", round(F,1))
print("Минимальная температура:", min(b, key=lambda i : i[::12]))