# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        curr = head
        smallerThanHead = ListNode(0)
        smallerThan = smallerThanHead
        biggerThanHead = ListNode(0)
        biggerThan = biggerThanHead
        
        while curr:
            if curr.val < x:
                smallerThan.next = curr
                smallerThan = smallerThan.next
            elif curr.val >= x:
                biggerThan.next = curr
                biggerThan = biggerThan.next
                
            curr = curr.next
        
        smallerThan.next = biggerThanHead.next
        biggerThan.next = None
        
        return smallerThanHead.next