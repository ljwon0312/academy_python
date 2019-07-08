#1
with open('title.txt','w') as f:
    f.write('This is a sequence file.')
#2
with open('title.txt','r') as f:
    l = f.read()
print('The first line is : {0}'.format(l))

