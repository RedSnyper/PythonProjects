values = '0.34 0.90 0.25 0.89 0.87 0.44 0.12 .21 .46 .67 ' \
         '.83 .76 0.79 0.64 .70 .81 .94 .74 .22 .74 ' \
         '.96 .99 .77 .67 .56 .41 .52 .73 .99 0.02 ' \
         '.97 .30 .17 .82 .56 .05 .45 .31 .78 .05 ' \
         '.79 .71 .23 .19 .82 .93 .65 .37 .39 .42 ' \
         '.99 .17 .99 .46 .05 .66 .10 .42 .18 .49 ' \
         '.37 .51 .54 .01 .81 .28 .69 .34 .75 .49 ' \
         '.72 .43 .56 .97 .30 .94 .96 .58 .73 .05 ' \
         '.06 .39 .84 .24 .40 .64 .40 .19 .79 .62 ' \
         '.18 .26 .97 .88 .64 .47 .60 .11 .29 .78'

# values = '36, 91, 51, 2, 54, 6, 58, 6, 58, 2, 54, 1, 48, 97, 43, 22, 83, 25, 79, 95, 42, 57, 73, 17, 2, 42, 95, 38, 79, 29, 65, 9, 55, 97, 39, 83, 31, 77, 17, 62, 3, 49, 90, 37, 13, 17, 58, 11, 51, 92, 33, 78, 21, 66, 9, 54, 49, 90, 35, 84, 26, 74, 22, 62, 12, 90, 36, 83, 32, 75, 31, 94, 34, 87, 40, 7, 58, 5, 56, 22, 58, 77, 71, 10, 73, 23, 57, 13, 36, 89, 22, 68, 2, 44, 99, 27, 81, 26, 85, 62'
if values.__contains__(','):
    a = values.split(',')
else:
    a = values.split(' ')


a = [float(i) for i in a]


N = len(a)
print(f'--------------values in the list are : {N}')

# n = int(input('Enter the number of class(range find garna (n)): '))
n = 10
ei = int(N / n)
oi = [0] * ei
ei = [ei] * ei

for i in a:
    if 0.00 <= i <= 0.1:
        oi[0] += 1
    if 0.1 < i <= 0.2:
        oi[1] += 1
    if 0.2 < i <= 0.3:
        oi[2] += 1
    if 0.3 < i <= 0.4:
        oi[3] += 1
    if 0.4 < i <= 0.5:
        oi[4] += 1
    if 0.5 < i <= 0.6:
        oi[5] += 1
    if 0.6 < i <= 0.7:
        oi[6] += 1
    if 0.7 < i <= 0.8:
        oi[7] += 1
    if 0.8 < i <= 0.9:
        oi[8] += 1
    if 0.9 < i <= 1:
        oi[9] += 1

print(oi)

oi_ei = []
oi_ei_sqr = []
oi_ei_sqr_by_ei = []
loop = int(N/n)
for i in range(0, loop):
    val = oi[i] - ei[i]
    oi_ei.append(val)
    oi_ei_sqr.append(val**2)
    oi_ei_sqr_by_ei.append(val**2/ei[i])

print('i: ')
for i in range(0,loop):
    print(i, end=',')
print()
print('oi: ')
for i in range(0,loop):
    print(oi[i], end=', ')
print()

print('ei: ')
for i in range(0,loop):
    print(ei[i], end=', ')
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

print(f'The sum of (oi-e1)2 / ei is {sum(oi_ei_sqr_by_ei)}')