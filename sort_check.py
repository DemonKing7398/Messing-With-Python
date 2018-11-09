def sortCheck(li):
    for i in range(len(li)-1):
        if(li[i]>li[i+1]):
            return 1
    return 0
m=input('enter all the numbers with space in bwtn \n')
m=m.split(' ')
val=sortCheck(m)
if( val==0):
    print("Not Needed")
else:
    for i in range(len(m)):
        for j in range(len(m)-1-i):
            if((m[j])>(m[j+1])):
                temp=m[j]
                m[j]=m[j+1]
                m[j+1]=temp


a=list(reversed(m))
print(a)
input()


