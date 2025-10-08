# This program creates a list of the first N positive odd numbers.

N = int(input("Enter a positive integer N: "))

if N > 0:
    # Create a list of odd numbers: 1, 3, 5, ...
    odd_numbers = []
    for i in range(N):
        odd_numbers.append(2 * i)
    print(odd_numbers)
else:
    print("N must be greater than 0")