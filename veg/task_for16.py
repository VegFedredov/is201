A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое число N (> 0): "))

for i in range(1, N + 1):
    print(f"{A}^{i} = {A ** i}")