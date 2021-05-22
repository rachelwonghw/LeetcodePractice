# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        next_node = None
        curr = head
        prev = None
        
        while curr:
            if curr.val == val:
                if prev and head:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
                else:
                    head = head.next
                    curr = head
            else:
                prev = curr
                curr = curr.next
                
        return head