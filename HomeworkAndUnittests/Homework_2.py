def SkipTheThirdLetter(string: str):
    
    return string[:2] + string[3:]

def LookingForC(string: str):

    if 'c' in string: return 'Найдена буква "c".'
    else: return 'Буква "c" не найдена.'

def LenOfString(string: str):

    return len(string)

def SkipTheLastLetter(string: str):

    return string[:-1]

def iteration(string: str):
    
    if len(string) < 3: raise ValueError('В строке должно быть >= 3 символов, иначе первое задание не имеет смысла.')
    
    print(f'\nСтрока без третьего символа: {SkipTheThirdLetter(string)}')
    print(f'Поиск буквы "c": {LookingForC(string)}')
    print(f'Длина строки: {LenOfString(string)}')
    print(f'Строка без последнего символа: {SkipTheLastLetter(string)}\n')
    

def main():
    
    while True:
    
        someString = input('Введите произвольную строку: ')
        iteration(someString)


if __name__ == '__main__': main()