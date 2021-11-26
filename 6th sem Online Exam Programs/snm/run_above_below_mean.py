values = '.41 .68 .89 .94 .74 .91 .55 .62 .36 .27 .19 .72 .76 .08 .54 .02 .01 .36 .16 .28 .18 .01 ' \
         '.95 .69 .18 .47 .23 .32 .82 .53 .31 .42 .73 .04 .83 .45 .13 .57 .63 .29'

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

print(run_list)
a=1
for i in range(0, len(run_list)- 1):
    if (run_list[i] == '+' and run_list[i+1]=='-') or (run_list[i] == '-' and run_list[i+1]=='+'):
        a = a + 1

print(f'Total number of runs {a}')
n1 = 0
n2 = 0
for i in run_list:
    if i == '+':
        n1 = n1 + 1
    elif i == '-':
        n2 = n2 + 1

print(f'n1+ = {n1}')
print(f'n2+ = {n2}')

mean = (2*n1*n2)/N + (1/2)
variance = ((2 * n1 * n2) * (2 * n1 * n2 - N))/(N ** 2 * (N-1))
import math
zo = (a-mean)/ math.sqrt(variance)

print(f' mean is {mean}, variance is {variance} and zo is {zo}')