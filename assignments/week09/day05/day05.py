#Q-1 ) Implement Queue using Stacks 
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack =[]
        
    

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """ 
        return self.stack.pop(0)
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
      
        return self.stack[0]
     
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack)==0
           


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
        nums =[]
        while head :
            nums.append(head.val)
            head = head.next
        l,r = 0, len(nums)-1  # here l is left and r is right
        while l <= r:
            if nums[l]!=nums[r]:
                return False
            l+=1
            r-=1
        else: 
            return True       
        
