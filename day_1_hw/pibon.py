import sys
n = int(sys.argv[1])
ll = [1,1]
while n>0:
    ll.append(ll[-1]+ll[-2])
    n-=1
print(ll)


