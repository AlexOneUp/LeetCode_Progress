# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy head for the result list
        tmp = dummy
        carry = 0  # Variable to store carry-over

        while l1 or l2 or carry:
            # Get the values from l1 and l2 if they exist
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry-over
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next iteration
            
            # Create a new node for the result list
            tmp.next = ListNode(total % 10)
            tmp = tmp.next  # Move to the next node in the result list
            
            # Move l1 and l2 to their next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Return the result list starting from dummy.next

       
  


'''
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
        1 1 1 1 1 1
_______________________
      8,9,9,9,0,0,0,1

- Nodes values are all 0 - 9
- 


'''