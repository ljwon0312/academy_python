ll = [3,1,1,2,0,0,2,3,3]
dicti = {}
for k in ll:
    try:
        dicti[k]+=1
    except:
        dicti[k]=1
print(dicti)

