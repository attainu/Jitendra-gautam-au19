#Q-1 ) Implement Queue using Stacks 
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 =[]
        self.stack2=[]
    

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """ 
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        ans =self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ans
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ans = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack1 and not self.stack2:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


#Q-2 ) Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur= head
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result == result[::-1]  

            
#Q-3) Maximum Depth of Binary Tree(or height of a BT):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def height(root):
            if root is None:
                return 0
        
            x = height(root.left)
            y = height(root.right)

            if x > y:
                return x + 1
            else:
                return y + 1

    
        return height(root)
    
    
#Q - 4) [BONUS QUESTION] Implement a stack, using two queues.     

from queue import Queue

class Stack:
   def __init__(self) :

      #using two queues
      self.q1 =Queue()
      self.q2 = Queue()
      self.curr_size =0

   def push(self,data):
      self.curr_size +=1
      self.q2.put(data)    # push data first in empty q2
        
       #Push all element remaining element in q1 to q2: 
      while not self.q1.empty():
         self.q2.put(self.q1.queue[0])
         self.q1.get()  

      #swap the namesof two queues
      self.q = self.q1
      self.q1 = self.q2 
      self.q2 =self.q 

   def pop(self): # here we pop out elements
      if self.q1.empty():
         return 
      self.q1.get()
      self.curr_size -= 1

   def top(self):
      if self.q1.empty():
         return -1      
      return self .q1.queue[0]

   def size(self):
      return self.curr_size           

if __name__=="__main__" :
   s=Stack()
   s.push(1)
   s.push(2)
   s.push(3)
   s.push(4)      

   print("Current size:",s.size())
   print(s.top())
   s.pop()
   print(s.top())
   s.pop()
   print(s.top())
   s.pop()
   print(s.top())

   print("current size:",s.size())
       
