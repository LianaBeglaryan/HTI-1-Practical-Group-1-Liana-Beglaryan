year = int(input('print year'))
residual = year%100
if year % 100 != 0:
   print(year//100+1)
else : 
   print(year//100)