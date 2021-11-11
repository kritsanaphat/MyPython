
print("*** Fun with Drawing ***")
x = (int)(input("Enter input : "))
i=0
j=0
evenRow=0
RowAndCo = 5+((x-2)*4)


for i in range(RowAndCo):
    num4 = RowAndCo-i-1
    num1 = (i/2)
    num2 = RowAndCo-i
    if(i > (RowAndCo-1)/2):
        num2 = (i/2)
    num3 = (i+1)/2
    num3V2 = (i+1)/2
    num4V2 = RowAndCo-i
    
    for j in range(RowAndCo):
        if i == 0 or i== RowAndCo-1:     #TOP AND LAST
            print("#",end="")
        else:
            if (i==1 or i==RowAndCo-2):
                if(j!= 0 and j!= RowAndCo-1):
                    print(".",end="") 
                else:
                    print("#",end="")
            elif (i%2 ==0 and i!=0):
                if(i<RowAndCo/2):
                    if ( j%2!=0 and num1 >0 and j!=0):
                        print(".",end="")
                        num1-=1  
                    elif  (j%2!=0 and j>=num2 and num2<RowAndCo):
                        print(".",end="") 
                        num2+=1 
                    else:
                        print("#",end="") 
                else:
                    if ( j%2!=0 and num1 < (RowAndCo-1)/2  and j!=0):
                        print(".",end="")
                        num1+=1  
                    elif  (j%2!=0 and j >= i+1) and  num2 < (RowAndCo-1)/2:
                        print(".",end="")
                        num2+=1 
                    else:
                        print("#",end="") 
            else :
                if(i<RowAndCo/2):
                    if ( j%2!=0 and num3 >0 and j!=0):
                        print(".",end="")
                        num3-=1
                    elif  (j%2!=0 and j>=num4 and num4<RowAndCo):
                        print(".",end="") 
                        num4+=1 
                    elif(j==0 or j==RowAndCo-1):
                        print("#",end="")
                    elif(j> (num3V2*2)-1 and j< RowAndCo-num3V2*2):
                        print(".",end="")
                    else:
                        print("#",end="")
                else:
                    if ( j%2!=0 and num3 < (RowAndCo-1)/2  and j!=0):
                        print(".",end="")
                        num1+=1  
                    elif  (j%2!=0 and j >= i+1) and  num4 < (RowAndCo-1)/2:
                        print(".",end="")
                        num2+=1 
                    elif(j==0 or j==RowAndCo-1):
                        print("#",end="")
                    elif(j> (num4V2-1) and j< RowAndCo-num4V2):
                        print(".",end="")
                    else:
                        print("#",end="")  
    print("")            

