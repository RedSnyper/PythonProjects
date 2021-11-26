#
#
# values = '36, 91, 51, 2, 54, 6, 58, 6, 58, 2, 54, 1, 48, 97, 43, 22, 83, 25, 79, 95, 42, 57, 73, 17, 2, 42, 95, 38, 79, 29, 65, 9, 55, 97, 39,' \
#          ' 83, 31, 77, 17, 62, 3, 49, 90, 37, 13, 17, 58, 11, 51, 92, 33, 78, 21, 66, 9, 54, 49, 90, 35, 84, 26, 74, 22, 62, 12, 90, 36, 83, 32,' \
#          ' 75, 31, 94, 34, 87, 40, 7, 58, 5, 56, 22, 58, 77, 71, 10, 73, 23, 57, 13, 36, 89, 22, 68, 2, 44, 99, 27, 81, 26, 85, 62'

values = '10 63 1 64 18 8 8 1 17 21 '\
'31 40 99 20 30 51 2 27 47 58 '\
'81 3 7 9 11 22 77 87 97 9 '\
'4 16 23 38 41 53 68 71 88 92 '\
'3 37 74 7 53 59 25 13 46 16 '\
'75 2 34 58 8 24 54 26 14 92 '\
'57 73 3 23 35 9 45 17 55 15 '\
'81 22 28 4 36 18 10 37 30 72 '\
'21 83 27 43 5 19 32 11 91 95 '\
'12 41 84 29 20 6 93 31 12 56'
if values.__contains__(','):
    a = values.split(',')
else:
    a = values.split(' ')

a = [int(i) for i in a]

N = len(a)
print(f'--------------values in the list are : {N}')

# n = int(input('Enter the number of class(range find garna (n)): '))
n = 10
ei = int(N / n)

oi = [0] * ei
ei = [ei] * ei

for i in a:
    if 0 <= i <= 10:
        oi[0] += 1
    if 10 < i <= 20:
        oi[1] += 1
    if 20 < i <= 30:
        oi[2] += 1
    if 30 < i <= 40:
        oi[3] += 1
    if 40 < i <= 50:
        oi[4] += 1
    if 50 < i <= 60:
        oi[5] += 1
    if 60 < i <= 70:
        oi[6] += 1
    if 70 < i <= 80:
        oi[7] += 1
    if 80 < i <= 90:
        oi[8] += 1
    if 90 < i <= 100:
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
    print(i+1, end=',')
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