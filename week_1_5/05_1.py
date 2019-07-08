with open('sequence.nucleotide.fasta','r') as f:
    ss = f.readlines()
    sequence = ''
    for k in ss:
        if k.startswith('>'):
            pass
        else:
            sequence+=k.strip()
    n=0
    while n+3<=len(sequence):
        print(sequence[n:n+3])
        n+=3




