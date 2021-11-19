class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
   
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            p = self.root
            while True:
                newData = Node(data)
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
               
    def Searchmin(self):
        t = self.root
        while(t.left is not None):
            t = t.left
        return t.data
    def Searchmax(self):
        t = self.root
        while(t.right is not None):
            t = t.right
        return t.data

    def isLesser(self,data):
        numofLesser = 0
        tL = self.root
        while(tL is not None):
            # print(int(data),int(tL.data))
            if(int(data)>=int(tL.data)):
                numofLesser +=1
                if(tL.right is not None and int(data)>int(tL.right.data)):
                    numofLesser +=1
            
            tL = tL.left
        
        tR = self.root.right
        while(tR is not None):
            # print(int(data),int(tR.data))
            if(int(data)>=int(tR.data)):
                numofLesser +=1
            if(tR.left is not None and int(data)>int(tR.left.data)):
                numofLesser +=1
            
            tR = tR.right    
        return numofLesser

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp,min = input("Enter Input : ").split('/')
inp = inp.split()
for i in range(len(inp)):
    data = int(inp[i])
    root = T.insert(data)
T.printTree(root)
print("--------------------------------------------------")
'''print("Min : ",T.Searchmin())
print("Max : ",T.Searchmax())
'''
print(T.isLesser(min))
