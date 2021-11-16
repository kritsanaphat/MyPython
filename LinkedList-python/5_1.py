
class node:

    def __init__(self, data, next = None):
        self.data = data

        if next == None:
            self.next = None
        else :
            self.next = next
    
    def __str__(self):
        return str(self.data)

class Linkedlist:

    def __init__(self, head = None):
        
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else :
            self.head = head
            t = head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t
    
    def Size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def append(self, data):

        p = node(data)
        if self.head == None:
            self.head = p
            t = p
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t
        else :
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
            self.size += 1
            self.tail = p

l =  Linkedlist()
x = list(input("Enter Input : "))
i =0
while(i<len(x)):
    l.append(str(x[i]))
    i+=1

i=0

t1o = 0
t1c = 0
t2o = 0
t2c = 0
while(i<l.Size()):
    if(str(l.head) == '['):
        t1o+=1
        l.head = l.head.next
    if(str(l.head)== ']'):
        t1c+=1
        l.head = l.head.next
    if(str(l.head)== '('):
        t2o+=1
        l.head = l.head.next
    if(str(l.head) == ')'):
        t2c+=1
        l.head = l.head.next
    i+=1

if(t1o-t1c == 0 and t2o-t2c ==0):
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")
    


