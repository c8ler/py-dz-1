# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def check_x_y(x, y):
    if x > 0 and y > 0:
        print('1')
    elif x < 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:
        print('3')
    elif x > 0 and y < 0:
        print('4')
    elif x == 0 and y != 0:
        print('Координаты на оси X')
    elif x != 0 and y == 0:
        print('Координаты на оси Y')
    elif x == 0 and y == 0:
        print('X и Y равны 0')
    return


number1 = input('Введите координату X: ')
number2 = input('Введите координату Y: ')

try:
    number1 = float(number1)
    number2 = float(number2)
    check_x_y(number1, number2)
except:
    print('Введите числа!')