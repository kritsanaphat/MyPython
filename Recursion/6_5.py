def fuc(n,k):
    if(n!=0 or k!=1):
        if(n>0):
            printF("_",n-1)
            printF("#",k)
            print()
            return fuc(n-1,k+1)
        elif(n<0):
            printF("_",k-1)
            printF("#",-n)
            print()
            return fuc(n+1,k+1)
    else:
        print("Not Draw!")
    
def printF(x,y):
    if(y>0):
        print(x,end='')
        return printF(x,y-1)
    else:
        return 0

fuc(int(input("Enter Input : ")),1)