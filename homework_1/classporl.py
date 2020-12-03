n=[int(n) for n in input("tpel tiv: ").split()]

for i in range(0,len(n)-1):
    if n[i]>n[i+1]:
        n[i],n[i+1]=n[i+1],n[i]
        print(n)

    elif n[i]<n[i+1]:
        print("everything id okay")    
