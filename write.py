fileame=input("enter the name of file")
text=input("enter into file:")
newfile=open(fileame,'w')
read=open(fileame,'r').read()
if(read=='' or read=='null'):
    newfile.write(text)
else:
    newfile.append(text)
newfile.close()
