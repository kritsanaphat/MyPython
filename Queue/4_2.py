from collections import deque
class Queue:
    
    def __init__(self,list = None):
        '''
        if list == None:
            self.item=[]
        else:
            self.item = list
        '''
        self.item = deque()
            
    def enQueue(self,i):
        self.item.append(i)
    
    def deQueue(self):
        #return self.item.pop(0)
        return self.item.popleft()
    
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.item)
    
    def __str__(self) :
        s = self.item[0]
        i=1
        if(self.size()>0):
            while(i<self.size()):
                s +=","+" "+self.item[i]
                i+=1
        return s

q = Queue()
saveQ =[]
saveEQ = []
num = input("Enter Input : ")
num = num.replace(","," ")
num = num.split()
i=0

while(i<len(num)):
    if(num[i] == "EN"):
        q.enQueue(num[i+1])
        saveQ.append(num[i+1])
        i+=2
    elif(num[i]=="ES"):
        saveEQ.append(num[i+1])
        q.item = []
        for j in range(len(saveEQ)):
            q.enQueue(str(saveEQ[j]))

        #print("save EQ to Q",q)

        for k in range(len(saveQ)):
            q.enQueue(str(saveQ[k]))
        #print("Q",saveQ)
        #print("save EQ and Q to Q",q)
        
       
        q.item = deque(q.item)
        i+=2
        
    elif(num[i]=="D"):
        if(q.isEmpty()==False):
            #print("Before pop",q)
            print(q.deQueue())
            if len(saveEQ) != 0:
                saveEQ.pop(0)
            else:
                saveQ.pop(0)

                
        else:
            print("Empty")
        i+=1