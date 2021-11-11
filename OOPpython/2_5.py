def bon(w):
    alphabets =[]
    num = 97
    while(num<=122):
        alphabets.append(chr(num))
        num+=1
    i=0
    j=0
    test =0
    val =0
    while(i<=25):
        for j in range(len(w)):
            if w[j] == alphabets[i]:
                test+=1
                if(test==2):
                    val=(i+1)*4
                    break
            else:
                test=0
        i+=1
    return val

secretCode = input("Enter secret code : ")
print(bon(secretCode))

