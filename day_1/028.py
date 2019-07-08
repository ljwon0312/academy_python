Seq1 = 'ATGTTATAG'

reverse = Seq1.replace("A","X")
reverse = reverse.replace("T","A")
reverse = reverse.replace("X","T")
reverse = reverse.replace("G","X")
reverse = reverse.replace("C","G")
reverse = reverse.replace("X","C")

print(reverse)
