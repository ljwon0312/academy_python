import re
with open('sequence.protein.2.fasta','r') as f:
    sequence = f.readlines()[1]
    ls  = []
    while True:
        aa = input('Searching for : ')
        if aa == 'XXX':
            print('Okay, I will stop.')
            break
        else:
            ll = re.compile(aa).finditer(sequence)
            for k in ll:
                ls.append(str(k.start()))
            print('Found at : '+', '.join(ls))


