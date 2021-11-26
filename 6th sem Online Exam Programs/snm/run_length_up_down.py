values='0.30 .48 .36 .01 .54 .34 .96 .06 .61 .85 ' \
       '.48 .86 .14 .86 .89 .37 .49 .60 .04 .83 ' \
       '.42 .83 .37 .21 .90 .89 .91 .79 .57 .99 ' \
       '.95 .27 .41 .81 .96 .31 .09 .06 .23 .77 ' \
       '.73 .47 .13 .55 .11 .75 .36 .25 .23 .72 ' \
       '.60 .84 .70 .30 .26 .38 .09 .19 .73 .44'

if values.__contains__(','):
    values = values.split(',')
else:
    values = values.split(' ')
values = [float(i) for i in values]
N = len(values)
print(f'--------------values in the list are : {len(values)}')
mean  = (0.0 + 0.99) / 2
run_list = []

for i in range(0, len(values)-1):
    if values[i] < values[i+1]:
        run_list.append('+')
    else:
        run_list.append('-')
print(run_list)

length_of_run = []
plus_counter = 0
minus_counter =0
show_plus = False
show_minus = False
# run_list.append('E0F') #just for length correciton
print('-------------------')
print('length of runs')
for i in range(0, len(run_list)):
    if run_list[i] == '-':
        minus_counter += 1
        show_minus= True
        if show_plus:
            length_of_run.append(plus_counter)
            plus_counter = 0
            show_plus = False
    elif run_list[i] == '+':
        plus_counter += 1
        show_plus = True
        if show_minus:
            length_of_run.append(minus_counter)
            minus_counter = 0
            show_minus = False
    if i == len(run_list)-1:
        if minus_counter == 1:
            length_of_run.append(minus_counter)
        else :
            length_of_run.append(plus_counter)

print(length_of_run)
o1 = 0
o2 = 0
o3_above = 0

for value in length_of_run:
    if value == 1:
        o1 +=1
    elif value == 2:
        o2 +=1
    else:
        o3_above += 1

print(f'o1 = {o1} \no2 = {o2} \no3+ = {o3_above} \n')
O = [o1,o2,o3_above]
E = []
from math import  factorial
for i in range(1,4):
    val = round((2/factorial(i+3)) * (N*(i**2 + 3 * i + 1) - (i**3 + 3*i**2-i-4)),3)
    E.append(round(val,3))
print(f'E(Y1) = {E[0]}\nE(Y2) = {E[1]}\nE(Y3) = {E[2]}\n')


oi_ei = []
oi_ei_sqr = []
oi_ei_sqr_by_ei = []
loop = 3
for i in range(0, loop):
    val = O[i] - E[i]
    oi_ei.append(round(val,3))
    oi_ei_sqr.append(round(val**2,3))
    oi_ei_sqr_by_ei.append(round(val**2/E[i],3))

print('i: ')
for i in range(0,loop):
    print(i+1, end=',')
print()
print('oi: ')
for i in range(0,loop):
    print(O[i], end=', ')
print()

print('ei: ')
for i in range(0,loop):
    print(E[i], end=', ')
print()

print('oi - ei: ')
for i in range(0,loop):
    print(oi_ei[i], end=', ')
print()

print('(oi - e1)2: ')
for i in range(0,loop):
    print(oi_ei_sqr[i], end=', ')
print()

print('(oi-e1 )2 / ei: ')
for i in range(0,loop):
    print(oi_ei_sqr_by_ei[i], end=', ')
print()

print(f'The sum of (oi-e1)2 / ei is {round(sum(oi_ei_sqr_by_ei),3)}')


print('Chi square ma degree of freedom for above below mean  = 3 ( L ), run up and down lai chai 2 (L-1 ) L = i1,i2,i3')