#Q1. Represent a graph using adjacency list and adjacency matrix.

import collections

class Graph:
   def __init__(self):
      self.graph = collections.defaultdict(dict)

   def add_edge(self, u, v, weight = 1, directed = True):
      self.graph[u][v] = weight
      if not directed:
         self.graph[v][u] = weight

   def __str__(self):
      to_return = ''
      for vertex in self.graph:
         to_return += str(vertex) + ': '
         for edge in self.graph[vertex]:
               to_return +=  '(' + str(edge) + ', ' + str(self.graph[vertex][edge]) + ')'
               to_return += '   '

         to_return += '\n'
      return to_return

if __name__ == '__main__':
   g = Graph()
   g.add_edge(1, 2, 7, False)
   g.add_edge(1, 3, 2, False)
   g.add_edge(2, 3, 1, False)
   g.add_edge(2, 4, 5, False)
   g.add_edge(2, 5, 3, False)
   g.add_edge(3, 5, 11, False)
   g.add_edge(4, 5, 10, False)
   g.add_edge(4, 6, 7, False)
   g.add_edge(5, 6, 4, False)
   print((g))



#Q-2 )Palindrome Number - Try using BFS in this
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        d=deque(str(x))
        while d:
            l=d.popleft()
            if d:  
                r=d.pop()
                if int(l)!=int(r):
                    return False
        return True
      

#Q-3 ) Binary Tree Zigzag Level Order Traversal
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        s1 = [root]
        s2 = []
        level = []
        result = []
        while s1 or s2:
            while s1:
                root = s1.pop()
                level.append(root.val)
                if root.left :
                    s2.append(root.left)
                if root.right:
                    s2.append(root.right)
            result.append(level)
            level =[]
            while s2:
                root = s2.pop()
                level.append(root.val)
                if root.right:
                    s1.append(root.right)
                if root.left:
                    s1.append(root.left)
            if level != []:
                result.append(level)
                level = []
        return result     
