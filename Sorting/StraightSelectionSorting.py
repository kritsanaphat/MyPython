def StraightSelectionSort(num,count,count1,MaxValue):
    if count1 <= len(num)-1:
        if num[count]>MaxValue:
            MaxValue = num[count]

        if count == len(num)-1-count1:
            
            temp = num[len(num)-1-count1]
            k = Index(num,MaxValue,0)
            if temp != MaxValue:
                print("swap",temp,"<->",MaxValue,": ",end='')
            num[len(num)-1-count1] = MaxValue
            num[k] = temp
            if temp!= MaxValue:
                print(num)
            MaxValue = -1000
            count1 +=1
            count = -1
            
        return StraightSelectionSort(num,count+1,count1,MaxValue)
    else:
        print(num)
        return 0
def Index(num,temp,index):
    if index <= len(num)-1:
        if num[index] == temp:
            return index
        else:
            return Index(num,temp,index+1)
    else:
        return 0


inp = [int(i) for i in input('Enter Input : ').split()]
StraightSelectionSort(inp,0,0,-1000)