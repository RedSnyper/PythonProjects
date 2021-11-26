print('Program to bring FW,Annual expenses and revenue to PW')
i = float(input('Enter the investment (0 if not given)'))
s = float(input('Enter the salvage value (0 if not given)'))
r = float(input('Enter the annual revenues'))
e = float(input('Enter the annual expenses'))
i = -i
e = -e
t= float(input('Enter the number of years'))
x = float(input('Enter the MARR '))
x=x/100
result = (i + (r+e)*(((1+x)**t-1)/(x*(1+x)**t)) + s*(1+x)**-t)
print(result)