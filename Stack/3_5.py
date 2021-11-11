class Stack :

    def __init__(self, ls = None):
        if ls == None:
            self.item = []
        else:
            self.item = ls
    def push(self,i):
        self.item.append(i)
        
    def pop(self):
        return self.item.pop()

    def __str__(self):
        s=''
        for i in range(len(self.item)):
            s+=str(self.item.pop())
        return s

def dec2bin(decnum):

    s = Stack()
    decnum = int(decnum)
    while(decnum>1):
        if(decnum%2==0):
            s.push(0)
            decnum=decnum/2        
        
        elif(decnum%2==1):
            s.push(1)
            decnum=(decnum-1)/2
            
    s.push(int(decnum))
    return s

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')
print(dec2bin(int(token)))


