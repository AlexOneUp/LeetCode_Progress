# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
#         find midpoint list
        
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
#         Now slow is the mid-point   
        
        def reverse(node):
            cur = node
            prev = None
        
            while cur:            
                nxt = cur.next  
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        midpt = reverse(slow)
        left = head

        # While midpt.next exists and isn't Null
        while midpt.next:     
            next_hop = left.next
            left.next = midpt
            left = next_hop
            
            next_hop = midpt.next
            midpt.next = left
            midpt = next_hop
            
# Initial Approach :
# // Find the midpoint splitting the list into 2 sections w/ 2 pointer approach
# // Reverse the 2nd half
# // uses 2 ptr approach to find mid point of LL, reverses the start of the 2nd half, uses other temp nodes to reassign the ptrs.