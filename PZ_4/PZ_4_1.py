A = int(input("Введите число А: ")) #Ввод А
B = int(input("Введите число В: ")) #Ввод B

S = 0

if A>B:
    for i in range(A-1, B, -1):
        print("Числа в прорядке убывания: ", i)
    S = A - B - 1

    print("количество чисел: ", S)
else:
    print("A должно быть больше В (A>B)")

if A<B:
    print("A должно быть больше В (A>B)")
