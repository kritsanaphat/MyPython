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
            if(int(data)>=int(tL.data)):
                numofLesser +=1
                if(tL.right is not None and int(data)>int(tL.right.data)):
                    numofLesser +=1
            
            tL = tL.left
        
        tR = self.root.right
        while(tR is not None):
            if(int(data)>=int(tR.data)):
                numofLesser +=1
            if(tR.left is not None and int(data)>int(tR.left.data)):
                numofLesser +=1
            
            tR = tR.right    
        return numofLesser
    
    def preoder(self,root):
        if root is not None:
                print(root.data,"",end='')
                self.preoder(root.left)
                self.preoder(root.right)


    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,"",end='')
            self.inorder(root.right)
    
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,"",end='')
    
    def breadth(self,root):
        t =self.root
        if t:
            print(t.data,"",end='')
        if t.left:
            print(t.left,"",end='')
        if t.right:
            print(t.right,"",end='')
        tR = self.root.right
        tL = self.root.left
        tRR = None
        tLR = None
        stage = 0
        while tR or tL:
            if tL:
                if tL.left:
                    print(tL.left.data,"",end='')
                if tL.right:
                    print(tL.right.data,"",end='')
                if tLR:
                    if tLR.left:
                        print(tLR.left.data,"",end='')
                    if tLR.right:
                        print(tLR.right.data,"",end='')
            tLR = tL.right
            tL = tL.left
            
            if tR:
                if tR.left:
                    print(tR.left.data,"",end='')
                if tR.right:
                    print(tR.right.data,"",end='')
                if tRR:
                    if tRR.left:
                        print(tRR.left.data,"",end='')
                    if tRR.right:
                        print(tRR.right.data,"",end='')
            tRR = tR.right
            tR = tR.left
        

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
#T.printTree(root)

print("Preorder : ",end='')
T.preoder(root)
print()
print("Inorder : ",end='')
T.inorder(root)
print()
print("Postorder : ",end='')
T.postorder(root)
print()
print("Breadth : ",end='')
T.breadth(root)
