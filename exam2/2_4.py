from typing import Text


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) :
        return str(self.data)

class Linkedlist:

    def __init__(self, list = None):
        p = node("DUMMY")
        self.head = p
        self.size = 1
        if(list is not None):
            p2 = node(list)
            t = self.head
            t.next = p2
            self.size = 2
    
    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        p = node(data)
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = p
        self.size += 1
    
    def remove(self, item):
        i = -1
        t =self.head
        if t.next == item:
            if(t.next.next is not None):
                k = t.next.next
            t.next = t.next.next
            self.size -= 1
        else :
            t = self.head
            while t.next is not None :
                i+=1
                if t.next.data == item:
                    if(t.next.next is not None):
                        k = t.next.next
                    t.next = t.next.next
                    self.size -= 1
                    break
                t = t.next

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
            p.next = t.next
            t.next = p
            self.size += 1

    def addBefore(self,data):
        p = node(data)
        t = self.head
        if(t.next is not None):
            y = t.next
            t.next = p
            p.next = y       
            self.size += 1
        else:
            t.next = p
            self.size +=1
    def __str__(self):
        s = ''
        t = self.head
        while(t != None):
            if(t.data != "DUMMY"):
                if(t.next != None):
                    s += str(t.data)+' <- '
                else:
                    s += str(t.data)
            t = t.next
        return s
    
    def sort(self):
        index = 0
        t = self.head
        while(t != None):
            if(t.data == '0'):
                break
            else:
                index += 1
                t = t.next
        text = t.data
        self.remove(t.data)
        self.addBefore(text)
        i = 1
        while(index<self.size and t.next!=None):
            t = t.next
            text = t.data
            self.remove(t.data)
            self.insert(i,text)
            i += 1
        



    
l = Linkedlist()
print(" *** Re order ***")
x = input("Enter Input : ").split()
for i in range(len(x)):
    l.append(x[i])
print("Before :",l)
l.sort()
print("After :",l)

  
