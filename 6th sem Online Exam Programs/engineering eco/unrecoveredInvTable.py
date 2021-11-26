print('get the value now to make uncorevered inveestment table')

print('-----IMP : see cashflow diagram and last year ma add salvage value to annual revenues -----')
#




invt = float(input('Enter the investment (0 if not given)'))
s = float(input('Enter the salvage value (0 if not given)'))
r = float(input('Enter the annual revenues'))
e = float(input('Enter the annual expenses'))
i = -i
e = -e
t= float(input('Enter the number of years'))
irr_val = float(input('Enter the irr(in decimal)'))
cashflow= []
beginning_year = []
eoy_Irr = []
unrecovered_invt = []
t = int(t)
for i in range (0, t + 1):
    if i ==0 :
        cashflow.append(invt)
    elif i==t:
        cashflow.append(s+(r-e))
    else:
        cashflow.append(r-e)

for i in range (0, t+1):
    if i == 0:
        beginning_year.append('-')
        eoy_Irr.append(invt)
        unrecovered_invt.append(invt)
        continue
    beg_val = round(unrecovered_invt[i-1],2)
    # eoy_value = (1+irr[0])**t * beg_val
    eoy_value = round((1+irr_val) * beg_val,2)
    beginning_year.append(beg_val)
    eoy_Irr.append(eoy_value)
    unrecovered_invt_val =round(  eoy_value + cashflow[i],2)
    unrecovered_invt.append(unrecovered_invt_val)

for i in zip(cashflow, beginning_year,eoy_Irr, unrecovered_invt):
    print(i)