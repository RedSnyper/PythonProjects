
import math
print(' USE "x" for all equation to solve not X and power lai use ** like : e ^ x is e ** x , 25x is 25 * x')
print('solves e, cos, sin, tan, log(base10) haru matra ')
fn = input('Enter the function: ')

e = math.e
cos = math.cos
sin = math.sin
log = math.log10
tan = math.tan

n = int(input('Correct upto how many decimal places? '))
error = (1/2) * 10** - n
print(f'Errror (e) = 1/2 * 10^-{n} = {error}')

print('finding the root interval using tabulation method')

value = [0]
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

print('for steps ')
steps = (log(abs(b-a)) - log(error))/log(2)
steps = math.ceil(steps)
print('required no of steps is : ', steps)

print('==============Bisection method==================')
no_of_steps = 0
A = [a]
B = [b]
x = (a+b)/2
X = [x]
if eval(fn) > 0:
    f_x = ['+']
else:
    f_x = ['-']


for i in range(1, steps):
    if f_x[i-1] == '+':
        # print('works on a ?')
        A.append(A[i-1])
        B.append(X[i-1])
    else:
        # print('works on b')
        B.append(B[i-1])
        A.append(X[i-1])
    x = round((A[i] + B[i])/2, n + 4)
    X.append(x)
    res = eval(fn)
    if res > 0:
        f_x.append('+')
    else:
        f_x.append('-')
    if i == steps-1:
        last_val = res



for i in zip(A, B, X, f_x):
    print(i)
print('The last value of f(n) is ', last_val)


