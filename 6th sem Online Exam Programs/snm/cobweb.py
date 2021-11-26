a = 12.4
b = 1.2
c = 1.0
d = 0.9
p0 = 1.0        #given
p = [p0]
supply = []
demand = []
print("WRITE FIRST 5 p Values for market stablity ")
for i in range(0,10): #to find p1,p2,p3
    p_new = round((a - c - d*p[i])/b,3)
    supply.append(round(c + d*p[i],3))
    demand.append(round(a-b*p[i],3))
    p.append(p_new)
print('plot market stability for ', p[:6])
print('price  supply  demand')
for i in zip(p, supply,demand):
    print(i)