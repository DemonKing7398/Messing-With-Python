import os
rawdat=list(input("Enter numbers separated wid space:").split(' '))
sum1=int(input("enter the sum u need:"))
i,v=0,0
while i<len(rawdat):
    if int(rawdat[i])>sum1:
        break
    n=sum1-int(rawdat[i])
    lowlim,uplim=0,len(rawdat)-1
    while lowlim<=uplim:
         mid=(lowlim+uplim)//2
         if(int(rawdat[mid])==n):
             print("pair is ",rawdat[i],"and",n)
             v=1
             break
         elif(int(rawdat[mid])>n):
             lowlim=mid+1
         else:
             uplim=mid-1

    i=i+1
if v==0:
    print("no pair")
k=input("SSup")
         
             
