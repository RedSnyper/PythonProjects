period = int(input('Enter the number of period'))
marr = float(input('Enter the percentage of MARR (in percentage)'))
marr = marr/100
net_cashflow = []
for i in range(0, period+1):
    if i==0:
        value = float(input('Enter the investment/ or use given talbe'))
        net_cashflow.append(-value)
    elif i == period:
        value = float(input('Enter annual (rev-cost) + salvage value/ or use given table'))
        net_cashflow.append(value)
    else:
        value = float(input(f'Enter the {i} value(annual value, enter revenue-cost wale value matra/or use table data'))
        net_cashflow.append(value)

present_value = []
cummulative_flow = []
for i in range(0,period+1):
    if i==0:
        present_value.append(net_cashflow[i])
        cummulative_flow.append(net_cashflow[i])
        continue
    present = net_cashflow[i]*(1+marr)**-i
    present_value.append(present)
    cummulative_flow.append(cummulative_flow[i-1]+present)

for i in zip(net_cashflow, present_value, cummulative_flow):
    print(i)