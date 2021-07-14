# 1.Given a non-negative integer x, compute and return the square root of x.

#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
      
# 2.Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexit
 class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        size = len(nums)-1
        output = []
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
                break
        nums = nums[::-1]
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(size - i)
                break
        return output
 
# 3.A peak element is an element that is strictly greater than its neighbors.

#Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

#You may imagine that nums[-1] = nums[n] = -∞.

#You must write an algorithm that runs in O(log n) time.

 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        for i in range(len(nums)):
            if i == 0 and nums[i+1] < nums[i]: 
                return i
            elif i==n-1 and nums[i-1] < nums[i]:
                return i
            else:
                 if nums[i-1]< nums[i] and nums[i] > nums[i+1]:
                    return i
                                     
                    
 # Time complexity is O(log n), space complexity is O(1)                   

          
