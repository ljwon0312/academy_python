with open('070.vcf','r') as fr:
    n=0
    n2=0
    count=0
    indels = ''
    for k in fr:
        if k.startswith("#"):
            pass
        else:
            n+=1
            s=k.split()
            c = s[4].split(',')
            count+=len(c)
            indel=' '.join(s[2:5])+' :'
            for a in c:
                if len(a)==len(s[3]):
                    pass
                elif len(a)>len(s[3]):
                    indel+=' insertion'
                elif len(a)<len(s[3]):
                    indel+=' delition'
            if len(indel.split())>=5:
                indels+=indel+'\n'
            if s[6] == "PASS":
                n2+=1
            if s[2].startswith('rs'):
                print('CHR : {0}    position : {1}  REF : {2}   ALT : {3}   ID : {4}'.format(s[0],s[1],s[3],s[4],s[2]))
print('\n'+indels)
print('mut : {0}    pass: {1}   total alt: {2}'.format(n,n2,count))



