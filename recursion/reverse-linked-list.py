# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = head
        curr = prev.next
        forw = curr.next
        prev.next = None
        while forw:
            curr.next = prev
            prev = curr
            curr = forw
            forw = forw.next
        curr.next = prev
        return curr
            
        
            