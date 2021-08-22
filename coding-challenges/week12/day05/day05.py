#Q-1 ) N-Queens
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backTrack(i):
            nonlocal ans
            if i == n:
                ans += 1
                return
            for j in range (n): 
                if not columns[j] and not diagonals[i+j] and not antiDiagonals[i-j]:
                    columns[j] = True
                    diagonals[i+j] = True
                    antiDiagonals[i-j] = True

                    backTrack(i+1)

                    columns[j] = False
                    diagonals[i+j]=False
                    antiDiagonals[i-j] = False
        columns = [False] * n
        diagonals = defaultdict(bool)
        antiDiagonals = defaultdict(bool)
        ans = 0 
        backTrack(0)

        return ans
      
      
      
#Q-2)Sum of All Subset XOR Totals
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l = len(nums)
        res = 0

        stack = [(0, 0)]

        while stack:
            pos, xor = stack.pop()
            res+=xor
            for i in range(pos, l):
                stack.append((i+1, xor^nums[i]))
        return res

                  
            

            
#Q-3)All Paths From Source to Target 
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        out = []
        
        def backtrack(path, nextpos):
			# It means that we are in the final position.
			
            if path[-1] == len(graph) - 1:
                out.append(path)
                return
            
			# Iterate through each possible next position
            for i in nextpos:
                backtrack(path + [i], graph[i])
            
        for start in graph[0]:
            backtrack([0, start], graph[start])
        
        
        return out
      



























