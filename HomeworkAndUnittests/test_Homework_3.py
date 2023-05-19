from unittest import TestCase, main
from HomeworkAndUnittests.Homework_3 import iteration, FindLongestAndFrequentWord


class TestHomework3(TestCase):
    
    def test_longest_word(self):
        
        self.assertEqual(FindLongestAndFrequentWord(['abc', 'abcd'])[0], 'abcd')
        
    def test_frequent_word(self):
        
        self.assertEqual(FindLongestAndFrequentWord(['abc', 'abc', 'abcd'])[1], 'abc')
    
    def test_iteration(self):
        
        with self.assertRaises(ValueError) as e:
            iteration([])
        self.assertEqual('Вы ничего не ввели.', e.exception.args[0])
        
if __name__ == '__main__':
    main()