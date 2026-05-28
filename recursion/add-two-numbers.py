# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      dummyHead = ListNode(0)
      curr = dummyHead
      remainder = 0

      while l1 or l2 or remainder != 0:
        if l1 != None:
            x = l1.val
        else:
            x = 0
            
        if l2 != None:
            y = l2.val
        else:
            y = 0
        sum = x + y + remainder
        remainder = sum // 10
        singleDigit = sum % 10
        
        curr.next = ListNode(singleDigit)
        curr = curr.next
        
        if l1:
          l1 = l1.next
        if l2:
          l2 = l2.next

        # if remainder != 0:
        #   curr.val = remainder
        
      return dummyHead.next