#Q-1 ) Print vertical order traversal, or Top view of a binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root,x,y):
            if not root: return
               
            d[x].append((y,root.val))
            dfs(root.left,x-1,y+1)
            dfs(root.right,x+1,y+1)

        d=defaultdict(list)
        dfs(root,0,0)
        return [[z for y,z in sorted(v)]for k, v in sorted(d.items())]
      
      
# Q-2 )Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root,curr):
            if root:
                curr = curr<<1|root.val
                if root.left or root.right:
                    return dfs(root.left,curr)+dfs(root.right,curr)
                else:
                    return curr
            else:
                return 0
        return dfs(root,0)     
      
      
#Q-3 )Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        dummy = curr =TreeNode()
        stack=[]
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()     
            curr.right = root
        
            curr =curr.right
            root = root.right
        
            curr.left = None
        return dummy.right     
                 
