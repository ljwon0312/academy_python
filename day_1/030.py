Seq1= "AGTTTATAG"
for n in range(2,len(Seq1)):
    if Seq1[n-2:n] =="TT":
        print(n-2)


