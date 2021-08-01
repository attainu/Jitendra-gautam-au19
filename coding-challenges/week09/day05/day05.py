#Q-1 ) Delete Node in a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        cur = node
        while node.next!=None:
            node.val = node.next.val
            cur = node
            node = node.next
        cur.next = None
        
        
#Q-2 )Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr=head
        while curr:
            if curr.next and curr.next.val==curr.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
      
      
#Q-3 ) Merge In Between Linked Lists 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        counter = 0
        ListNodea = list1
        ListNodeb = list1
        while counter <= b and  ListNodeb:
            if counter < a - 1:
                ListNodea =  ListNodea.next 
            ListNodeb =  ListNodeb.next
            counter += 1       
        ListNodea.next = list2
        while list2.next:
            list2 = list2.next
        list2.next =  ListNodeb
        return list1
