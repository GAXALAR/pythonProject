earnings = int( input('Введите сумму выручки: '))
if earnings == 0:
    print('Вы ничего не заработали, старайтесь больше')
elif earnings < 0:
    print('Возможно ведение бизнеса не самая сильная ваша сторона')
else:
    loss = int( input('Введите сумму убытков: '))
    employee = int( input('Введите кол-во сотрудников: : '))
    profit = earnings - loss
    profitMargin = profit/earnings
    employeeProfitMargin = profit/employee
    print(f'Прибыль составляет: {profit}')
    print(f'Рентабельность: {round(profitMargin, 1)}')
    print(f'Прибыль фирмы в расчете на одного сотрудника: {round(employeeProfitMargin, 2)}')
