N = int(input("Введите целое число N (> 0): "))
product = 1.0
for i in range(1, N + 1):
    product *= 1 + i / 10
print("Произведение:", product)