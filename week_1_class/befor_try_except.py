while True:
    hours = raw_input('enter the hours : ')
    rate = raw_input('enter the rate : ')
    try:
        pay = int(hours)*int(rate)
        print pay
        break
    except:
        print 'please enter the number'
    

