def calc():
    symbol = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if symbol in ['0', '+', '-', '*', '/']:

        if symbol == '0':
            print('Всего доброго')
            exit()

        a = int(input())
        b = int(input())
        if symbol == '*':
            print(a*b)
            return calc()
        if symbol == '/':
            try:
                print(a/b)
            except:
                print('на ноль делить нельзя')
            return calc()
        if symbol == '-':
            print(a-b)
            return calc()
        if symbol == '+':
            print(a + b)
            return calc()
    else:
        print('Вы ввели неверный символ, попробуйте еще раз')
        return calc()



print(calc())




