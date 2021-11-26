import math
assets = float(input('enter the assets value'))
salvage = float(input('enter the salvage value'))
years = int(input('Enter the years'))

print('find rate on your own if its double declining \n'
      'use (1/N) * 100 * 2\n'
      '150% declining method vae rate = 150/N'
      'if rate is not given 1 - root of N(S/I)')

dep_rate = float(input('enter the depreciation rate ( in percentage ) '))
dep_rate = dep_rate / 100

book_val_at_beg = []
db_dep = []
switch_over_dec = []
sl_dep = []
selected_dep = []
book_val_at_end = []


for i in range(0, years+1):
    if i==0:
        book_val_at_beg.append('-')
        db_dep.append('-')
        switch_over_dec.append('-')
        sl_dep.append('-')
        selected_dep.append('-')
        book_val_at_end.append(assets)
        continue
    book_val_at_beg.append(book_val_at_end[i-1])
    db_dep.append( book_val_at_beg[i] * dep_rate)
    selected_dep.append(db_dep[i])
    book_val_at_end.append(book_val_at_beg[i] - selected_dep[i])

print('adjust the table data to the table column in copy')
print('book value at beginning \t db depreciation \t book value at end')
for i in zip(book_val_at_beg, db_dep,book_val_at_end):
    print(i)

