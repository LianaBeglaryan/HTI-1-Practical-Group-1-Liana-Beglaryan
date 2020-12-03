l = [int(l) for l in input("tpel tiv : ")]

l_1 = l[0:len(l)+1:2]
theSum = 0   
for i in l_1:
    theSum = theSum + i
    print(theSum)

l_2 = l[1:len(l):2]
theSum_1 = 0
for i in l_2:
    theSum_1 = theSum_1 + i
    print(theSum_1) 
if theSum == theSum_1:
    print("yes")
        
else:
    print("no")  
