#Q-2 ) Min Stack: 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normalstack = []
        self.min_stack = []
       

    def push(self, val: int) -> None:
        if not self.normalstack:
            self.normalstack.append(val)        
            self.min_stack.append(val)
        else:
            self.normalstack.append(val)
            self.min_stack.append(min(val,self.min_stack[-1]))
        

    def pop(self) -> None:
        self.normalstack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.normalstack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Q-3 )Trapping Rain Water 
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[0]*n
        right=[0]*n
        if n==0:
            return 0
        left[0]=height[0]
        right[len(height)-1]=height[-1]
        for i in range(len(height)):
            left[i]=max(height[i],left[i-1])
        for j in range(len(height)-2,-1,-1):
            right[j]=max(height[j],right[j+1])
        print(left,right)
        ans=0
        for i in range(len(height)):
            ans+=min(left[i],right[i])-height[i]
        return ans
        
