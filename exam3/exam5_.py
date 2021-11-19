


class Node:
    def __init__(self,data):
        self.data  = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            t = self.root
            while True:
                if int(t.data) <= data:
                    if t.right is None:
                        t.right = Node(data)
                        break

                    t = t.right
                else:
                    if t.left is None:
                        t.left = Node(data)
                        break

                    t = t.left
        return self.root
    def Levelorder(self):
        level = []
        level.append(self.root)
        while level:
            temp = []
            for t in level:
                print(t.data,'',end='')
                if t.left:
                    temp.append(t.left)
                if t.right:
                    temp.append(t.right)
            level = temp
                 
    def preorder(self,root):
        if root:
            print(root.data,'',end='')
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,'',end='')
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,'',end='')
            

print(" *** Binary Search Tree ***")
T = BST()
x = input('Enter Input : ').split()
for i in range(len(x)):
    root = T.insert(int(x[i]))
print()
print(" --- Tree traversal ---")
print("Level order : ",end='')
T.Levelorder()
print()
print("Preorder : ",end='')
T.preorder(root)
print()
print("Inorder : ",end='')
T.inorder(root)
print()
print("Postorder : ",end='')
T.postorder(root)
print()
