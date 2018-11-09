def emitter(alpha,string,alpha_count):
    for i in range(len(alpha)):
        for j in range(len(string)):
            if(alpha[i]==string[j]):
                for k in range(j+1,len(string)+1):
                    vallu=True
                    word=string[j:k]
                    for l in range(len(alpha_count)):
                        if(word==alpha_count[l]):
                            vallu=False
                    if(vallu):
                        alpha_count.append(word)
    return alpha_count   
def minion_game(string):
    # Game Of vowels Vs consonant
    string=string.upper()
    stuart,kevin=0,0
    vowels,conso=[],[]
    for i in range(len(string)):
        vallu=True
        if string[i] in 'AEIOU':
            for j in range(len(vowels)):
                if(vowels[j]==string[i]):
                    vallu=False
             
            if vallu:
                vowels.append(string[i])
        else:
            for j in range(len(conso)):
                if(conso[j]==string[i]):
                    vallu=False
            
            if vallu:
                conso.append(string[i])    
    vowels_count,conso_count=vowels,conso
    vowels_count=emitter(vowels,string,vowels_count)
    conso_count=emitter(conso,string,conso_count)
    for i in range(len(vowels_count)):
        for j in range(len(string)+1):
            if(string[j:j+len(vowels_count[i])]==vowels_count[i]):
                kevin+=1
    for i in range(len(conso_count)):
        for j in range(len(string)+1):
            if(string[j:j+len(conso_count[i])]==conso_count[i]):
                stuart+=1       
    if(stuart== kevin):
        print("Draw")
    elif(stuart>kevin):
        print("Stuart",stuart)
    else:
        print("Kevin",kevin)    


    input()
if __name__ == '__main__':
    s = input("Enter a Word")
    minion_game(s)
