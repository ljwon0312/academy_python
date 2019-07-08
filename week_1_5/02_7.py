codon_table = {}
while True:
    codon = input('Enter three-base codon to build : ')
    if codon == 'XXX':
        break
    aa = input('Enter amino acid : ')
    codon_table[codon] = aa
Q = input('Enter three-base codon you want to know : ')
print(codon_table[Q])


