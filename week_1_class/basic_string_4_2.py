while True:
    n = input('Enter a number : ')
    try:
        number = int(n)
        for i in range(1,10):
            print('{0} * {1} = {2}'.format(number, i, number*i))
        break
    except:
        print('Error : try again')



