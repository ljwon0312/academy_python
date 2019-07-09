with open('059.fasta','r') as f:
    f.readline()
    seq = f.read().replace('\n','')
    print("A",seq.count("A"),"T",seq.count("T"),"G",seq.count("G"),"C",seq.count("C"))




