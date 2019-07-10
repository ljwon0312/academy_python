with open('077.bed','r') as fr:
    leng = 0
    for k in fr:
        leng+= int(k.split()[2])-int(k.split()[1])
print(leng)




