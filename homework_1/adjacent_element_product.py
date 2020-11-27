s1 = input('print a number: ') # միայն միանիշ թվերի համար
s = list(s1)
print(s , end = '  ') 
list_of_ints = [int(x) for x in s]
for i in range(len(list_of_ints)-1) :
    print( list_of_ints[i] * list_of_ints[i+1] ) # արտադրյալներից  ամենամեծը չեմ կարողացել տպել 