height = [int(height)  for  height  in  input("tpel tiv : ").split()]
max_height = [max(height)]*len(height)       
product = []
for i in range(len(height)):
    product.append(max_height[0] - height[i])

for x in  product:
    sum = 0 
    sum = sum+x           
print(sum) 
 