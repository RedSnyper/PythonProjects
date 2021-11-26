import random
# r = int(input("enter the radius"))
# run = int(input('number of times to run the loop'))
x = []
y = []
fxy = []
f_val = []
n_arr = []
N_arr=[]
n = 0
N= 0
for i in range(0, 10):
    #generates random number from (0,1)
    x_rand = round(random.random(),2)
    y_rand = round(random.random(),2)

    #generates random number from (a,b)
    # x_rand = random.randint(2,4)
    # y_rand = random.randint(2,16) #check boundary value

    x.append(x_rand)
    y.append(y_rand)
    f = x_rand ** 2 + y_rand ** 2 - 1   #r**2 (for radius)        #change this equation only
    f_val.append(round(f,2))
    # f = x_rand ** 2 + y_rand           #change this equation only

    # print('value of f is' , f)
    #if f > 0 for case in range(a,b)
    # if f > 0:
    # if >0.0 for case in (0,1) range
    if f > 0.0:
        fxy.append(f' f({x_rand},{y_rand}) = {f_val[i]} >0')
    else:
        fxy.append(f'f({x_rand},{y_rand}) = {f_val[i]} < 0')
        n=n+1

    n_arr.append(n)
    N = N + 1
    N_arr.append(N)

print('x\t\ty\t\t\tf(x,y)\t\t\t\tn\tN')
for i in zip(x,y,fxy,n_arr,N_arr):
    print(i)