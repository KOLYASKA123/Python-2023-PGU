from unittest import TestCase, main
from HomeworkAndUnittests.Homework_1 import sravnitel, iteration


class TestHomework1(TestCase):
    
    def test_a_bigger_b(self):
        
        self.assertEqual(sravnitel(2, 1), 'a > b')
        
    def test_a_smaller_b(self):
        
        self.assertEqual(sravnitel(1, 2), 'a < b')
        
    def test_a_bigger_3b(self):
        
        self.assertEqual(sravnitel(4, 1), 'a > 3 * b')
        
    def test_is_not_numbers(self):
        
        with self.assertRaises(ValueError) as e:
            iteration('abc', 'cba')
        self.assertEqual('Похоже, вы ввели какие-то символы, которые не позволяют сделать преобразование в число с плавающей точкой.', e.exception.args[0])
        
if __name__ == '__main__':
    main()