with open('sequence.nucleotide.gp.gb','r') as f:
    ll = f.readlines()
    seq = ''
    a=0
    b=0
    for k in ll:
        if k.startswith('     CDS'):
            a=1
        elif a==1:
            if k.startswith('                     /translation'):
                b=1
                seq+=k.split('"')[-1].strip()
            elif k.startswith('     STS'):
                break
            elif b==1:
                seq+=k.strip()
print(seq[:-1]+"*")


