# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#input: [1,2,5,3,4,null,6]
#output: [1,null,2,null,3,null,4,null,5,null,6]

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        stack.append(root)
        
        if root is None:
            return []
        
        while stack:
            node = stack.pop()
            #first appening right of node and then left of node....that way left always                 #stays on top of the stack
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
            #assigning None to left of node.
            node.left = None
            
            #adding left of node to right of node
            if stack:
                node.right = stack[-1]
            else:
                None
                
        return root
        
