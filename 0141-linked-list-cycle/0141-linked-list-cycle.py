# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # If there is no head / start of the list, return false
        if not head:
            return False
        
        # Tortoise hare method
        s = head
        f = head.next
        
        while s != f :
            # If the fast ptr doesn't reach end or the end - 1 ptr
            if not f or not f.next:
                return False
            s = s.next
            f = f.next.next

        return True

        
        