# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = node = ListNode()
        
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next, list1 = list1, list1.next
            else:
                node.next, list2 = list2, list2.next
            node = node.next
        
        if list1:
            node.next = list1
        else:
            node.next = list2
            
        return res.next
        
'''
res will be the head of the new list 

    if list1 < list2, 
        node next = list1 curr node
        iter list1 
    else 
        list2 curr node
        iter list2
    

'''