def bubbleSort(num,count,count1,max):
    if count1 <= max-1:
        if count+1<=max:
            if num[count] > num[count+1]:
                temp = num[count]
                num[count] = num[count+1]
                num[count+1] = temp
                
             
        if count == max:
            count1 +=1
            count = -1
        return bubbleSort(num,count+1,count1,max)
    else:
        print(num)
        return 0


inp = [int(i) for i in input('Enter Input : ').split()]
bubbleSort(inp,0,0,len(inp)-1)