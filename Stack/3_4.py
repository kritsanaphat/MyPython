class Stack():

    def __init__(self, ls = None):
        if ls == None:
            self.item = []
        else:
            self.item = ls
    def push(self,i):
        self.item.append(i)

        
    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

class StackCalc():
    def __init__(self):
        self.error = None

    def getValue(self):
        return int(self.value)

    def isInt(self):
        self.isInt=True
        return self.isInt

    def run(self,st):
        i=0
        index =0
        size = len(st)
        s = Stack()
        for i in range(size):
            y=0
            if st[i] == "*":
                y = s.item[index-1]*s.item[index-2]
                s.pop()
                s.pop()
                s.push(y)
                index-=1

            elif st[i] == "-":
                y = s.item[index-1]-s.item[index-2]
                s.pop()
                s.pop()
                s.push(y)
                index-=1

            elif st[i] == "+":
                y = s.item[index-1]+s.item[index-2]
                s.pop()
                s.pop()
                s.push(y)
                index-=1

            elif st[i]== "/":
                y = s.item[index-1]/s.item[index-2]
                s.pop()
                s.pop()
                s.push(y)
                index-=1
            elif st[i]== "DUP":
                s.push(int(s.item[index-1]))
                index+=1
            elif st[i]== "POP":
                s.pop()
                index-=1
            elif st[i] =="PSH:":
                s.push(st[i])   
                index+=1
            else:
                self.error = st[i]     
                s.push(int(st[i]))
                index+=1
           


        if (s.isEmpty()==True):
            s.push(0)
            self.value = s.item[len(s.item)-1]    
        else:
            self.value = s.item[len(s.item)-1]    
              
           
            
print("* Stack Calculator *")
arg = list(input("Enter arguments : ").split())

machine = StackCalc()
try:
    machine.run(arg)
    print(machine.getValue())

except:
    print("Invalid instruction:",machine.error)
    