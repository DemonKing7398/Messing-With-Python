n=int(input("enter number:"))
for i in range(n,0,-1):
    a=i
    t=0
    while(a>9):
        if(a%10<(a/10)%10):
            t=1
            break
        a=a/10
    if(t==0):
        print(i)
        break
    else:
        continue
    

    
        

