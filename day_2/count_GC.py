ss = 'acgtcgtaaa\nttttggggcccc'
ss = ss.replace('\n','').lower()
print('GC = {0}%'.format((ss.count('g')+ss.count('c'))/len(ss)*100))


