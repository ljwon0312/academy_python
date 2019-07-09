with open('tsv.tsv','r') as f:
    for k in f:
        print(k.split('\t'))
        print(k.split(' '))


