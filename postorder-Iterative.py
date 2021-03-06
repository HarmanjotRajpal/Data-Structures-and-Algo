class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 


def insertIntoBST(root, node):
    # if root is None create 
    if root is None:
        root = node
        return
    else:
        if root.val < node.val:
            # check if right is None then insert to the right
            if root.right is None:
                root.right = node
            else:
                insertIntoBST(root.right, node)
        else:
            # check if right is None then insert to the right
            if root.left is None:
                root.left = node
            else:
                insertIntoBST(root.left, node)
    return
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
def postorderIterative(root):
    stack = []
    stack_res= []
    
    stack.append(root)
    
    while len(stack)!= 0:
        curr = stack.pop()
        stack_res.append(curr.val)
        
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    print(stack_res[::-1])

r = Node(50) 
insertIntoBST(r,Node(30)) 
insertIntoBST(r,Node(20)) 
insertIntoBST(r,Node(40)) 
insertIntoBST(r,Node(70)) 
insertIntoBST(r,Node(60)) 
insertIntoBST(r,Node(80)) 

#inorder(r)
postorderIterative(r)
