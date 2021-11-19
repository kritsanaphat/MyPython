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
               
        

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,data):
        if data == int(self.root.data):
            print("Root")
            return 0
        else:
            t = self.root.left
            while True:
                if t.left:
                    if(int(t.data) == data):
                        if t.left or t.right:
                            print("Inner")
                            return 0
                        else:
                            print("Leaf")
                            return 0
                    t = t.left
                else:
                    t = self.root.right
                    if t.right:
                        if(int(t.data) == data):
                            if t.left or t.right:
                                print("Inner")
                                return 0
                        else:
                            print("Leaf")
                            return 0
                        t = t.right
                    else :
                        print("Not exist")
                        break


                    

                

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])