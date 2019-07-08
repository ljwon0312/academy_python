import time

while True:
    n = int(input("Which times table : "))
    if 1<=n<=9:
        for k in range(1,10):
            print('{0} * {1} = {2}'.format(n,k,n*k))
        break
    else:
        print('Try again')
        time.sleep(2)


