from sympy.solvers import solve
from sympy import Symbol
x= Symbol('x', real=True)
print('Uses PW formulation, not for FW or AW')
invt = float(input('Enter the investment (0 if not given)'))
s = float(input('Enter the salvage value (0 if not given)'))
r = float(input('Enter the annual revenues'))
e = float(input('Enter the annual expenses'))
invt = -invt
e = -e
t= float(input('Enter the number of years'))




result = solve((invt + (r + e) * (((1 + x) ** t - 1) / (x * (1 + x) ** t)) + s * (1 + x) ** -t), x)
irr= []
for values in result:
    if values > 0:
        irr.append(values)
print(f'the irr rate is : {irr[0]*100}')
print('The value is ', irr[0])
print('By trial and error let i1 = (value) , i2 = (value)')
i1 = float(input('Enter the i1 in percentage'))
i1 = i1/100
x=i1
pw1 = (invt + (r + e) * (((1 + x) ** t - 1) / (x * (1 + x) ** t)) + s * (1 + x) ** -t)
print(f'Pw(i1) = {pw1}')
i2 = float(input('Enter the i2 in percentage'))
i2= i2/100
x = i2
pw2 = (invt + (r + e) * (((1 + x) ** t - 1) / (x * (1 + x) ** t)) + s * (1 + x) ** -t)
print(f'Pw(i2) = {pw2}')
print(f'Since pw() > 0 and pw() < 0, irr is in between .....')
print('Using linear interpolation: ')
i3 = i1 + (i2-i1)*((0-pw1)/(pw2-pw1))
print(f'The result is i3 {i3*100}%')

x= i3
pw3 = (invt + (r + e) * (((1 + x) ** t - 1) / (x * (1 + x) ** t)) + s * (1 + x) ** -t)
print(f'Pw(i3) = {pw3}')

pw1pw3 = (pw1 > 0 and pw2< 0 and pw3 < 0) or (pw1< 0 and pw2 > 0 and pw3 > 0)
pw2pw3 = (pw1 > 0 and pw2< 0 and pw3 > 0) or (pw1< 0 and pw2 > 0 and pw3 < 0)

if pw1pw3 :
    print('Using linear interpolation')
    i4 = i1 + (i3 - i1) * ((0 - pw1) / (pw3 - pw1))
    x = i4
    pw4 = (invt + (r + e) * (((1 + x) ** t - 1) / (x * (1 + x) ** t)) + s * (1 + x) ** -t)
    print(f'The result is i4 {i4 * 100}%')
    print(f'Pw(i4) = {pw4}')
if pw2pw3 :
    print('Using linear interpolation: ')
    i4 = i2 + (i3 - i2) * ((0 - pw2) / (pw3 - pw2))
    x = i4
    pw4 = (invt + (r + e) * (((1 + x) ** t - 1) / (x * (1 + x) ** t)) + s * (1 + x) ** -t)
    print(f'The result is i4 {i4 * 100}%')
    print(f'Pw(i4) = {pw4}')

print('USing interpolation again....')


print('get the value now to make uncorevered inveestment table')

print('-----IMP : see cashflow diagram and last year ma add salvage value to annual revenues -----')
#




# i = float(input('Enter the investment (0 if not given)'))
# s = float(input('Enter the salvage value (0 if not given)'))
# r = float(input('Enter the annual revenues'))
# e = float(input('Enter the annual expenses'))
# i = -i
# e = -e
# t= float(input('Enter the number of years'))
irr_val = round(irr[0],6)
print('The irr value is {} '.format(irr_val))
cashflow= []
beginning_year = []
eoy_Irr = []
unrecovered_invt = []
t = int(t)
for i in range (0, t + 1):
    if i ==0 :
        cashflow.append(invt)
    elif i==t:
        cashflow.append(s+(r+e))
    else:
        cashflow.append(r+e)

for i in range (0, t+1):
    if i == 0:
        beginning_year.append('-')
        eoy_Irr.append(invt)
        unrecovered_invt.append(invt)
        continue
    beg_val = round(unrecovered_invt[i-1],2)
    # eoy_value = (1+irr[0])**t * beg_val
    eoy_value = round((1+irr_val) * beg_val,2)
    beginning_year.append(beg_val)
    eoy_Irr.append(eoy_value)
    unrecovered_invt_val =round(  eoy_value + cashflow[i],2)
    unrecovered_invt.append(unrecovered_invt_val)
print('cashflow\tbeginning of year\teoy @ irr rate\t unrecovered investment')
for i in zip(cashflow, beginning_year,eoy_Irr, unrecovered_invt):
    print(i)
    #
    #
    # #
    # # # MCC Py Tutorials
    # # # 7 months ago
    # # # Hi, good question. Yes, you can use "sympify" to convert the user input into something useable here.
    # # #
    # # # Here's a short example for you, if you were to do this on CoCalc where a user types in Eq(3+x, 23).
    # # #
    # # # In:
    # # # from sympy import *
    # # # from sympy.solvers import solve
    # # # from sympy import Symbol
    # # # x = Symbol('x',real = True)
    # # #
    # # # In:
    # # # eqn = sympify(input("Type in your equation using Eq() formatting, please: "))
    # # # res = solve(eqn,x)
    # # # print(res)
    # # # Out: Type in your equation using Eq() formatting, please: Eq(3+x, 23)
    # # import math
    # #
    # # from sympy import *
    # # x = Symbol('x', real = True)
    # # x = 0
    # # prev_result = []
    # # f_a = []
    # # f_b = []
    # # f_x = []
    # # x_val = []
    # # a = 0
    # # b = 0
    # # while True:
    # #     func = math.e ** x + math.cos(25*x) - 4
    # #     x_val.append(x)
    # #     f_x.append(func)
    # #     if x == 0:
    # #         x =  x + 1
    # #         continue
    # #     else:
    # #         b_val = f_x.pop()
    # #         print(b_val)
    # #         a_val = f_x.pop()
    # #         print(a_val)
    # #         if (b_val > 0 and a_val < 0) or (b_val<0 and a_val > 0):
    # #             b = b_val
    # #             a = a_val
    # #             break
    # #     x = x + 1
    # #
    # # print(a ,b)
    # #
    # #
    # # print(func)
    #
    # # Defining Function
    # def f(x):
    #     return x ** 3 - 5 * x - 9
    #
    #
    # # Implementing Bisection Method
    # def bisection(x0, x1, e):
    #     step = 1
    #     print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    #     condition = True
    #     while condition:
    #         x2 = (x0 + x1) / 2
    #         print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
    #
    #         if f(x0) * f(x2) < 0:
    #             x1 = x2
    #         else:
    #             x0 = x2
    #
    #         step = step + 1
    #         condition = abs(f(x2)) > e
    #
    #     print('\nRequired Root is : %0.8f' % x2)
    #
    #
    # # Input Section
    # x0 = input('First Guess: ')
    # x1 = input('Second Guess: ')
    # e = input('Tolerable Error: ')
    #
    # # Converting input to float
    # x0 = float(x0)
    # x1 = float(x1)
    # e = float(e)
    #
    # # Note: You can combine above two section like this
    # # x0 = float(input('First Guess: '))
    # # x1 = float(input('Second Guess: '))
    # # e = float(input('Tolerable Error: '))
    #
    # # Checking Correctness of initial guess values and bisecting
    # if f(x0) * f(x1) > 0.0:
    #     print('Given guess values do not bracket the root.')
    #     print('Try Again with different guess values.')
    # else:
    #     bisection(x0, x1, e)
