def mySum(a,b):
    return int(a)+int(b)
while True:
    ch = input('enter a pair of number : ')
    try:
        print(mySum(ch.split(',')[0], ch.split(',')[1]))
    except:
        break



