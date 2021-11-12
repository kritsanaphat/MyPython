
from collections import deque
class Queue:
    
    def __init__(self,list = ""):
        self.item = deque(list)
            
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
        s=''
        
        for ele in self.item:
            s+=ele
        return s
    
    def printFormat(self):
        s=[]
        i=0
        for i in range(self.size()):
            s.append(self.item[i])
        return s

def encodemsg(q1,q2):
    runnum =0
    DectoAscii = []
    i=0
    while(i<q1.size()):
        y = q2.deQueue()
        DectoAscii = (ord(q1.deQueue())+int(str(y)))
        q2.enQueue(y)
        if(DectoAscii >90 and DectoAscii<97):
           DectoAscii-=26
        if(DectoAscii >122 ):
           DectoAscii-=26
        q1.enQueue(chr(DectoAscii))
        i+=1
        runnum+=1

    while(runnum%q2.size()!=0) :
        y = q2.deQueue()
        q2.enQueue(y)
        runnum+=1

    print("Encode message is :  ",end="")
    print(q1.printFormat())

def decodemsg(q1,q2):
    DectoAscii = []
    i=0
    while(i<q1.size()):
        y = q2.deQueue()
        DectoAscii = (ord(q1.deQueue())-int(str(y)))
        q2.enQueue(y)
        if(DectoAscii <=65  ):
           DectoAscii+=26
        if(DectoAscii < 97  and DectoAscii+int(y)>=97):
           DectoAscii+=26
        q1.enQueue(chr(DectoAscii))
        i+=1

    print("Decode message is :  ",end="")
    print(q1.printFormat())
    

string,number = input("Enter String and Code : " ).split(",")

string = string.replace(" ","")
q1 = Queue(string)
q2 = Queue(str(number))

encodemsg(q1, q2)
decodemsg(q1, q2)