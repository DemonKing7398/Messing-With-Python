def minion_game(string):
    setStuart=set()
    setStuart2=set()
    setKevin=set()
    setKevin=set()
    countStuart,countKevin=0,0
    for i in range(len(string)):
        if string[i] in 'AIEOU':
            setKevin.add(string[i])
            countKevin+=1
            j=i+1
            while(j<len(string)):
                setKevin.add(string[i:j+1])
                countKevin+=1
                j+=1
        else:
            setStuart.add(string[i])
            countStuart+=1
            j=i+1
            while(j<len(string)):
                setStuart.add(string[i:j+1])
                countStuart+=1
                j+=1
    if countStuart==countKevin:
        print("Draw")
    elif countStuart>countKevin:
        print("Stuart "+str(countStuart))
    else:
        print("Kevin "+str(countKevin))


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)