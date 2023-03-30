def FindTheBiggestWord(listOfWords):

    unicWords = set(listOfWords)
    word = ''

    for i in unicWords:

        if len(i) > len(word):
            
            word = i
    
    print(f'Самое большое слово: {word}')


def FindTheMostFrequentWord(listOfWords):

    unicWords = set(listOfWords)
    word = ''
    
    for i in unicWords:

        if listOfWords.count(i) > listOfWords.count(word):

            countOfWords = listOfWords.count(i)
            word = i

    print(f'Самое часто встречающееся слово (возможно, единственное): {word}')

def main():

    someString = input("Введите произвольную строку: ")
    someString = someString.split()
    FindTheMostFrequentWord(someString)
    FindTheBiggestWord(someString)


if __name__ == '__main__': main()