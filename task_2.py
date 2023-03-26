a=int(input('число: '))
b=int(input('степень: '))

def sqr(n = 1, sqr2 = 1):
    if sqr2 <= b:
        n = n*a
        sqr2 += 1
        return sqr(n, sqr2)

    else:
        print(n)
print(sqr())