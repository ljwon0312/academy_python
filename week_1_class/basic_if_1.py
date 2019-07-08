try:
    hours = int(input('enter hours : '))
    rate = int(input('enter rate : '))
except:
    print('not numeric')
else:
    if int(hours)>=100:
        print('pay : '+str(int(hours)*int(rate)*2))
    else:
        print('pay : '+str(int(hours)*int(rate)))

