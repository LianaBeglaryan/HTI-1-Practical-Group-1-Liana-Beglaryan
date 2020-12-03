def my_filter(lst,func):
    filtered_list=[]
    for i in lst:
        if func(i):
            filtered_lst.append(i)
    return filtered_list
print(my_filter([1,2,3,4,5,6,7,8,9,1,0,11],lambda x: x%2==0))            