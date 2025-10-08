# Запрашиваем у пользователя целое число N больше 0
N = int(input("Введите целое число N (> 0): "))

# Формируем список степеней двойки от 2^1 до 2^N
powers_of_two = []
for i in range(1, N + 1):
    powers_of_two.append(2 ** i)

# Выводим полученный список
print(powers_of_two)