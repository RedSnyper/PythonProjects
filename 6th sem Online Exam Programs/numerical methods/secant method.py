
import math

print('\n\n USE "x" for all equation to solve not X and power lai use ** like : e ^ x is e ** x , 25x is 25 * x')
print('\n\nsolves e, cos, sin, tan, log(base10) haru matra ')
fn = input('Enter the equation ')

e = math.e
cos = math.cos
sin = math.sin
log = math.log10
tan = math.tan

n = int(input('Correct upto how many decimal places? '))
error = (1/2) * 10** - n
print(f'Errror (e) = 1/2 * 10^-{n} = {error}')

print('finding the root interval using tabulation method')

value = [1 if fn.__contains__('log') else -5]
f_x = []
index = 0
a = 0
b = 0
while True:
    x = value[index]
    f_x.append(eval(fn))
    if index >= 1:
        cond =  [(f_x[index-1] > 0 and f_x[index] < 0) , (f_x[index-1] < 0 and f_x[index] > 0)]
        if True in cond:
            if cond[1]:
                a = value[index-1]
                b = value[index]
            else:
                a = value[index]
                b = value[index - 1]
            break

    value.append(value[index] + 1)
    index = index + 1

print(f'x: {value}')
print(f'f(x) : {f_x}')
print(f"the root lies in between {a} and {b}")




print('#################################Secant method#################################')

x0 = a
x1 = b

x = a

fx0 = eval(fn)

x = b

fx1 = eval(fn)

x2 = (x0 * fx1 - x1 * fx0) /(fx1 - fx0)

print(f'x2 = {x2}')

x = x2
fx2 = eval (fn)
print(f'fx2 = {fx2}')

A = [a]
B = [b]
X0 = [x0]
X1 = [x1]
FX1 = [fx1]
X2 = [x2]
FX2 = [fx2]
FX0 = [fx0]
# FX0FX2 = ['yes' if fx0*fx2 < 0 else 'no']

i = 0
while True:
    if i == 0:
        i = i + 1
        continue
    # if FX0FX2[i-1] == 'yes':
    #
    #     # print('works on a ?')
    #     X1.append(X2[i - 1])
    #     X0.append(X0[i - 1])
    # else:
    #     # print('works on b')
    #     X1.append(X1[i - 1])
    #     X0.append(X2[i - 1])

    X0.append(X1[i-1])
    X1.append(X2[i-1])

    # x = round((A[i] + B[i]) / 2, n + 4)
    x = X0[i]
    FX0.append(eval(fn))
    x = X1[i]
    FX1.append(eval(fn))

    x = (X0[i] * FX1[i] - X1[i] * FX0[i]) / (FX1[i] - FX0[i])

    X2.append(x)

    FX2.append(eval(fn))

    if math.fabs(X1[i] -X0[i-1]) < error:
        root = X2[i]
        val = FX2[i]
        break
    i = i + 1


for i in zip(X0, FX0, X1, FX1, X2, FX2):
    print(i)

print(f'The root is {root} correct upto {n} decimal places and f(x) = {val}')