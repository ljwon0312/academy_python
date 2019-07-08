codon_dic = {'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',   'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',   'TAT':'Y', 'TAC':'Y', 'TAA':'*', 'TAG':'*',   'TGT':'C', 'TGC':'C', 'TGA':'*', 'TGG':'W',   'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',   'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',   'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',   'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',   'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M',   'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',   'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',   'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',   'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',   'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',   'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',   'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

with open('sequence.nucleotide.fasta','r') as f:
    t = f.read()
    ll = t.split('\n')[1:]
    sequence = ''.join(ll)
    n=0
    while n*60<len(sequence):
        line = sequence[n*60:(n+1)*60]
        print(line)
        n+=1
        a = ''
        for i in range(len(line)//3):
            a+=codon_dic[line[i*3:(i+1)*3]]+'  '
        print(a)






