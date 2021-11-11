print(" *** Divisible number ***")
num = int(input("Enter a positive number : "))
f = 0 
outp = []
if(num>0):
    for i in range(1,num+1):
        if(num%i == 0):
            outp.append(int(i))
    print("Output ==> ",end='')
    for i in range(len(outp)):
        print(outp[i],"",end='')

    print("\nTotal ==>",len(outp))
else:
    print(num,"is OUT of range !!!")