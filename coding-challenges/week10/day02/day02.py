#Q-1 ) Maximum Depth of Binary Tree:

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
          
# Q-2 ) Invert Binary Tree  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left,root.right= (
            self.invertTree(root.right),self.invertTree(root.left))
        return root        
      
# Q-3)Count Complete Tree Nodes 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root==None:
            return 0

        left=root
        right=root
        h_l=0
        h_r=0
        while left != None:
            h_l +=1
            left=left.left
        while right !=None:
            h_r+=1
            right = right.right
        if h_l==h_r: 
            return(2**h_l)-1
        else:
            return 1+ self.countNodes(root.left) + self.countNodes(root.right)
      
