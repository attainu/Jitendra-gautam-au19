#Q-1 ) Fibonacci Number - solve without DP

class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        
        prev1,prev2 = 1,0
        output = 0
        for i in range(2,n+1):
            output = prev1+prev2
            prev2=prev1 
            prev1= output
            
        return output    
      
      
      
#Q-2 )Solve above question with DP 

class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        dp =[0,1]+[0]*(n-1)   # here  dp is dynamic programming
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]   
      
      
      
#Q-3 )Pow(x, n) 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if  n < 0:
            n=-n
            x=1/x
            
        while  n > 0:
            if n%2==1:
                result=result*x
            n=n>>1
            
            x=x*x
        return result
   
#and second approch
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        
