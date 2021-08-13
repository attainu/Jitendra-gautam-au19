#Q-1 ) Climbing Stairs - solve without DP
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        first,second=1,2
       
        for start in range(2,n):
            first,second = second,first+second
           
        return second

#Q-1 ) Climbing Stairs - solve without DP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*2
        dp[0]=1
        if n>=1:
            dp[1] = 1
        for i in range(2,n+1):
            dp[i%2]=dp[(i-1)%2]+dp[(i-2)%2]
        return dp[n%2]    
      
      
#Q-3 ) Longest Common Subsequence - Solve using DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for z in range (n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]                              
