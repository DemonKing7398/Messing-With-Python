ip=input("enter the ip address :")
ip=ip+'.'
c=0
for i in range(len(ip)-1):
    if(ip[i+1]=='.'):
        c=c+1
print(c)
k=input()
