#Q-2 ) Write postorder and inorder traversal function for the tree given
below, including declaring classes, providing input and perform the dry run
also.
class Node:
   def __init__(self, key):
      self.left = None
      self.right = None
      self.val = key

 
# A function to do inorder tree traversal
def printInorder(root):
 
   if root:

      # First recur on left child
      printInorder(root.left)

      # then print the data of node
      print(root.val),

      # now recur on right child
      printInorder(root.right)
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
   if root:

      # First recur on left child
      printPostorder(root.left)

      # the recur on right child
      printPostorder(root.right)

      # now print the data of node
      print(root.val),

root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.right.right = Node(7)
root.left.left = Node(5)
root.left.right = Node(4)

 
print ("Inorder traversal of binary tree is")
printInorder(root)
 
print ("Postorder traversal of binary tree is")
printPostorder(root)

#Q-3) N-ary Tree Preorder Traversal 
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def preorder(node):  # root-> left, right
            if not node:
                return
            output.append(node.val)
            for c in node.children:
                preorder(c)
        output =[]
        preorder(root)
        return output
 
