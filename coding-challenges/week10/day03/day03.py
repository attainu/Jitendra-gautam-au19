#Q-1 ) Write a program to print nodes in a BST having odd values:
class newNode: 
   def __init__(self, key): 
      self.key = key
      self.left = None
      self.right = None
  
#A utility function to do inorder 
def inorder( root) :
  
   if (root != None): 
      inorder(root.left) 
      print(root.key, end = " ") 
      inorder(root.right) 
      
def insert(node, key): 
   if (node == None): 
      return newNode(key) 
   if (key < node.key): 
      node.left = insert(node.left, key) 
   else:
      node.right = insert(node.right, key) 
   return node 
  
def oddNode(root) :

   if (root != None): 
      oddNode(root.left) 
         
      if (root.key % 2 != 0):
         print(root.key, end = " ") 
      oddNode(root.right) 

if __name__ == '__main__':
        
   root = None
root = insert(root, 8) 
root = insert(root, 3) 
root = insert(root, 1) 
root = insert(root, 6) 
root = insert(root, 4) 
root = insert(root, 7) 
root = insert(root, 10) 
root = insert(root, 14) 
root = insert(root, 13) 

oddNode(root) 


#Q-2 ) Binary Search Tree to Greater Sum Tree

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.valu=0
        self.solve(root)
        return root
    def solve (self,root):
        if root is None:
            return
        self.solve(root.right)
        root.val+=self.valu
        self.valu=root.val
        self.solve(root.left)
        
        
#Q-3 ) Kth Smallest Element in a BST
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inOrder(root):
            if root is None:
                return[]
            in_left = inOrder(root.left)
            root.val=[root.val]
            in_right =inOrder(root.right)
            return in_left+root.val+in_right
           
        return inOrder(root)[k-1]
       
