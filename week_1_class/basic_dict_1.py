data = {}
while True:
    string = input('enter your name, phone number : ')
    try:
        data[string.split(',')[0]] = string.split(',')[1]
    except:
        if string == 'done':
            print(data.keys())
            break
        else:
            print('enter again')
name = input('choose one of the names : ')
print(data.get(name))

