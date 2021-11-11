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
    
    def peek(self):
        return self.item[-1]
    
    def isEmpty(self):
        return self.item == []

    def size(self):
         return len(self.item) 

    def __str__(self):
        s = ""
        for i in self.item:
            s += str(i)+' '
        if(s==""):
            return("Empty")
        return s
 
    
s = Stack()
x = input("Enter Input : ")
x = x.replace(","," ")
x = x.split()
m= 0
for i in range(len(x)):
    if(x[i]=="A"):
        s.push(x[i+1])
        print("Add =",x[i+1], "and","Size =",s.size())
        i+=2
    elif(x[i]=="P"):
        try:
            y=s.pop()
            print("Pop =",y, "and","Index =",s.size())
        except:
            print("-1")
        i+=1


print("Value in Stack =",s)
