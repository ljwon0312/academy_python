with open('sequence.nucleotide.gp.gb','r') as f:
    ll = f.readlines()
    title_list = 'TITLE\n\n'
    a=0
    for i in range(len(ll)):
        if a==0:
            if ll[i].startswith('  TITLE'):
                a=1
            else:
                pass
        if ll[i].startswith('  JOURNAL'):
            a=0
        elif a==1:
            title_list+=ll[i][7:]
print(title_list)



