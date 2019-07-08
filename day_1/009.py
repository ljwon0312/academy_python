def greet(n):
    return '\nHello, Bioinformatics'*n
while True:
    enter = input('enter the function : ')
    if enter == 'nope':
        break
    elif enter == 'greet':
        n = input('enter the number : ')
        print(greet(int(n)))



