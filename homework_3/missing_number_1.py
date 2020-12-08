lst = [int(elem) for elem in input("enter a list").split()]

def missing_number(lst):
    for i in range(1,len(lst)+2):
        if i in lst:
           continue
        else:
            print(i)
            break
    return 

missing_number(lst)       










       
    
    
    


