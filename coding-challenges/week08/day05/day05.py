#Q-1 )Find the Duplicate Number:

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0]!=nums[nums[0]]:
            nums[nums[0]],nums[0]=nums[0],nums[nums[0]]
        return nums[0]    
#Time Complexity: O(n)
#Space Complexity: O(1)

#Q-2 )Sum of Unique Elements:
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            if(nums.count(i)==1):
                total=total+i
        return total
      
  #Q-3 ) Longest Common Prefix: 
  class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        for i in range(min(map(len, strs))):
            ch = strs[0][i]
            if all(s[i] == ch for s in strs):
                prefix += ch
            else:
                break
        return prefix
      
