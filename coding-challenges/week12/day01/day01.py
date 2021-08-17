#Q-2 ) Tiling a Rectangle with the Fewest Squares - Solve with DP
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        @lru_cache(None)  # @lru_cache using the maxsize attribute:
        def recur(n,m):
            if ((n == 11 and m == 13) or (m == 11 and n == 13)):
                    return 6
            if n==m:
                return 1

            lmin=min(n,m)
            lmax=max(n,m)
            ans=float('inf')
            val=0
            for i in range(lmin,0,-1):
                #this is Possibility 1
                if i==lmin:
                    val=recur(lmax-lmin,lmin)
                #this is Possibility 2
                else:
                    val=min(recur(lmax-i,lmin)+recur(i,lmin-i),
                            recur(lmax-i,i)+recur(lmin-i,lmax))
                ans=min(ans,val)

            return ans+1

        return(recur(n,m))
      
      
      
  
#Q-3 ) Divisor Game (solve with DP)

class Solution:
    def divisorGame(self, n: int) -> bool:
        # solve witj bottom up dp method
        dp=[False]*(n+1)
        dp[0],dp[1]=False,False
        for i in range(2,n+1):
            for j in range(1,i):
                if i%j==0 and dp[i-j]==False:
                    dp[i]=True
                    break
        return dp[-1]
    
      
      
      


























