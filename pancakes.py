def flip(user,opOp):
    hellno=''
    for i in range(opOp,opOp+int(user[1])):
        if user[0][i]=='-':
            hellno=hellno+'+'
        else:
            hellno=hellno+"-"
    if opOp==0:
        val=user[0][int(user[1]):]
        user[0]=hellno+val
    else:
        user[0]=user[0][0:opOp]+hellno+user[0][(opOp+int(user[1])):]
t=int(input())
for e in range(1,t+1):
    user=input()
    user=user.split(" ")
    flips=0
    while(1):
        if ('-' in user[0])==False:
            print("Case #{0}: {1}".format(e,flips))
            break
        if int(user[1])==(len(user[0])):
            print("Case #{0}: IMPOSSIBLE".format(e))
            break
        for j in range(len(user[0])-int(user[1])+1):
            if user[0][j] == '-':
                flip(user,j)
                flips+=1
        if '-' in user[0]:
            print("Case #{0}: IMPOSSIBLE".format(e))
            break

input()
