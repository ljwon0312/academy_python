while True:
    try:
        num = int(input('Enter : '))
        print(10/num)
        break
    except ValueError:
        print('not numeric')
    except ZeroDivisionError:
        print('Don\'t enter Zero')



