values = '.12 .01 .23 .28 .89 .31 .64 .28 .03 .93 ' \
         '.99 .15 .33 .35 .91 .41 .60 .27 .75 .88 ' \
         '.68 .49 .05 .05 .95 .58 .15 .36 .69 .87'

if values.__contains__(','):
    values = values.split(',')
else:
    values = values.split(' ')
values = [float(i) for i in values]
N = len(values)
print(f'--------------values in the list are : {len(values)}')
mean  = (0.0 + 0.99) / 2
run_list = []

for i in values:
    if i < mean :
        run_list.append('-')
    else:
        run_list.append('+')


i = int(input('the first starting number in the test sequence? '))
m = int(input('gap in sequence between (ith+1 - ith) no, m?: '))

print('To find M, where M is the largest integer is gven by i + (M+1)m <=N')

import math
M = math.floor(round(((N-i)/m)-1,3))
print(f'\nM is, {M} \n')

print('cap <Pim> is given by zo = cap<Pim> / std cap<Pim>')
print('these two are found isng scmidt and taylor series')

display_string = ''
display_value = ''
output = 0
for k in range(0,M+1):
    display_string += f'R{i + k * m}*R{i + (k + 1) * m}+'
    display_value += f'{values[(i + k * m)-1]}*{values[(i + (k + 1) * m)-1]}+'

display_string = display_string.rstrip('+')
display_value = display_value.rstrip('+')
print(display_string)

print(f'^P{i}{M+1} = 1/{M} * [{display_string}] - 0.25')
for k in range(0,M+1):
    output += (values[(i+k*m)-1] * values[(i +(k+1)*m)-1])

print(f'^P{i}{m} = 1/{M+1} * [{display_value}] - 0.25')
result = 1/(M+1) * output -0.25
print(f'^P{i}{m} = {result}')

num = 13 * M + 7
denom  = 12 * (M + 1)
std_dev = round(math.sqrt(num)/denom,4)
print(f'sigma P{i}{m} = sqrt(13*{M} + 7)/12({M}+1) = {std_dev}')

print(f'z0 = ^p{i}{m} / sigma ^P{i}{m} = {result/std_dev}')