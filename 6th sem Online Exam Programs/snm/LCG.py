print('for periodic cylce of random number, m = even , '
      'a = odd'
      'c = odd'
      'seed value = even? \n\n')

z0 = int(input('Enter the seed value (z0): '))
a = int(input('Enter the multiplicative factor (a): '))
c = int(input('Enter the incrementing factor (c): '))
m = int(input('Enter the modulus value (m): '))

n = int(input('Sequence to generate random number for? (n): '))
i_val = []
z_val = [z0]
u_val = []
u_val_digit = []
for i in range(0, n):
    if i==0:
        i_val.append(i)
        u_val.append(f'{z_val[i]}/ {m}')
        u_val_digit.append(round(z_val[i]/m,3))
        continue

    z_val.append((a * z_val[i-1] +c) % m)
    i_val.append(i)
    u_val.append(f'{z_val[i]}/{m}')
    u_val_digit.append(z_val[i] / m)
print('i \t zi \t ui \t ui(in digits)')
for i in zip(i_val, z_val, u_val, u_val_digit):
    print(i)


print(u_val_digit)



