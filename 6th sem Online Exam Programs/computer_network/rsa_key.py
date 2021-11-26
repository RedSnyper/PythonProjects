
import math
p = int(input('Enter the first given prime number(p): '))
q = int(input('Enter the second given prime number(q): '))

n = p * q
print(f'n = {p} * {q}')
print(f'n = {n}')

m = (p-1) * (q-1)
print(f'n = {p}-1 * {q}-1')
print(f'n = {m}')
val_for_e = 0
for e in range(2,m):

    print(f'e = {e} ==> GCD(e,{m} == {math.gcd(e,m)})')
    if math.gcd(e,m) == 1:
        val_for_e = e
        break

print('find d such that de%m==1 , d = (1+m*i)/e')
i=0
d=0
while True:
    d_float = (1 + (m * i)) / val_for_e
    d_int = (1 + (m * i)) // val_for_e
    if d_float != d_int:
        print(f'When i={i}, d= {(1 + (m * i))}/{val_for_e} ={d_float} (No integer - discard)')

    else:
        print(f'When i={i}, d= {(1 + (m * i))}/{val_for_e} = {d_int} (Integer - check condition)')
        if d_int*val_for_e % m == 1:
            print(f'Condition satisfied( integer number for d value {d_int}')
        break
    i = i + 1
print(f'public key (n,e) are ({n},{val_for_e})')
print(f'private key (n,d) are ({n},{d_int})')

p = int(input('Enter the plain text to encrypt: '))
encrpyt = p**val_for_e % n
print(f'Encrypt: p^e % n = {encrpyt}')
print(f'cipher {encrpyt} will be sent to the receiver')
decrypt = encrpyt**d_int % n
print(f'Decryption : c^d % n = {decrypt}')
print(f'Therefore the original transmitted message is {decrypt}')
