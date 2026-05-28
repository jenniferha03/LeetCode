# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        curr = list3
        
        while list1 and list2:
            temp = ListNode()
            if list1.val <= list2.val:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
            
            curr.next = temp
            curr = curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
            
        return list3.next
        
            