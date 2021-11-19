
class TreeNode(object):

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None



def list_to_bst(list_nums):
    root = []
    right =[]
    left = []
    i = 0
    if ((len(list_nums)-1)%2)==0:
        while i<len(list_nums):
            if i<(len(list_nums)-1)/2:
                left.append(list_nums[i])
                
            if i == (len(list_nums)-1)/2:
                root.append(list_nums[i])
            if i>(len(list_nums)-1)/2:
                right.append(list_nums[i])
            i +=1
    else:
        while i<len(list_nums):
            if i<(len(list_nums)/2):
                left.append(list_nums[i])
                
            if i == (len(list_nums)/2):
                root.append(list_nums[i])
            if i>(len(list_nums)/2):
                right.append(list_nums[i])
            i +=1

    T = TreeNode(root[0])
    m = T
    lR = len(right)
    if lR %2 != 0:
        m.right = TreeNode(int(right[int((lR+1)/2)-1]))
        right.remove(m.right.val)
        m = m.right
    else:
        m.right = TreeNode(int(right[int((lR/2))]))
        right.remove(m.right.val)
        m = m.right
    j = len(right)
    for k in range(len(right)-1):
        m = T
        while True:
            if m.val < right[j]:
                if m.right is None:
                   m.right = TreeNode(right[k])
                   j -=1
                   break
                m = m.right 
            else:
                if m.left is None:
                    m.left = TreeNode(right[k])
                    j-=1
                    break
                m = m.left



    m = T
    lL = len(left)
    j = 0
    if lL %2 != 0:
        m.left = TreeNode(int(left[int((lL+1)/2)-1]))
        left.remove(m.left.val)
        m = m.left
    else:
        m.left = TreeNode(int(left[int((lL/2))]))
        left.remove(m.left.val)
        m = m.left
    j = len(left)-1
    while j>=0:
        m = T
        while True:
            if m.val < left[j]:
                if m.right is None:
                   m.right = TreeNode(left[j])
                   j -=1
                   break
                m = m.right 
            else:
                if m.left is None:
                    m.left = TreeNode(left[j])
                    j-=1
                    break
                m = m.left
    
   

    return T
        


def preOrder(node): 

    if not node: 

        return      

    print(node.val)

    preOrder(node.left) 

    preOrder(node.right)   



def printBST(node,level = 0):

    if node != None:

        printBST(node.right, level + 1)

        print('     ' * level, node.val)

        printBST(node.left, level + 1)



list_nums = sorted([int(item) for item in input("Enter list : ").split()])
#print(list_nums)
result = list_to_bst(list_nums)
#list_to_bst(list_nums)


print("\nList to a height balanced BST : ")

print(preOrder(result))

print("\nBST model : ")

printBST(result)