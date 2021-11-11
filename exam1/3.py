print(" *** String count ***")
x = input("Enter message : ")
numUpper =0
numLowwer = 0
lower = []
uper = []
for i in range(len(x)):
    if(ord(x[i])>=97 and ord(x[i])<=122):
        numLowwer += 1
        if(x[i] not in lower):
            lower.append(x[i])
    elif(ord(x[i])>=65 and ord(x[i])<=90):
        numUpper +=1
        if(x[i] not in uper):
            uper.append(x[i])

lower = sorted(lower)
uper = sorted(uper)

print("No. of Upper case characters :",numUpper)
print("Unique Upper case characters : ",end='')
for i in range(len(uper)):
    print(uper[i],' ',end='')

print("\nNo. of Lower case Characters :",numLowwer)
print("Unique Lower case characters : ",end='')
for i in range(len(lower)):
    print(lower[i],' ',end='')