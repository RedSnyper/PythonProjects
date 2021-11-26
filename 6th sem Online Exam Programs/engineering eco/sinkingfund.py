
invt = float(input('Enter the investment'))
salvage = float(input('Enter the salavge value'))
years = int(input('Enter the life of assets'))
interest = float(input("enter the percentage ( in percentage ) if not given assume "))
int_rate = interest / 100

fixed_annual_depreciation = round((invt-salvage) * ( int_rate/((1+int_rate)**years-1)),2)
print(f'fixed annual depreciation (A) = ({invt}-{salvage}) * ( A/F, {interest}%, {years} ) = {fixed_annual_depreciation}')

bookvalue_at_beg = []
int_factor = []
net_depreciation=[]
bookvalue_at_end = []

fixed_depreciation = [fixed_annual_depreciation] * int(years+1)
for i in range(0, (years+1)):
    if i ==0 :
        bookvalue_at_beg.append( '-')
        fixed_depreciation[i] = '-'
        int_factor.append('-')
        net_depreciation.append( '-')
        bookvalue_at_end.append( invt)
        continue
    bookvalue_at_beg.append( bookvalue_at_end[i-1])
    int_factor.append(round((1+int_rate)**(i-1),4))
    net_depreciation.append( round(fixed_annual_depreciation * int_factor[i],2))
    bookvalue_at_end.append(round(bookvalue_at_beg[i]-net_depreciation[i],2))

for i in zip(bookvalue_at_beg, fixed_depreciation, int_factor, net_depreciation, bookvalue_at_end):
    print(i)