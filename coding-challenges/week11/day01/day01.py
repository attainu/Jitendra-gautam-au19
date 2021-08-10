#Q-1 ) write a program to take input a Binary tree and tell if that binary tree is
#alanced or not?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        if not root:
            return True
        return abs(self.findHeight(root.left) - self.findHeight(root.right)) <2 and self.isBalanced(root.left)  and self.isBalanced(root.right)
    
    def findHeight(self,root):
        if not root:
            return -1
        return 1+max(self.findHeight(root.left),self.findHeight(root.right))
      
      
      
#Q-2 )Write steps in heapify/percolate down method, and write time
#complexity and space complexity analysis.
"""
Create a Heap
A heap is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out various 
operations on heap data structure. Below is a list of these functions.

heapify − This function converts a regular list to a heap. In the resulting heap the 
smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.

heappush − This function adds an element to the heap without altering the current heap.

heappop − This function returns the smallest data element from the heap.

heapreplace − This function replaces the smallest data element with a new value supplied in the function.




Heaps help you quickly retrieve objects with the smallest or the largest key.

From this definition, we can infer that we can use heaps when we to retrieve
 the maximum or minimum object in constant time.

MinHeap operations
1.Insertion O(log n)O(logn): Finding the exact position of the new element is performed in log nlogn since 
it is only compared with the position of the parent nodes.
2.Delete Min O(log n)O(logn): After the minimum element is removed, 
the heap has to put the new root in place.
3.ind Min O(1)O(1): This is possible because the heap 
data structure always has the minimum element on the root node.
4.Heapify O(n)O(n): This operation rearranges all the nodes
 after deletion or insertion operation. The cost of this operation 
 is nn since all the elements have to be moved to keep the heap properties.
5.Delete O(log n)O(logn): A specific element from the heap can be removed in log nlogn time.


"""

#Q - 3) Merge Two Binary Trees 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
       
        if root1 and not root2:
            return root1
        if root2 and not root1:
            return root2
        # If both trees are passed 
        else:
            # Set root of merged Tree to be sum of the passed root values
            root3 = TreeNode(root1.val + root2.val)
            
            root3.left = self.mergeTrees(root1.left, root2.left)
            root3.right = self.mergeTrees(root1.right, root2.right)
            # Return the merged tree
            return root3
          
                


 
