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
                        break 
                    p = p.right 
                else:
                    if p.left is None:
                        p.left = newData
                        break 
                    p = p.left 
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)  

    def rank(self,root,value):
        if root.right is None and root.left is None:
            if value >= root.data:
                return 1
            else:
                return 0
        elif root.right is None:
            if value >= root.data:
                return self.rank(root.left,value) + 1
            else:
                return self.rank(root.left,value)
        elif root.left is None:
            if value >= root.data:
                return self.rank(root.right,value) + 1
            else:
                return self.rank(root.right,value)
        else:
            if value >= root.data:
                return self.rank(root.right,value) + self.rank(root.left,value) + 1
            else:
                return self.rank(root.right,value) + self.rank(root.left,value)

T = BST()
input = input('Enter Input : ').split("/")
inp = [int(i) for i in input[0].split()]
for j in inp:
    root = T.insert(j)
T.printTree(root)
print("--------------------------------------------------")
print(f"Rank of {input[1]} : {T.rank(root,int(input[1]))}")