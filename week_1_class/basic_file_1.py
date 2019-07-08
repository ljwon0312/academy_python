ff = input('enter the file name : ')
nn = input('enter the number : ')
with open(ff,'w') as f:
    for i in range(1,10):
        f.write('{0} * {1} = {2}\n'.format(nn, i, int(nn)*i))

t = 0
n = 0
'''
p = open(ff,'r')
'''
with open(ff,'r') as p:
    for i in p:
        for k in i.split():
            try:
                t+=int(k)
                n+=1
            except:
                pass
    print(t,n,t/n)
'''
p.close()
'''

