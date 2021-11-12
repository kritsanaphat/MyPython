from collections import deque
class Queue:
    
    def __init__(self,list = ""):
        self.item = deque(list)
            
    def enQueue(self,i):
        self.item.append(i)
    
    def deQueue(self):
        return self.item.popleft()
    
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.item)
    
    def __str__(self):
        s =''
        for ele in self.item:
            s += ele
        return s
    
class Stack:
    def __init__(self,list = None):
        if list == None:
            self.item = []
        else:
            self.item  = list

    def push(self,i):
        self.item.append(i)
    
    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

def check(q,s):
    q2 = Queue()
    numBoom = 0
    numBoomN = 0
    ReverseData = []
    ReverseDataN = []
    BoomData = []
    BoomDataN = []
    checkBoom  = 1
    itr = 0
    i = 0
    while(not s.isEmpty()): #Reverse MIR
        ReverseData.append(s.pop())  

    while(not q.isEmpty()): #not Reverse NOR
        ReverseDataN.append(q.deQueue())

    while(i<len(ReverseData)-1): #Check Boom in MIR
        if(ReverseData[i+1] == ReverseData[i]):
            checkBoom+=1
            i += 1
        else:
            i += 1
            checkBoom = 1

        if(checkBoom == 3):
            BoomData.append(ReverseData[i])
            for j in range(3):
                ReverseData.remove(BoomData[-1])
            i = 0
            checkBoom = 1
            numBoom+=1

    i=0
    y = len(ReverseData)
    while(i<y): # bring mirror to q and Reverse
        q2.enQueue(ReverseData[-1])
        ReverseData.pop(-1)
        i+=1
    
    
    i = 0
    while(i<len(ReverseDataN)-1):   #bring boom from mirror to normal
        if(ReverseDataN[i+1] == ReverseDataN[i]):
            checkBoom+=1
            i += 1
        else :
            checkBoom = 1 
            i += 1
        
        if(checkBoom == 3 and len(BoomData)>0):
            if(BoomData[0] == ReverseDataN[i]):
                itr+=1
            ReverseDataN.insert(i,BoomData[0])
            BoomData.remove(BoomData[0])
            checkBoom = 1 
            i += 2

            
    
    i = 0
    checkBoom = 1
    while(i<len(ReverseDataN)-1):   #check boom in normal
        if(ReverseDataN[i+1] == ReverseDataN[i]):
            checkBoom+=1
            i += 1
        else:
            i += 1
            checkBoom = 1
        
        if(checkBoom == 3 ):
            BoomDataN.append(ReverseDataN[i])
            for j in range(3):
                ReverseDataN.remove(BoomDataN[-1])
            i = 0
            numBoomN +=1
            checkBoom = 1

    i=0
    y = len(ReverseDataN)   #Reverse Normal for display
    while(i<y):
        q.enQueue(ReverseDataN[-1])
        ReverseDataN.pop(-1)
        i+=1
    
    numBoomN = numBoomN-itr
    print("NORMAL :")
    print(q.size())
    if(q.size() == 0):
        print("Empty")
    else :
        print(q)
    print(numBoomN , "Explosive(s) ! ! ! (NORMAL)")
    if(itr > 0):
        print("Failed Interrupted",itr,"Bomb(s)")
    print("------------MIRROR------------")
    print(": RORRIM")
    print(q2.size())
    if(q2.size() == 0):
        print("ytpmE")
    else :
        print(q2)
    print( "(RORRIM) ! ! ! (s)evisolpxE",numBoom)
      

normal,mirror = input("Enter Input (Normal, Mirror) : ").split()
q = Queue(list(normal))
s = Stack(list(mirror))
check(q,s)