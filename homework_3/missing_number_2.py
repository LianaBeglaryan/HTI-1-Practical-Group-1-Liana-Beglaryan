lst =  [int(elem) for elem in input("enter a list : ").split()]      

def missing_element(lst):
    lst_1=list(range(1,len(lst)+2))
    lst.sort()
    for i in range(len(lst)+1):
        if lst[i]==lst_1[i]:
            if i == len(lst)-1 and lst == lst_1[:-1]:
                print( lst_1[-1] )
                break
            else:
                continue
        elif lst[1] != lst_1[i]:    
             print( lst[i]-1 )
             break
    return

missing_element(lst)            