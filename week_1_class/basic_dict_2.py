string = input('enter the string : ')

'''
ll = ','.join(string).split(',')
ll = [string[a] for a in range(len(string))]
'''

ld= {}
for k in string:
    try:
        ld[k] +=1
    except:
        ld[k] = 1

keys = sorted(ld.keys())
for i in keys:
    print(i,':',ld[i])



