import sys

def k_mer(l1,l2,n):
    if n==1:
        return l2
    while True:
        if len(l2[0]) ==n:
            break
        j = l2.pop(0)
        for i in l1:
            l2.append(j+i)
    return k_mer(l1,l2,n-1)

l1 = ["A","T","G","C"]
l2 = ["A","T","G","C"]
n = int(sys.argv[1])

print(k_mer(l1,l2,n))

