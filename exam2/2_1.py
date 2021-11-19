class Stack:
    def __init__(self,item= None):
        if(item == None):
            self.data = []
            self.sizes = 0
        else:
            self.data = list(item)
            self.sizes = 1

    def push(self,i):
        self.data.append(str(i))
        self.sizes += 1
    
    def pop(self):
        self.data.pop()
        self.sizes -=1

    def isEmpty(self):
        return self.sizes == 0
    
    def size(self):
        return self.sizes

    def peek(self):
        if self.sizes != 0:
            return self.data[-1]
    
    def bottom(self):
        if self.sizes != 0:
            return self.data[0]
    
    def __str__(self):
        s = "Data in Stack is : "
        for i in range(self.sizes):
            s += self.data[i]+ ' '
        return s

x = input("Enter choice : ")
if(x == str(1)):
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
elif(x==str(2)):
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
elif(x==str(3)):
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())