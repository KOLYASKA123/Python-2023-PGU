def main():

    while 1:
        
        a = int(input("Введите произвольное число: "))
        b = int(input("Введите пограничное число: "))

        print(f'a {"> 3 *" if a / b > 3 else ">" if a > b else "<"} b')

if __name__ == '__main__': main()