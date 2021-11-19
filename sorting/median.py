l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    median = 0
    l=list(map(int, l))
    ls = []
   
 
    for i in range(len(l)): 
        ls = []
        for k in range(i+1):
            ls.append(l[k])
        
        j = 0
        while j<len(ls)-1:
            if ls[j]>ls[j+1]:
                temp = ls[j+1]
                ls[j+1] = ls[j]
                ls[j] = temp
                j = 0
            else:
                j +=1
                
        ls2 = ls[0:i+1] 
           
        print("list =",l[0:i+1],": median = ",end='')
        if len(ls2)%2==0:
            
            median =(ls2[int(len(ls2)/2)]+ls2[int(len(ls2)/2)-1])/2
        else:
            
            median = ls2[int(len(ls2)/2)]
        print(float(median))