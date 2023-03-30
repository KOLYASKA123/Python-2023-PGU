def SkipTheThirdLetter(string: str):
    
    for i in range(len(string)):
        
        if i != 2: print(string[i], end='')
    
    print()

def LookingForC(string: str):

    for i in string:

        if i == 'c' or i == 'с':
            
            print('Найдена буква "c".')
            return

def LenOfString(string: str):

    counter = 0

    for i in string:

        counter += 1

    print(f'Длина строки: {counter}')

def SkipTheLastLetter(string: str):

    for i in range(len(string)):

        if i != len(string) - 1: print(string[i], end='')

    print()

def main():
    
    someString = input('Введите произвольную строку: ')

    SkipTheThirdLetter(someString)
    LookingForC(someString)
    LenOfString(someString)
    SkipTheLastLetter(someString)

if __name__ == '__main__': main()