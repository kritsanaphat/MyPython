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

    def __str__(self):
        s =''
        y = self.head
        while (y is not None):
            if(y.data is not 'DUMMY'):
                if(y.next is not None):
                    s += y.data + '->'
                else:
                    s += y.data
            y = y.next
        if(s == ''):
            s = 'Empty'
        return s
    
 
def working(x):
    foundLoop = 0
    l = Linkedlist()
    i = 0
    while(i<len(x)):
        if(x[i] == 'A'):
            l.append(x[i+1])
            print(l)
            i += 2
        elif(x[i] == 'S'):
            if(int(x[i+1])<l.size-1 and int(x[i+2])<l.size-1):    
                t = l.head
                k = l.head
                j = 0
                while(j<=int(x[i+1])):      
                    t = t.next
                    j += 1

                j1 = 0
                while(j1<=int(x[i+2])):
                    k = k.next
                    j1 += 1
                 
                if(str(k.previous) == "DUMMY" or k.next == t or k == t):
                    idx = str(x[i+1])+':'+t.data +' -> '+str(x[i+2])+':'+k.data
                    foundLoop = 1
                else:
                    idx = str(x[i+1])+':'+t.data +' -> '+str(x[i+2])+':'+k.data
                    t.next = k
                    k.previous = t
                    print("Set node.next complete!, index:value =",idx)
                    foundLoop = 0


            elif(not int(x[i+1])<l.size-1 and int(x[i+2])<l.size-1):
                print("Error! {index not in length}:",x[i+1])
            elif(int(x[i+1])<l.size-1 and not int(x[i+2])<l.size-1):
                print("index not in length, append :",x[i+2])
                l.append(x[i+2])
            elif(l.size == 1):
                print("Error! {list is empty}")
                foundLoop = 0
            i+=3
    if(foundLoop == 1):
        print("Set node.next complete!, index:value =",idx)
        print("Found Loop")
    else:
        print("No Loop")
        print(l)



x = input("Enter input : ")
x = x.replace(","," ")
x = x.replace(":"," ")
x = x.split()
working(x)
