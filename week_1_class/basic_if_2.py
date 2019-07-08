s = input('Enter score : ')
try:
    score = float(s)
except:
    print('Not numeric')
else:
    if score >1.0:
        print('Score is out of range')
    elif score >=0.9:
        print('A')
    elif score>=0.8:
        print('B')
    elif score>=0.7:
        print('C')
    elif score>=0.6:
        print('D')
    elif score>0:
        print('F')
    else:
        print('Score is out of range')

