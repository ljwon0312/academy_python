while True:
    n = input('Enter a number : ')
    try:
        for i in range(1,10):
            print(n+' * '+str(i)+' = '+str(int(n)*i))
        break
    except:
        print('Error : try again')

