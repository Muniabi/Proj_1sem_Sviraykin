a = "*"
N = int(input("Сколько звёздочек в строке хотите? ")) # ввод количества строк
for i in range(1,N+1): # цикл для обработки количества столбцов
    print(i, "(номер строки = кол-во звёздочек)")
    print(a*i) # printing stars
