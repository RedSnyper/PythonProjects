while True:
    dec = int(input('enter the decimal number: '))

    output = bin(dec).replace("0b","")
    print(f'The binary of decimal {dec} is {output}')
    ch = input('want to continue ? press y/Y: ')
    if ch not in ('y', 'Y'):
        break