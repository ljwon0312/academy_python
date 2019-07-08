while True:
    string = input('enter the string : ')
    character = input('enter the character : ')
    try:
        print(string[string.index(character):string.index(character)+3])
        break
    except:
        print('Error : try again')
