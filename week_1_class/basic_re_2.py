import re
string = input('enter a string : ')
nl = re.compile('[0-9]+').findall(string)
print(nl)
t=0
for k in nl:
    t+=int(k)
print(t/len(nl))

