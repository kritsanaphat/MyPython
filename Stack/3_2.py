class Stack:

    def __init__(self,list = None):
        if list == None:
            self.item = []
        else:
            self.item=list

    def push(self,i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def Delete(self,i):
         self.item.remove(i)

    def peek(self):
        return self.item[-1]
    
    def isEmpty(self):
        return self.item == []

    def size(self):
         return len(self.item) 
 

class Stack2:

    def __init__(self,list = None):
        if list == None:
            self.item = []
        else:
            self.item=list

    def push(self,i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()
        
    def Delete(self,i):
         self.item.remove(self.item[i])
    
    def isEmpty(self):
        return self.item == []

    def size(self):
         return len(self.item) 



def ManageStack(x):
    s = Stack()
    s2 =Stack2()
    num =0
    for i in range(len(x)):
        if(x[i]=="A"):
            s.push(int(x[i+1]))
            s2.push(int(x[i+1]))
            print("Add =",x[i+1])
            i+=2
            s2.item.sort()
        elif(x[i]=="P"):
            if(s.isEmpty()==False):
                y=s.pop()
                s2.pop()
                print("Pop =",y)
            else:
                print("-1")
            i+=1
        elif(x[i]=="D"):
            j=0
        
            if(s.isEmpty()==False):
                while(j<len(s.item)):
                    if(int(x[i+1])==s2.item[j]):
                        print("Delete =",s2.item[j])
                        s.Delete(s2.item[j]) 
                        s2.Delete(j)
                    else:
                        j+=1          
            else :
                print("-1")
            
           

        elif(x[i]=="LD"):
            j=0
            if(s.isEmpty()==False):
                while(j<len(s.item)):
                    if(int(x[i+1])>s2.item[j]):
                        print("Delete =",s2.item[j],"Because",s2.item[j],"is less than",x[i+1])
                        s.Delete(s2.item[j]) 
                        s2.Delete(j) 
                    
                    else:
                        j+=1    
            else :
                print("-1")
    

        elif(x[i]=="MD"):
            j=0
            if(s.isEmpty()==False):
                while(j<len(s.item)):
                    if(int(x[i+1])<s2.item[j]):
                        print("Delete =",s2.item[j],"Because",s2.item[j],"is more than",x[i+1])
                        s.Delete(s2.item[j])
                        s2.Delete(j)
                    else:
                        j+=1                  
            else :
                print("-1")


    print("Value in Stack =",s.item)
           


x = input("Enter Input : ")
x = x.replace(","," ")
x = x.split()
ManageStack(x)
