n=0
t=0
while True:
    a = input('Enter a number : ')
    try:
        t+= int(a)
        n+=1
    except:
        if a == 'done':
            print(str(t),str(n),str(t/n))
            break
        else:
            print('Please enter a number')
            continue

