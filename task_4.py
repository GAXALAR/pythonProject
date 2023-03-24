
def my_func():
    a = int(input('введите число а: '))
    b = int(input('введите число в: '))
    c = int(input('введите число с: '))
    my_list=[a,b,c]
    my_list.sort()
    return my_list[1]*my_list[2]



def my_func_2():
    a = int(input('введите число а: '))
    b = int(input('введите число в: '))
    c = int(input('введите число с: '))
    my_list=[a,b,c]
    return (a*b*c)/min(my_list)

print(my_func_2())
