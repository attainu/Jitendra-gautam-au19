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


#Q-2 )Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0
        l,r=0 ,len(height) -1
        leftMax, rightMax = height[l],height[r]
        res = 0
        
        while l<r:
            if leftMax < rightMax:
                l+=1
                leftMax =max(leftMax,height[l])
                res += leftMax -height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                res += rightMax -height[r]
        return res     
        
