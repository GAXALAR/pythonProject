def sum_elem(n):
    if n == 1:
        return 1
    x = 1 / pow(2, n - 1)
    if n % 2 == 0:
        x = -x
    return sum_elem(n - 1) + x

number = int(input())
print(sum_elem(number))