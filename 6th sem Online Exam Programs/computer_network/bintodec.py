while True:
    bin = (input('enter the binary number: '))

    output = int(bin,2)
    print(f'The binary of binary {bin} is {output}')
    ch = input('want to continue ? press y/Y: ')
    if ch not in ('y', 'Y'):
        break