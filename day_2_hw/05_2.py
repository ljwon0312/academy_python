import sys

def k_mer(l1,l2,n):
    if n==1:
        return l2
    lt = []
    for j in l2:
        for i in l1:
            lt.append(j+i)
    return k_mer(l1,lt,n-1)

l1 = ["A","T","G","C"]
l2 = ["A","T","G","C"]
n = int(sys.argv[1])

print(k_mer(l1,l2,n))

