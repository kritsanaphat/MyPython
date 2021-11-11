from os import path


print("*** String Rotation ***")
x,y = input("Enter 2 strings : ").split()
if(len(x)>len(y)):
    max = len(x)
else:
    max = len(y)
x = list(x)
y = list(y)
stanX = list(x)
stanY = list(y)
i = 0
while(i == 0 or (x != stanX or y != stanY)):
    
    k = x[-1]
    x.pop()
    x.insert(0,k)
    
    k2 = y[0]
    y.remove(k2)
    y.append(k2)
    if(i<5):
        print(i+1,'',end='')
        for j in range(len(x)):
            print(str(x[j]),end='')
        print(" ",end='')
        for k in range(len(y)):
            print(str(y[k]),end='')
        print(" ")
    i +=1
    num = i


if(num>6):
    print(" . . . . . ")
    print(num,"",end='')
    for j in range(len(x)):
        print(str(x[j]),end='')
    print(" ",end='')
    for k in range(len(y)):
            print(str(y[k]),end='')
    print(" ")
elif(num == 6):
    print(num,"",end='')
    for j in range(len(x)):
        print(str(x[j]),end='')
    print(" ",end='')
    for k in range(len(y)):
            print(str(y[k]),end='')
    print(" ")

print("Total of ",num,"rounds.")
