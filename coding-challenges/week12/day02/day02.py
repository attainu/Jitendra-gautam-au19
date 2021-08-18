#Q-1 ) Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        low, high = 0, 0   

        if not s: return True

        while high<len(t):
            if t[high] == s[low]:
                low+=1
            if low == len(s): return True

            high+=1 

        return False
      
      
# Q-2 ) Count Unique Characters of All Substrings of a Given String     
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * (len(s) + 1)
        pre = {}
        prepre = {}
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + (i - 1 - pre.get(s[i - 1], -1)) - (pre.get(s[i - 1], -1) - prepre.get(s[i - 1], -1))
            prepre[s[i - 1]] = pre.get(s[i - 1], -1)
            pre[s[i - 1]] = i - 1
        return sum(dp)










