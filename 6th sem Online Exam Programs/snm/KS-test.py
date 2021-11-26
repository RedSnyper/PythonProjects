z = input('Enter the data: (ki use comma or spaces for values)')
if z.__contains__(','):
    a = z.split(',')
else:
    a = z.split(' ')
numbers = [float(i) for i in a]

numbers = sorted(numbers)

N = len(numbers)
print(f'--------------values in the list are : {N}')



D_plus = []
D_minus = []
i_by_N = [i/len(numbers) for i in range(1, len(numbers)+1)]
i_minus1_by_N = [(i-1)/len(numbers) for i in range(1, len(numbers)+1)]

for i in range(0, N):

    D_plus_val = i_by_N[i]-numbers[i]
    D_plus.append(round(D_plus_val,2))

    D_minus_val = numbers[i] - (i_minus1_by_N[i])
    D_minus.append(round(D_minus_val,2))

#
# for i in zip(numbers, i_by_N, D_plus, D_minus):
#     print(i)
print('i')

for i in numbers:
    print(i, end=" ")
print()
print('i/N')
for i in i_by_N:
    print(i, end= " ")
print()
print('(i/n)-Ri')
for i in D_plus:
    print(i, end= " ")
print()
print('Ri-(i-1)/N')
for i in D_minus:
    print(i, end= " ")
print('\n\n\n')

print(f'D+ = Max(i/N-Ri) = {max(D_plus)}')
print(f'D- = Max(Ri - (i-1)/N) = {max(D_minus)}')
D_val =  [max(D_plus), max(D_minus)]
print(f'D = Max( D+, D-) = {max(D_val)}')
