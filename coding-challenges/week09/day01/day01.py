#Q-1 ) Valid Parentheses:
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i not in dict:
                stack.append(i)
            elif len(stack)==0 or stack.pop()!=dict[i]:
                return False
        if len(stack) == 0:
            return True
          
#Q-2 )Baseball Game: 
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record =[]
        for i in ops:
            if i =="C":
                record.pop()
            elif i =="D":
                record.append(record[-1]*2)
            elif i =="+":
                record.append(record[-1]+record[-2])
            else:
                record.append(int(i))
        return sum (record)       
                
                 
#Q-3 )Remove All Adjacent Duplicates In String 
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        
