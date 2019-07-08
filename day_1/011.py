def fact(n):
    t=1
    while n>0:
        t*=n
        n-=1
    return t

print(fact(5))

