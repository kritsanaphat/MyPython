class Node:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL:
    def insert(self, root, key):
        
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 

        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
 
       
        balance = self.getBalance(root)
 
        
        #Left Left
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)
 
        # Right Right
        if balance < -1 and key >= root.right.data:
            return self.leftRotate(root)
 
        # Left Right
        if balance > 1 and key >= root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Right Left
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right

        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
 
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = AVL()
root = None

inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    print("Insert :","(",i,")")
    root = T.insert(root,i)
    T.printTree(root)
    print("--------------------------------------------------")