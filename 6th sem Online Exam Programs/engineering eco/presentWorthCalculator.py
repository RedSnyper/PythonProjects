
print('Program to calculate present worth only . Not to bring to present. To bring do individual values')
while True:
    val = float(input('Enter the value'))
    n = float(input('enter the time period to bring value to present: '))
    i_percent = float(input('Enter the percentage: '))
    i = i_percent / 100


    choice = input('Is it future(salvage) or annual or gradient: press s for salvage a for annual and g for graident ')
    if choice =='s':
        print(f'Present worth of future(salvage) is {val * (1/(1+i)**n)}')
    elif choice =='a':
        print(f'present worth of annuity is {val * ((1+i)**n-1)/(i*(1+i)**n)}')
    choice = input('is it uniform gradient series? ')
    if choice=='g':
        g = float(input('Enter the gradient'))
        print(f'present worth of gradient is {g * (((1+i)**n-i*n-1)/(i**2*(1+i)**n)) }')

    input_key = input('Press y for continuing ')
    if input_key != 'y':
        break