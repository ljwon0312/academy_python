a = []
while True:
    n = input('Enter a number : ')
    try:
        number = int(n)
        if 0<= number <=100:
            a.append(number)
            a.sort()
        else:
            print('Please enter a number in range(1,100)')
    except:
        if n == 'done':
            print(a[-1])
            print(a[0])
            break
        else:
            print('Please enter a number')


