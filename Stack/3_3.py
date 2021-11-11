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

def postFixeval(st):
    i=0
    index =0
    s = Stack()
    size = len(st)
    for i in range(size):
        y=0
        if st[i] == "*":
            y = s.item[index-2]*s.item[index-1]
            s.pop()
            s.pop()
            s.push(y)
            index-=1

        elif st[i] == "-":
            y = s.item[index-2]-s.item[index-1]
            s.pop()
            s.pop()
            s.push(y)
            index-=1

        elif st[i] == "+":
            y = s.item[index-2]+s.item[index-1]
            s.pop()
            s.pop()
            s.push(y)
            index-=1

        elif st[i]== "/":
            y = s.item[index-2]/s.item[index-1]
            s.pop()
            s.pop()
            s.push(y)
            index-=1
            
        else:
            s.push(int(st[i]))
            index+=1
   

        

    return float(s.item[0])

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))