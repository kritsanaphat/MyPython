class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self) :
        return str(self.data)

class Linkedlist:

    def __init__(self, head = None):
        p = node("DUMMY")
        self.head = p
        self.size = 1
    
    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        p = node(data)
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = p
        p.previous = t
        self.size += 1

    def remove(self, item):
        found = False
        i = -1
        t =self.head
        if t.next == item:
            if(t.next.next is not None):
                k = t.next.next
                k.previous = t
            t.next = t.next.next
            self.size -= 1
            print("removed :",item,"from index : 0")
        else :
            t = self.head
            while t.next is not None :
                i+=1
                if t.next.data == item:
                    if(t.next.next is not None):
                        k = t.next.next
                        k.previous = t
                    t.next = t.next.next
                    self.size -= 1
                    print("removed :",item,"from index :",i)
                    found = True
                    break
                t = t.next
            if(found is False):
                print("Not Found!")
            
            

    def insert(self,index,data):
        if (index < self.size and index>=0):
            p = node(data)
            i=0
            t=self.head
            while(i<index):
                t = t.next
                i+=1
            if(t.next is not None):
                y = t.next
                y.previous = p
            p.next = t.next
            t.next = p
            p.previous = t 
            self.size += 1
            print("index =",index, "and data =" ,data)

        else:
            print("Data cannot be added")
           
    def addBefore(self,data):
        p = node(data)
        t = self.head
        if(t.next is not None):
            y = t.next
            t.next = p
            p.next = y
            p.previous = t
            y.previous = p
            self.size += 1
        else:
            t.next = p
            p.previous = t
            self.size +=1
    

    def __str__(self):
        s ='linked list : '
        y = self.head
        while (y is not None):
            if(y.data is not 'DUMMY'):
                if(y.next is not None):
                    s += y.data + '->'
                else:
                    s += y.data
            y = y.next
        return s
    
    def revers(self):
        s = "reverse : "
        t = self.head
        k = self.head
        while(t.next is not None):
            t = t.next
        y = t
        while(y is not k):
            if(y.previous is k):
                s += y.data
            else:
                s += y.data +'->'
            y = y.previous
        return s
            
        

def fuc(x):
    l = Linkedlist()
    i=0
    while(i<len(x)):
        if(x[i] == 'A'):
            l.append(x[i+1])
            print(l)     
            i += 2
            print(l.revers())
        elif(x[i] == 'Ab'):
            l.addBefore(x[i+1])
            print(l)
            print(l.revers())
            i += 2
        elif(x[i] == 'I'):
            l.insert(int(x[i+1]),x[i+2])
            print(l)
            print(l.revers())
            i += 3
        elif(x[i] == 'R'):
            l.remove(x[i+1])
            print(l)
            print(l.revers())
            i += 2


x = (input("Enter Input : "))
x = x.replace(","," ")
x = x.replace(":"," ")
x = x.split()

fuc(x)