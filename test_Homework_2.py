from unittest import TestCase, main
from Homework_2 import SkipTheThirdLetter, LookingForC, LenOfString, SkipTheLastLetter, iteration


class TestHomework2(TestCase):
    
    def test_SkipTheThirdLetter(self):
        
        self.assertEqual(SkipTheThirdLetter('abcd'), 'abd')
        
    def test_LookingForC(self):
        
        self.assertEqual(LookingForC('abcd'), 'Найдена буква "c".')
        self.assertEqual(LookingForC('abd'), 'Буква "c" не найдена.')
        
    def test_LenOfString(self):
        
        self.assertEqual(LenOfString('abcd'), 4)
        
    def test_SkipTheLastLetter(self):
        
        self.assertEqual(SkipTheLastLetter('abcd'), 'abc')
        
    def test_iteration(self):
        
        with self.assertRaises(ValueError) as e:
            iteration('ab')
        self.assertEqual('В строке должно быть >= 3 символов, иначе первое задание не имеет смысла.', e.exception.args[0])
    
        
if __name__ == '__main__':
    main()