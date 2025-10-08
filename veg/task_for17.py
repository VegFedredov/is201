A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое число N (> 0): "))

sum_result = 1.0
current = 1.0

for i in range(1, N + 1):
    current = current * A
    sum_result = sum_result + current

print("Сумма:", sum_result)