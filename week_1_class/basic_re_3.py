import re
string = input('enter the string : ')
cc = input('enter the character : ')
pp = re.compile(cc, re.I)
ml = pp.finditer(string)
for k in ml:
    print(k.start())


