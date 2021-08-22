#Q-1 ) Pascal's Triangle 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result =[[1]]
        
        for i in range (numRows -1):
            temp =[0] + result[-1] + [0]
            row =[]
            for j in range (len(result[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            result.append(row)
        return result






#Q-3 ) Pascal's Triangle 
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = []
        temp = self.getRow(rowIndex-1)
        for i in range(len(temp)-1):
            res.append(temp[i]+temp[i+1])
        return [1]+res+[1]



#Q-3) Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr =[]
        buy = math.inf
        profit =0
        for price in prices:
            
            buy = min(price,buy)
            profit = max(price-buy ,profit)
            arr.append(profit)
        return max(arr)    
