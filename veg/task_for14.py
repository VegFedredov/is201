N = int(input("Введите целое число N (> 0): "))
sum_ = 0
for i in range(1, N + 1):
    term = 2 * i - 1
    sum_ += term
    print(sum_)