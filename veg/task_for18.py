A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое число N (> 0): "))

result = 1.0
sign = -1

for k in range(1, N + 1):
    term = sign * (A ** k)
    result = result + term
    sign = sign * -1

print("Результат:", result)