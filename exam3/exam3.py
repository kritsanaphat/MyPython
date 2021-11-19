def gcd(max,min):
    if(min is 0):
        if(max<0):
            max = max*(-1)
        return max
    else:
        return gcd(min,max%min)

x,y = input("Enter Input : ").split()
if(x>y):
    max = x
    min = y
else: 
    max = y
    min = x
if(int(max) != 0 or int(min) != 0):
    print("The gcd of",max,"and",min,"is :",gcd(int(max),int(min)))
else:
    print("Error! must be not all zero.")
