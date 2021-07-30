#Q-1 ) Write a program to remove first node from a linked list:
# node structure
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

#class LinkedList
class LinkedList:
   def __init__(self):
      self.head = None

  #Add new element at the end of the list
   def addAtEnd(self, newElement):
      newNode = Node(newElement)
      if(self.head == None):
         self.head = newNode
         return
      else:
         temp = self.head
         while(temp.next != None):
            temp = temp.next
         temp.next = newNode

  #Delete first node of the list
   def remove_front(self):
      if(self.head != None):
         self.head = self.head.next
         temp = None 

  #display the content of the list
   def PrintList(self):
      temp = self.head
      if(temp != None):
         print("The list contains:", end=" ")
         while (temp != None):
            print(temp.data, end=" ")
            temp = temp.next
         print()
      else:
         print("The list is empty.")

# test the code                 
MyList = LinkedList()

#Add four elements in the list.
MyList.addAtEnd(2)
MyList.addAtEnd(5)
MyList.addAtEnd(6)
MyList.addAtEnd(8)
MyList.addAtEnd(3)
MyList.PrintList()

#Delete the first node
MyList.remove_front()
MyList.PrintList()  

#output:
#5
#6
#8
#3

#Q-2 ) Convert Binary Number in a Linked List to Integer: 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result =head.val
        while head.next!=None:
            result = result*2+head.next.val
            head = head.next
        return result    
      
      
#Q-3 ) Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        walker = runner = head
        while runner and runner.next:
            walker= walker.next
            runner =runner.next.next
        return walker    
