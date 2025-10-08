N = int(input("Введите N (> 0): "))
result = 0.0
sign = 1

for i in range(1, N + 1):
    result += sign * (1 + i / 10)
    sign *= -1

print(result)