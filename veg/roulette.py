import random

baraban = [0, 0, 0, 0, 1, 0]
lives = 0

while True:
    result = baraban[random.randint(0, 5)]
    if result == 1:
        print('стреляет игрок: 1 (Game Over)')
        break
    else:
        lives += 1
        print('стреляет игрок: 0 (You survived)')

print(f'Вы выжили {lives} раз(а)')
