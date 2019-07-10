def k_mer(l1,l2,n):
    if n==1:
        l2
    lt = []
    for i in l1:
        for j in l2:
            lt.append(i+j)
    k_mer(l1,lt,n-1)

l1 = ["A","T","G","C"]
l2 = ["A","T","G","C"]

k_mer(l1,l2,7)

n=0
for k in l2:
    if k == k[::-1]:
        print(k)
        n+=1
print('palindrome in 7-mer : {0}'.format(n))
