def fact(n):
    t=1
    while n>0:
        t*=n
        n-=1
    return t

ii = int(input('enter a number : '))
print(fact(ii))

