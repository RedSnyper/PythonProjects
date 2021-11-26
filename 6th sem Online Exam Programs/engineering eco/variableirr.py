print('Uses PW formulation, not for FW or AW. \n\n '
      'IMPORTANT: this is for individual data entry ')

t= int(input('Enter the number of years'))


irr_val = float(input('Enter the irr rate'))
irr_val = irr_val/100
cashflow= []
beginning_year = []
eoy_Irr = []
unrecovered_invt = []
t = int(t)
for i in range (0, t + 1):
        cashflow.append(float(input(f'Input the {i}th given value(neg vae ni add neg sign)')))
for i in range (0, t+1):
    if i == 0:
        beginning_year.append('-')
        eoy_Irr.append(cashflow[0])
        unrecovered_invt.append(cashflow[0])
        continue
    beg_val = round(unrecovered_invt[i-1],2)
    # eoy_value = (1+irr[0])**t * beg_val
    eoy_value = round((1+irr_val) * beg_val,2)
    beginning_year.append(beg_val)
    eoy_Irr.append(eoy_value)
    unrecovered_invt_val =round(  eoy_value + cashflow[i],2)
    unrecovered_invt.append(unrecovered_invt_val)
print('cashflow\tbeginning of year\teoy @ irr rate\t unrecovered investment')
for i in zip(cashflow, beginning_year,eoy_Irr, unrecovered_invt):
    print(i)