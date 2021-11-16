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
        s =''
        y = self.head
        while (y is not None):
            if(y.data is not 'DUMMY'):
                s += y.data + ' '
            y = y.next
        return s

    def revers(self):
        s = ''
        t = self.head
        k = self.head
        while(t.next is not None):
            t = t.next
        y = t
        while(y is not k):
            if(y.previous is k):
                s += y.data
            else:
                s += y.data +' '
            y = y.previous
        return s
            

def Merge(l1,l2):
    print("L1    :" , l1)
    print("L2    :" , l2)
    k = str(l1) + str(l2.revers())
    print("Merge :",k)


l1 = Linkedlist()
l2 = Linkedlist()
x1 , x2 = input("Enter Input (L1,L2) : ").split()
x1 = x1.split('->')
x2 = x2.split('->')

i=0
while(i<len(x1)):
    l1.append(x1[i])
    i += 1
     
i = 0
while(i<len(x2)):
    l2.append(x2[i])
    i += 1 

Merge(l1,l2)