ss = ''

IF = input('Enter input file : ')
OF = input("Enter output file : ")
print('Option1> Read a FASTA format DNA sequence file and make a reverse sequence')
print('Option2> Read a FASTA format DNA sequence file and make a reverse complement')
print('Option3> Convert GenBank format file to FASTA format file.')
Op = input('Select the option : ')
if Op == '3':
    with open(IF, 'r') as f3:
        fff = f3.readlines()
        ss += '>'+fff[0].split()[1]+' '
        ss += ' '.join(fff[1].split()[1:])+'\n'
        for k in fff:
            try:
                int(k.split()[0])
                p = ''.join(k.split()[1:])
                ss += p.upper()+'\n'
            except:
                pass
else :
    s2 = ''
    with open(IF,'r') as f1:
        ff = f1.readlines()
        ss+=ff.pop(0)
        for k in ff:
            s2+=k.strip()
        s2 = s2[::-1]
        if Op =='1':
            ss+=s2
        elif Op =='2':
            s2 = s2.replace("A","X")
            s2 = s2.replace("T","A")
            s2 = s2.replace("X","T")
            s2 = s2.replace("G","X")
            s2 = s2.replace("C","G")
            s2 = s2.replace("X","C")
            ss+=s2

with open(OF,'a') as F:
    F.write(ss)

