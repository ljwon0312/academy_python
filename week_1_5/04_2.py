s1 = 'title : '
s2 = 'seq : '

with open('sequence.protein.fasta.gb.gp','r') as f:
    p = f.readlines()
    for k in p:
        if k.startswith('LOCUS'):
            s1 += k
        else:
            try:
                int(k.split()[0])
                s2 += ''.join(k.split()[1:])
            except:
                pass
print(s1+s2)



