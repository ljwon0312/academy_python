with open('sequence.protein.fasta','r') as f:
    ll = f.read().split()
    la = ' '.join(ll[:4])
    ss = ''.join(ll[4:])
print(la+'\n'+ss)

