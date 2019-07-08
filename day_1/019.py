try:
    with open('noname.txt','r') as fr:
        read = fr.readlines()
    print(read)
except:
    print('file doesn\'t exsist')



