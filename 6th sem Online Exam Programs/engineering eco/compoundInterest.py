while True:
    i_percent = float(input('Enter the percentage: '))
    i = i_percent / 100
    n = float(input('enter the number of years: '))
    g_percent = float(input('enter the rate of change ( g, use 0 if not needed ) : '))
    g = g_percent / 100
    print('Single Payment')
    print(f'(F/P,{i_percent}% ,{n}) = {(1+i)**n}')
    print(f'(P/F,{i_percent}% ,{n}) = {(1/(1+i)**n)}')
    print('Equal payment series')
    print(f'(F/A,{i_percent}% ,{n}) = {((1+i)**n-1)/i}')
    print(f'(A/F,{i_percent}% ,{n}) = {i/((1+i)**n-1)}')
    print(f'(P/A,{i_percent}% ,{n}) = {((1+i)**n-1)/(i*(1+i)**n)}')
    print(f'(A/P,{i_percent}% ,{n}) = {(i*(1+i)**n)/((1+i)**n-1)}')
    print(f'(F/AD(annuity due),{i_percent}% ,{n}) = {(((1+i)**n-1)/i)*(1+i)}')
    print(f'(P/AD(annuity due),{i_percent}% ,{n}) = {(((1+i)**n-1)/(i*(1+i)**n))*(1+i)}')
    print('Linear gradient series')
    print(f'(P/G,{i_percent}% ,{n}) = {(((1+i)**n-i*n-1)/(i**2*(1+i)**n))}')
    print(f'(F/G,{i_percent}% ,{n}) = {(((1+i)**n-i*n-1)/(i**2))}')
    print(f'(A/G,{i_percent}% ,{n}) = {(((1+i)**n-i*n-1)/(i*((1+i)**n-1)))}')

    if g!=0:
        print('Geometric gradient series')

        if i!=g:
            print(f'(P/A1, {g_percent}, {i_percent}% ,{n}) = {((1-(1+g)**n*(1+i)**-n)/(i-g))}')
            print(f'(F/A1, {g_percent}, {i_percent}% ,{n}) = {((1-(1+g)**n*(1+i)**-n)/(i-g))*(1+i)**n}')
        else:
            print(f'(P/A1, {g_percent}, {i_percent}% ,{n}) = {(n/(1+i))}')
            print(f'(F/A1,, {g_percent} ,{i_percent}% ,{n}) = {((n*(1+i)**n)/(1+i))}')
    quit_char = input('Do you wanna quit? ')
    if quit_char in ("y","Y"):
        quit(1)