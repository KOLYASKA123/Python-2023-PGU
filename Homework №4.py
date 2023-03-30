from math import *
from random import *

def calc():

    expression = input('>>> ')

    if expression.find('stop') != -1: exit()

    try:

        eval(expression)
        print(f' = {eval(expression)}')

    except NameError: print('Ошибка. Вероятно, в введённых вами инструкциях несуществующая функция.')
    except ZeroDivisionError: print('На ноль делить нельзя, олух.')

def main():
    
    while True: calc()

if __name__ == '__main__': main()