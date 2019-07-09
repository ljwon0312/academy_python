def add(a,b):
    return a+b+b
def maxx_minn(lit,x,n):
    for k in lit:
        if k<n:
            n=k
        if k>x:
            x=k
    return x,n

if __name__ =="__main__":
    print(maxx_minn([4,9,25,6,3],0,50))

