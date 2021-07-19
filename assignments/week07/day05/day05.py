#Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

#Return the sorted array.

 

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mp = {}
        for i in set(nums):
            x=nums.count(i)
            try:
                mp[x].append(i)
            except:
                mp[x]=[i]
        ans=[]

        for i in sorted(mp):
             for j in sorted(mp[i], reverse=True):
                ans.extend([j]*i)
        return ans


     
