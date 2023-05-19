from unittest import TestCase, main
from HomeworkAndUnittests.Homework_4 import calc
import math

class TestHomework4(TestCase):
    
    def test_abs(self):
        
        self.assertEqual(calc('abs(-5)'), 5)
        
    def test_factorial(self):
        
        self.assertEqual(calc('factorial(5)'), 120)
        
    def test_randint(self):
        
        self.assertEqual(calc('randint(5, 5)'), 5)
        
    def test_acos(self):
        
        self.assertEqual(calc('acos(-1)'), math.pi)
        
    def test_asin(self):
        
        self.assertEqual(calc('asin(-1)'), -math.pi/2)
        
    def test_sin(self):
        
        self.assertEqual(calc('sin(pi/4)'), (2 ** 0.5) / 2)
        
    def test_cos(self):
        
        self.assertEqual(calc('cos(pi/4)'), (2 ** 0.5) / 2)
        
    def test_NameError(self):
        
        with self.assertRaises(NameError) as e:
            calc('strange_function("someParameter")')
        self.assertEqual('Ошибка. Вероятно, в введённых вами инструкциях несуществующая функция.', e.exception.args[0])
        
    def test_ZeroDivisionError(self):
        
        with self.assertRaises(ZeroDivisionError) as e:
            calc('5/0')
        self.assertEqual('На ноль делить нельзя.', e.exception.args[0])
        
    def test_SyntaxError(self):
        
        with self.assertRaises(SyntaxError) as e:
            calc('C++')
        self.assertEqual('Вы что-то как-то неправильно написали...', e.exception.args[0])
        
    def test_TypeError(self):
        
        with self.assertRaises(TypeError) as e:
            calc('abs([2, 2, 2])')
        self.assertEqual('Возможно, вы неправильно использовали функцию.', e.exception.args[0])
    
    def test_ValueError(self):
        
        with self.assertRaises(ValueError) as e:
            calc('acos(pi)')
        self.assertEqual('Возможно, вы попытались передать неправильное значение в какую-то функцию.', e.exception.args[0])
    
if __name__ == '__main__':
    main()