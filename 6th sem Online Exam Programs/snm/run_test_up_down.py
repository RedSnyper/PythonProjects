values = '.41 .68 .89 .94 .74 .91 .55 .62 .36 .27 .19 .72 .76 .08 .54 .02 .01 .36 .16 .28 .18 .01 ' \
         '.95 .69 .18 .47 .23 .32 .82 .53 .31 .42 .73 .04 .83 .45 .13 .57 .63 .29'

if values.__contains__(','):
    values = values.split(',')
else:
    values = values.split(' ')
values = [float(i) for i in values]
print(f'--------------values in the list are : {len(values)}')

run_list = []
for i in range(0, len(values)-1):
    if values[i] < values[i+1]:
        run_list.append('+')
    else:
        run_list.append('-')
print(run_list)

a=1
for i in range(0, len(run_list)- 1):
    if (run_list[i] == '+' and run_list[i+1]=='-') or (run_list[i] == '-' and run_list[i+1]=='+'):
        a = a + 1

print(f'Total number of runs in the sequence {a}')

a = int ( input('total no of changes in runs: {mathi ko a value nai but check } '))

mean = round((2 * len(values) -1 )/3,2)
variance = round((16 * len(values) - 29)/90,2)

import math
std_nrml_dist = round((a - mean) / math.sqrt(variance),3)
print(f' mean is {mean}, variance is {variance} and z0 is {std_nrml_dist}')