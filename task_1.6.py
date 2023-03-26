import random
r = random.randint(1, 100)
print('я загадал число от 1 до 100, попробуй угадай за 10 попыток')
def guess_num(attempts = 1):
    user_nmb = int(input('введи число: '))

    if attempts < 10:
        if user_nmb > r:
            print('это число больше загаданного')
            attempts += 1
            return guess_num(attempts)
        elif user_nmb < r:
            print('это число меньше чем я загадал')
            attempts += 1
            return guess_num(attempts)
        else:
            print('возьми медальку с полочки, ты угадал')
    else:
        print(f'Хватит, я загадал число: {r}')
print(guess_num())




