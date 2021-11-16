
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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
            t.previous = p
            self.size = 2
    
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
        i = -1
        t =self.head
        if t.next == item:
            if(t.next.next is not None):
                k = t.next.next
                k.previous = t
            t.next = t.next.next
            self.size -= 1
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
                y.previous = p
            p.next = t.next
            t.next = p
            p.previous = t 
            self.size += 1

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

    def maxDig(self):
        t = self.head
        min = 0
        while(t is not None):
            if(t.data == 'DUMMY'):
                t = t.next
            if(len(str(t.data)) > min):
                min = len(str(t.data))
            else:
                t = t.next
        return min

    def __str__(self):
        s =''
        y = self.head
        while (y is not None):
            if(y.data != 'DUMMY'):
                if(y.next is not None):
                    s += y.data + ' '
                else:
                    s += y.data
            y = y.next
        return s

    def str2(self):
        s =''
        y = self.head
        while (y is not None):
            if(y.data != 'DUMMY'):
                if(y.next is not None):
                    s += y.data + ' -> '
                else:
                    s += y.data
            y = y.next
        return s

def RadixSort(x):
    l = Linkedlist()
    lrs = [Linkedlist(),Linkedlist(),Linkedlist(),Linkedlist(),Linkedlist(),
          Linkedlist(),Linkedlist(),Linkedlist(),Linkedlist(),Linkedlist(),] 
    for i in range(len(x)):
        l.append(x[i])
    num = -1
    for i in range(l.maxDig()+1):
        Check(l,lrs,i,x)
        x = 0
        for j in range(10):
            if(lrs[j].head.next is None ):
                x += 1
        print("------------------------------------------------------------")
        print("Round :",i+1)
        print("0 :",fordisplay(lrs,0))
        print("1 :",fordisplay(lrs,1))
        print("2 :",fordisplay(lrs,2))
        print("3 :",fordisplay(lrs,3))
        print("4 :",fordisplay(lrs,4))
        print("5 :",fordisplay(lrs,5))
        print("6 :",fordisplay(lrs,6))
        print("7 :",fordisplay(lrs,7))
        print("8 :",fordisplay(lrs,8))
        print("9 :",fordisplay(lrs,9))
        num += 1
        if(x == 9 and lrs[0].head.next is not None ):
            break
    print("------------------------------------------------------------")
    print(num,"Time(s)")
    print("Before Radix Sort :",l.str2())
    print("After  Radix Sort :",lrs[0].str2())

def NumAtDigN(num,n):
    if(num<0):
        num = num*(-1)
    num = int((num/10**n))%10
    return int(num)

def Check(l,lrs,i,x):
   
    if(i == 0):
        num1 = sorted(x,reverse=True)
        for j in range(len(num1)):
            num = 0
            for k in range(10):
                if(NumAtDigN(int(num1[j]),i) == num):
                    if(lrs[0].head.next is not None):
                        y2 = lrs[0].head.next
                        y2 = int(y2.data)
                    else:
                        y2 = 0
                    if(int(num1[j]) < y2):
                        lrs[num].append(str(num1[j]))
                    else:
                        lrs[num].addBefore(str(num1[j]))

                    break
                num += 1
        
    else:
        for m in range(10):
            y = lrs[m].head.next
            while(y is not None):
                for o in range(10):
                    if(NumAtDigN(int(y.data),i) == o and m != o):
                        if(lrs[o].head.next is not None):
                            y2 = lrs[o].head.next
                        else:
                            lrs[o].append(y.data)
                            lrs[m].remove(str(y.data))
                            break
                        if(y2 == None or int(y2.data) > int(y.data) ):
                            lrs[o].append(y.data)
                        else:
                            lrs[o].addBefore(y.data)
                    
                        lrs[m].remove(str(y.data))
                        break
                y = y.next

def fordisplay(lrs,j):
    num = []
    t = lrs[j].head.next
    
    while(t is not None):
        num.append(int(t.data))
        t = t.next
    num = sorted(num,reverse=True)
    s = ''
    i = 0
    for i in range(len(num)):
        s += str(num[i])+' '
    return s
        

                

x = input("Enter Input : ").split()
RadixSort(x)