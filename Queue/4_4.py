
from collections import deque
Activity = {
  "0": "Eat",
  "1": "Game",
  "2": "Learn",
  "3": "Movie"
}

Location = {
  "0": "Res.",
  "1": "ClassR.",
  "2": "SuperM.",
  "3": "Home"
}
class QueueMe:
    
    def __init__(self,list = None):

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
        s +=":"+self.item[1]
        i=2
        if(self.size()>1):
            while(i<self.size()):
                s +=","+" "+self.item[i]+":"+self.item[i+1]
                i+=2
        return s

    def numTostr(self) :
        s = Activity[self.item[0]]
        s +=":"+Location[self.item[1]]
        i=2
        if(self.size()>1):
            while(i<self.size()):
                s +=","+" "+Activity[self.item[i]]+":"+Location[self.item[i+1]]
                i+=2
        return s

    
    def __init__(self,list = None):

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
        s +=":"+self.item[1]
        i=2
        if(self.size()>1):
            while(i<self.size()):
                s +=","+" "+self.item[i]+":"+self.item[i+1]
                i+=2
        return s
    
    def numTostr(self) :
        s = Activity[self.item[0]]
        s +=":"+Location[self.item[1]]
        i=2
        if(self.size()>1):
            while(i<self.size()):
                s +=","+" "+Activity[self.item[i]]+":"+Location[self.item[i+1]]
                i+=2
        return s


def CollectData(str):
    score =0
    qM = QueueMe()
    qY = QueueMe()
    i=0
    while(i<len(str)):
        qM.enQueue(str[i])
        qM.enQueue(str[i+1])
        qY.enQueue(str[i+2])
        qY.enQueue(str[i+3])
        i+=4
    
    print("My   Queue =",qM)
    print("Your Queue =",qY)
    print("My   Activity:Location =",qM.numTostr())
    print("Your Activity:Location =",qY.numTostr())

    i=0
    
    while(i<len(str)/2):
        Sameplace = False
        SameAct = False
        if(qM.item[i]==qY.item[i]):
            SameAct = True
        if(qM.item[i+1]==qY.item[i+1]):
            Sameplace = True
        if(Sameplace and SameAct):
            score+=4
        elif(Sameplace and not SameAct):
            score+=2
        elif(not Sameplace and SameAct):
            score+=1
        else:
            score-=5
        i+=2
        
    if(score>=7):
        print("Yes! You're my love! : Score is ",end="")
        print(score,"",sep=".")
    elif(score>0):
        print("Umm.. It's complicated relationship! : Score is ",end="")
        print(score,"",sep=".")
    else:
        print("No! We're just friends. : Score is ",end="")
        print(score,"",sep=".")


acti = input("Enter Input : ")
acti = acti.replace(","," ")
acti = acti.replace(":"," ") 
acti = acti.split()
CollectData(acti)