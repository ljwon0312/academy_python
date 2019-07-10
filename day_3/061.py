with open('061.fastq','r') as fr:
    ll = fr.readlines()
    ls = [ll[k].strip() for k in range(len(ll)) if k%4==1]
    seq = ''.join(ls)
    print(len(seq))




