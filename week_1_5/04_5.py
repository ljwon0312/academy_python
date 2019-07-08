with open('sequence.nucleotide.gp.gb','r') as f:
    ll = f.readlines()
    title_list = 'TITLE\n'
    a=''
    for i in range(len(ll)):
        if ll[i].startswith('  TITLE'):
            a=ll[i][7:-1]
        elif ll[i].startswith('  JOURNAL'):
            title_list += a+'\n'
            a=''
        else:
            a+=' '+' '.join(ll[i].split())
print(title_list)



