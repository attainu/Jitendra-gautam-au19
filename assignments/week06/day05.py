# first question
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right =len(nums)-1
        while left <= right:
            mid = floor((left+right)/2)
            if nums[mid] == target:
                return mid 
            elif target < nums[mid]:
                right = mid -1
            else:
                left = mid +1
        return left    

    # second questioin
    
    class Solution:
    def searchRange(self, N:List[int], T:int) -> List[int]:
        Tleft = bisect_left(N, T)
        if Tleft == len(N) or N[Tleft] != T: return [-1, -1]
        return [Tleft, bisect_right(N, T) - 1]
