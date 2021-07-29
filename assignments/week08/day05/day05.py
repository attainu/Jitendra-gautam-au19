#Q-2 )Next Greater Element I: 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dict={}
        for i in nums2:
            while(stack and stack[-1]<i):
                j=stack.pop()
                dict[j]=i
            stack.append(i)
        return[dict.get(v,-1)for v in nums1]    
        
        
#Q-3 ) Build an Array With Stack Operations        
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        j=0
        for i in range(1,n+1):
            if i in target:
                ans.append("Push")
                j=max(len(ans),j)
            else:
                ans.append("Push")
                ans.append("Pop")
        while ans[-1] == "Pop":
            ans.pop()
        return ans[:j]         
