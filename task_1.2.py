def user_number(x, even=0, odd=0):
    if x == 0:
        print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    else:
        cur_nmb = x % 10
        x = x // 10
        if cur_nmb % 2 == 0:
            even += 1
        else:
            odd += 1
        return user_number(x, even, odd)

x = int(input("Введите число: "))
user_number(x)