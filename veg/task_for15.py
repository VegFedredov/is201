A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое число N (> 0): "))

result = 1
for _ in range(N):
    result *= A

print(f"{A} в степени {N} = {result}")