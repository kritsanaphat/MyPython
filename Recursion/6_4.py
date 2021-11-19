def sum(x,t,f,l,value):
    if(t<=int(((len(x)/2)-1)*3) or t == 1):
        y = x[f:l]
        value2 = int(perketS(y,len(y)-1))-int(perketB(y,len(y)-1))
        if(value2 < 0):
            value2 *= -1
        if(value > value2):
            value =  value2
        if(t <= (len(x)/2)-1):
            return sum(x,t+1,f+2,l+2,value)
        else:
            if(t == int((len(x)/2))):
                l = 2
                f = 0
            if(l<len(x)):
                return sum(x,t+1,f,l+2,value)
            else:
                return sum(x,t+1,f+2,l,value)

    else:
        return value

def perketS(x,t):
    if(t==-1):
        return 1
    elif(t%2==0):
        return perketS(x,t-1) * int(x[t])
    else:
        return perketS(x,t-1)   

def perketB(x,t):
    if(t==-1):
        return 0
    elif(t%2!=0):
        return perketB(x,t-1) + int(x[t])
    else:
        return perketB(x,t-1)


x = input("Enter Input : ")
x = x.replace(","," ")
x = x.split()
x =list(x)

print(sum(x,1,0,2,100000))