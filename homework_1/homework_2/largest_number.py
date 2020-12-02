num=[int(n) for n in input("tpel tiv: ")]
def largest_number(n):
    n_copy=n.copy()
    n_copy.sort()
    if n_copy[::-1] > n:
        return n_copy[::-1]
    


if largest_number(num):
   print("yes")
else:
    print("No")    
