from typing import NewType


class Stack:
    def __init__(self):
        self.items = []
 
    def push(self,i):
        self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            poped=self.items.pop(len(self.items)-1)
            return poped

class Queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        temp=''
        for i in range(len(self.queue)):
            if i != len(self.queue)-1:
                temp+=self.queue[i].data[0]
                temp+=', '
            else:
                temp+=self.queue[i].data[0]
        return str(temp)
    def size(self):
        return int(len(self.queue))
    def pop(self):
        if(len(self.queue)>0):
            return self.queue.pop(0)
    def front(self):
        if(len(self.queue)>0):
            return self.queue[0]   
        return None
    def second(self):
        if(len(self.queue)>1):
            return self.queue[1]   
        return None

    def push(self,arg):
        self.queue.append(arg)
    def isEmpty(self):
        if(len(self.queue)>0):
            return False
        else:
            return True

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data[0])

class BST:
    def __init__(self):
        self.root = None
    def Root(self,node):
        self.root = node
    def insert(self, data):
        if self.root != None:
            p=self.root
            while(p!=None):
                if data >= p.data:
                    if p.right == None:
                        p.right = Node(data)
                        break
                    p=p.right

                elif data < p.data:
                    if p.left == None:
                        p.left = Node(data)
                        break
                    p=p.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


def Encode(root,codeWord):
    if(root.left == None and root.right == None):
        encoded.update({root.data[0]:codeWord})
        return
    Encode(root.right,codeWord+'1')
    Encode(root.left,codeWord+'0')


inp = input('Enter Input : ')
count = {}
for i in inp:
    if i in count:
        count[i]+=1
    else:
        count.update({i:1})

#sort Dic by item
sort_count = dict(sorted(count.items(), key=lambda x: x[::-1],reverse=False))

s=Stack()
q=Queue()

#keep charecter to queue in format Node
for i in sort_count.items():
    q.push(Node(i))


q2=Queue()

while q.isEmpty() is False:
    if q2.isEmpty():
        q2.push(q.pop())
       
    else:
        
        # while q2.size()>=2 and q.front().data[1] >= q2.front().data[1] + q2.second().data[1]:
        #     q1temp = q2.pop()
        #     q2temp = q2.pop()
        #     newNode = Node(('*',q1temp.data[1]+q2temp.data[1]))
        #     newNode.left = q1temp
        #     newNode.right = q2temp
        #     q2.push(newNode)
        
        q2.push(q.pop())


while q2.isEmpty() is False:
    q1temp=q2.pop()
    q2temp=q2.pop()
    newNode = Node(('*',q1temp.data[1]+q2temp.data[1]))
    newNode.left=q1temp
    newNode.right=q2temp
    q2.push(newNode)
    if q2.size()==1:
        root = q2.pop()

T = BST()
encoded = {}
Encode(root,'')
print(encoded)
T.Root(root)
T.printTree(T.root)
encodedWord=''
for i in inp:
    encodedWord+=encoded[i]
print('Encoded! : '+encodedWord)