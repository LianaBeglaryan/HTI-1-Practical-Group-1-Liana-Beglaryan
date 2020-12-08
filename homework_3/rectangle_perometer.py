x1,y1,x2,y3 = [float(elem) for elem  in  input("enter the coordinates : ").split()]
y2 = y1
x3 = x1
x4 = x2
y4 = y3
def segment_length(x1, y1, x2, y2):
    d = (x2-x1)**2 + (y2-y1)**2
    if (x2-x1)**2 == 0:
        d_root = (y2-y1)
    else: 
        d_root = (x2-x1)
    return d_root     
    
length = segment_length(x1, y1, x2, y2)
width = segment_length(x1,y1,x3,y3)
area = length * width
print(area)

