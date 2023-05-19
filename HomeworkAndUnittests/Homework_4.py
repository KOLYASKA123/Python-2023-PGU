from math import *
from random import *

def calc(expression):

    try:

        result = eval(expression)
        return result

    except NameError: raise NameError('Ошибка. Вероятно, в введённых вами инструкциях несуществующая функция.')
    except ZeroDivisionError: raise ZeroDivisionError('На ноль делить нельзя.')
    except SyntaxError: raise SyntaxError('Вы что-то как-то неправильно написали...')
    except TypeError: raise TypeError('Возможно, вы неправильно использовали функцию.')
    except ValueError: raise ValueError('Возможно, вы попытались передать неправильное значение в какую-то функцию.')

def main():
    
    print("""
          В этой программе вы можете использовать любые математические функции из библиотеки math.
          Достаточно просто написать нужное вам математическоеи выражение с использованием (или без)
          функций из этой библиотеки. Вот несколько функций, которые вы можете использовать (есть и другие):
          
          factorial(a) | randint(a,b) | abs(a) | acos(a) | asin(a) | cos(a) | sin(a) | exit() - для выхода из программы
          """)
    
    while True:
        
        expression = input('>>> ') 
        print(f' = {calc(expression)}')

if __name__ == '__main__': main()