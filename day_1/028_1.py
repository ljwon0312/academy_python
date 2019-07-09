Seq1 = 'ATGTTATAG'

change_D = {"A":"T","T":"A","G":"C","C":"G"}
reverse = ''
for k in Seq1:
    reverse+=change_D[k]

print(reverse)
