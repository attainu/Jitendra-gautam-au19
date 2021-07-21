#Q-1 ) Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1) # here & use for itersection in set1 and set2
        
#Q-2 ) Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n -1
        while m > 0 and n > 0:
            if nums1[m-1]> nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]= nums2[n-1]
                n-=1
            last-=1
        while n>0:
            nums1[last]=nums2[n-1]
            n,last=n-1,last-1
          
 #Q-3 ) Sort Colors

 class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,white,blue=0,0,len(nums)-1
        while(white<=blue):
            if nums[white]==0:
                nums[white],nums[red]=nums[red],nums[white]
                white+=1
                red+=1
            elif nums[white] ==1:
                       white+=1
            else:
                nums[white],nums[blue] = nums[blue],nums[white]
                blue-=1
                        
            
