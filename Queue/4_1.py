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
delete =[]
num = input("Enter Input : ")
num = num.replace(","," ")
num = num.split()
i=0
while(i<len(num)):
    if(num[i] == "E"):
        q.enQueue(num[i+1])
        i+=2
        print(q)
    elif(num[i]=="D"):
        if(q.isEmpty()==False):
            delete.append(q.deQueue())
            print("{}".format(delete[-1]),"<- ",end="")

            if(q.isEmpty()==False):
                print(q)
            else:
                print("Empty")
        else:
            print("Empty")
        
        i+=1

if(len(delete)!=0):
    delete2 = delete[0]
    j=1
    while(j<len(delete)):
        delete2 +=","+" "+delete[j]
        j+=1
else:
    delete2="Empty" 
if(q.isEmpty()==True):
    q.enQueue("Empty")

     

print(delete2,":",q)
    
