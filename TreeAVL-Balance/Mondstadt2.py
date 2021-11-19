class Node:
    def __init__(self, data,tag):
        self.data = data
        self.tag = tag
        self.left = None
        self.right = None
    
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
   
    def insert(self, data,tag):
        if self.root is None:
            self.root = Node(data,tag)
        else:
            p = self.root
            while True:
                newData = Node(data,tag)
                if data > p.data:  
                    if p.right is None:
                        p.right = newData
                        break #done for insert(while TRUE)
                    p = p.right  #back to check again
                else:
                    if p.left is None:
                        p.left = newData
                        break #done for insert(while TRUE)
                    p = p.left #back to check again
        return self.root
    
    def compareT(self,tag1,tag2):
        pow1 = 0
        pow2 = 0
        t1 = self.root
        while t1:
            if t1.tag == tag1:
                pow1 = t1.data
                break
            else:    
                t1=t1.left
        t2 = self.root
        while t2:
            if t2.tag is tag2:
               pow2 = t2.data
               break
            else:
                t2 = t2.left
        if pow1>pow2:
            print(tag1,'>',tag2,sep='')
        elif pow1==pow2:
            print(tag1,'=',tag2,sep='')
        else:
            print(tag1,"<",tag2,sep='')
        
    def sumT(self,root,vale=0):
        if root:
            vale+=root.data
            self.sumT(root.left)
        return vale

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp,cp = input("Enter Input").split('/')
inp = inp.split()
cp = cp.replace(","," ")
cp = cp.split()
pow2 = []
for i in range(len(inp)-1,-1,-1):
    power = int(inp[i])
    for j in range(1,3):
        N = (2*i)+j-(len(inp)-len(pow2))
        if N<len(pow2):
            power+=pow2[N]
        
    pow2.insert(0,power)
    
for i in range(len(pow2)):
    root = T.insert(pow2[i],int(i))
    
print(T.sumT(root))
for i in range(0,len(cp),2):
    T.compareT(int(cp[i]),int(cp[i+1]))