print('...edit table on your own...')

y0 = float(input('enter the initial value of y0(y-1) '))

year = [1,2,3,4,5]
G = [15,20,25,30,35]
y= [y0]
for i in range(0, len(year)):

    print(f'For {i+1} year')
    I = round(2 + 0.1 * y[i],3)
    Y = round(45.45 + 2.27 * (I + G[i]),3)
    T = round(0.2 * Y,3)
    C = round(20 + 0.7 * (Y-T),3)
    y.append(Y)
    print(f'Investment (I) = 2 * 0.1 * {y[i]} = {I}')
    print(f'national income (y) = 45.45 + 2.27 * ({I} + {G[i]} ) = {Y}')
    print(f'Taxes (T) = 0.2 * {Y} = {T}')
    print(f'Consumption (C) = 20 + 0.7 * ({Y}-{T}) = {C}')
    print('\n\n')