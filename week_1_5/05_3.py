codon_dict = {'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',   'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',   'TAT':'Y', 'TAC':'Y', 'TAA':'*', 'TAG':'*',   'TGT':'C', 'TGC':'C', 'TGA':'*', 'TGG':'W',   'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',   'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',   'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',   'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',   'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M',   'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',   'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',   'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',   'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',   'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',   'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',   'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

with open('sequence.nucleotide.fasta','r') as f:
    ll = f.read().split('\n')[1:]
    sequence = ''.join(ll)
    compl = sequence.replace("A","X")
    compl = compl.replace("T","A")
    compl = compl.replace("X","T")
    compl = compl.replace("G","X")
    compl = compl.replace("C","G")
    compl = compl.replace("X","C")
    f1 = '  '.join([codon_dict[sequence[n-3:n]] for n in range(3,2332) if n%3==0])
    f2 = '  '.join([codon_dict[sequence[n-3:n]] for n in range(3,2332) if n%3==1])
    f3 = '  '.join([codon_dict[sequence[n-3:n]] for n in range(3,2332) if n%3==2])
    r1 = '  '.join([codon_dict[compl[::-1][n-3:n]] for n in range(3,2332) if n%3==0])
    r2 = '  '.join([codon_dict[compl[::-1][n-3:n]] for n in range(3,2332) if n%3==1])
    r3 = '  '.join([codon_dict[compl[::-1][n-3:n]] for n in range(3,2332) if n%3==2])


print(f1+'\n '+f2+'\n  '+f3+'\n'+sequence+'\n'+compl+'\n'+
        '%2331s\n%2330s\n%2329s' %(r1[::-1],r2[::-1],r3[::-1]))

