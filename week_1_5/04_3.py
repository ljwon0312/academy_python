s1 = ''
with open('sequence.protein.fasta.gb.gp','r') as f:
    ll = f.readlines()
    for k in ll:
        try:
            int(k.split()[0])
            s1 += ''.join(k.split()[1:])
        except:
            pass
    n=0
    while n*70<len(s1):
        n+=1
        print(s1[70*(n-1):70*n])



