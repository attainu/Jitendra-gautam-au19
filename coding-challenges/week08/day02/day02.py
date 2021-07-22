#Q-1 ) Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = []
        for num in nums:
            squared_nums.append(num**2)
        squared_nums.sort()  
        return squared_nums
            
#Q-2 ) Reverse String        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
      
#Q-3 )Maximum Ascending Subarray Sum: 
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=[]
        a=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                a+=nums[i]
            else:
                ans.append(a)
                a=nums[i]
        ans.append(a)
        return max(ans)      
      
