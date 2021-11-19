from collections import deque
from os import path
class Queue:
    def __init__(self,item=None):
        if item == None:
            self.data = deque('')
            self.size = 0
        else:
            self.data = deque(item)
            self.size = 1
    
    def enQueue(self,i):
        self.data.append(i)
        self.size +=1 
    
    def deQueue(self):
        self.data.popleft()
        self.size -=1
    
    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        if(self.size!= 0):
            s= "Queue data : "
            for i in range(self.size):
                s += str(self.data[i])+ ' '
        else:
            s= "Empty Queue"
        return s
    def isDuplicate(self):
        Duplicate = 'NO Duplicate'
        i = 0
        j = 1
        while(i<self.size):
            while(j<self.size):
                if(self.data[i] == self.data[j] and i!=j):
                    Duplicate = 'Duplicate'
                    break
                else:
                    j+=1
            i+=1
            j=i+1
        return Duplicate


x,y = input("Enter Input : ").split('/')
x = x.split()
y = y.replace(',',' ')
y = y.split()

q = Queue()
for i in range(len(x)):
    q.enQueue(x[i])
j = 0

while(j<len(y)):
    if(y[j] == 'D'):
        q.deQueue()
        j +=1
    elif(y[j]=='E'):
        q.enQueue(str(y[j+1]))
        j+=2
print(q.isDuplicate())

