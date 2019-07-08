'''
n = int(input('enter the number : '))
for i in range(1,10):
    if i%2==0:
        print('{0} * {1} = {2}'.format(n,i,n*i))

n = int(input('enter the number : '))
for i in range(2,10,2):
    print(f'{n} * {i} = {n*i}')
'''

n = int(input('enter the number : '))
for i in range(2,10,2):
    print('{0} * {1} = {2}'.format(n,i,n*i))


