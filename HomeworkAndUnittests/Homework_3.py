def FindLongestAndFrequentWord(listOfWords: list[str]):

    unicWords = set(listOfWords)
    longest_word = ''
    frequent_word = ''

    for i in unicWords:

        if len(i) > len(longest_word):
            
            longest_word = i
            
        if listOfWords.count(i) > listOfWords.count(frequent_word):
            
            frequent_word = i
    
    return longest_word, frequent_word

def iteration(someString):
    
    if len(someString) == 0: raise ValueError('Вы ничего не ввели.')
    result = FindLongestAndFrequentWord(someString)
    
    print(f'\nСамое большое слово: {result[0]}')
    print(f'Самое часто встречающееся слово (возможно, единственное): {result[1]}\n')

def main():
    
    while True:
        
        someString = input("Введите произвольную строку: ")
        someString = someString.split()
        print(len(someString))
    
        iteration(someString)


if __name__ == '__main__': main()