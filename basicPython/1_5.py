
print("*** Fun with countdown ***")
x=[]
num =0
numCheck = 2
numprint = []
numprint2 = []
numprint3 = []
numofOne = 0


x = input("Enter List : ").split(" ")
for i in range(len(x)):
    x[i] = int(x[i])



for i in range(len(x)):
    if x[i] == 1:
        numofOne+=1
        numprint.insert(num , x[i])
        for j in range(i+1):
            if(x[i-(j+1)]) == numCheck:
                numprint.insert(num,numCheck)
                numCheck+=1
            else :
                numCheck =2
                num = 0
                break
        numprint2.append(numprint)
    numprint = []     

numprint3.append(numprint2)
numprint3.insert(0,numofOne)
print(numprint3)
    





