def user_number(x, reverse = 0):
    if x == 0:
        print(reverse)
    else:
        cur_nmb = x % 10
        x = x // 10
        reverse = reverse * 10
        reverse = reverse + cur_nmb
        return user_number(x, reverse)

x = int(input("Введите число: "))
user_number(x)