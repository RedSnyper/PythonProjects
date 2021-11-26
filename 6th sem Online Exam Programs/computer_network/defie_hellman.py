G = int(input("enter a random number ( G ) "))
N = int(input("enter a large prime number ( N ) "))
print('these two numbers are sent publicly and can be seen by others')
X = int(input("enter another large number(secret) chosen by(sender) one party ( X ) "))
print('calculating the public key by the sender to receiver R1 = G ^ X mod N ')
R1 = G ** X % N
print(f'the public key R1 = {R1} is sent to the receiver by the sender')
Y = int(input("enter another large number(secret) chosen by(receiver) another party ( Y ) "))
print('calculating the public key by the receiver R2 = G ^ Y mod N ')
R2 = G ** Y % N
print(f'the public key R2 = {R2} is sent to the sender by the receiver')
print('\n\nNow the secret key for both parties is calculated as ')
print('For sender.... K = R1 ^ Y mod N ')
K = R1**Y % N
print(f'the key is {K}')
print('For receiver.... K = R2 ^ X mod N')
K = R2**X % N
print(f'the key is {K}')
print('and the symmertic shared secret key for the session K is K = G^(XY) mod N')
K = G **(X*Y) % N
print(f'symmertic key is {K}')