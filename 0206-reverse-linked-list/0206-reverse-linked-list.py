# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, cur = None, head

        # while current node isn't null
        while cur:
            nxt = cur.next 
            # 1 = 2
            cur.next = prev
            # 2 = 1
            prev = cur
            # null = 1
            cur = nxt
            # 1 = 2

            
            # 2 1 1 2
        return prev