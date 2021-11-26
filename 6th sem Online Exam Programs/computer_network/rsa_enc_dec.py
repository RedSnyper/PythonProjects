
e = int(input("enter the public key (e) "))
d = int(input("enter the private key (d) "))
f = int(input('enter the plain text(f) '))
n = int(input("enter the product of prime numbers (N) "))

print('For encrpytion, Cipher = f^e % n')
encrpyt = f ** e % n
print(f'The ciphered text is : {encrpyt}')

print('for decryption text = cipher * d % n ')
decrpyt = encrpyt ** d % n
print(f'the text is {decrpyt}')
