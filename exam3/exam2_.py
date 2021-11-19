def maxd(i,num,max):
    if i <len(num):
        if int(num[i]) > int(max):
            return maxd(i+1,num,int(num[i]))
        else:
            return maxd(i+1,num,max)
    else:
       print("Max :",max)

x = input("Enter Input : ").split()
maxd(0,x,-10000)