import math
import os
x=int(input("Enter the number:"))
os.system("cls")
bin=0
sum=0
compareVar=[1024,512,256,128,64,32,16,8,4,2,1]
for i in range(len(compareVar)):
    if(sum>x):
        continue
    elif(sum+compareVar[i]<=x):
        sum+=compareVar[i]
        bin=bin*10+1
    else:
        bin=bin*10+0
print(bin)
k=input()

