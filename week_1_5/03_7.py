with open('sequence.protein.2.fasta','r') as f:
    ss = ''.join(f.readlines()[1:])
    while True:
        n = input('Enter position : ')
        try:
            print(ss[int(n):int(n)+3])
        except:
            if n =='XXX':
                print('Okay, I will stop.')
                break
            else:
                print('Try again.')

