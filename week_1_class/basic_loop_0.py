n = ''
while True:
    a = input('Enter a number : ')
    try:
        int(a)
        n +=  a+' '
    except:
        if a == 'done':
            print(n)
            break
        else:
            print('Please enter a number')
            continue

