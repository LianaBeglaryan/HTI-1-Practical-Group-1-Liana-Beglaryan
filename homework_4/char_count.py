def char_count(str):
    dict={}
    for i in str:
        count = str.count(i)
        dict[i] = count
    return dict
    
str = [n for n in input("enter a string: ")]
print(char_count(str))