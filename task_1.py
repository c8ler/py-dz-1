# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def check_day(day):
    net = [1, 2, 3, 4, 5]
    da = [6, 7]
    if day in net:
        print('нет')
    elif day in da:
        print('да')
    else:
        print('Вы ввели не день недели')


number = input('Введите число дня недели: ')

try:
    number = int(number)
    check_day(number)
except:
    print('Введите целое число')
