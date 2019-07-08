ll = input("enter the string : ").split(',')
l1 = [int(i.strip()) for i in ll]
l2 = sorted(l1)
l3 = sorted(l1)[::-1]

'''
l2 = l1[:]
l2.sort()
l3 = l2[::-1]
l3.sort(reverse = True)
'''
if l1 == l2:
    print('ascending')
elif l1 == l3:
    print('descending')
else:
    print('not sorted')

