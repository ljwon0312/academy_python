import re
string = input('enter a string : ')
pp = re.compile('[a-z]+', re.I)
ll = pp.findall(string)
ll.sort()
print(ll)
