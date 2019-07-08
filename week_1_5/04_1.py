with open('sequence.protein.fasta.gb.gp','r') as f:
    ll = f.readlines()
    for k in ll:
        if k.startswith('ORIGIN'):
            n= ll.index(k)
            seq = ''.join(ll[n+1:])
    print('title : '+ll[0]+'seq : '+seq)



