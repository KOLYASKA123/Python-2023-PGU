from math import *
from random import *

def calc():

    expression = input('>>> ')

    if expression.find('stop') != -1: exit()

    try:

        result = eval(expression)
        print(f' = {result}')

    except NameError: print('Ошибка. Вероятно, в введённых вами инструкциях несуществующая функция.')
    except ZeroDivisionError: print('На ноль делить нельзя, олух.')
    except SyntaxError: print('Вы что-то как-то неправильно написали...')

def main():
    
    while True: calc()

if __name__ == '__main__': main()