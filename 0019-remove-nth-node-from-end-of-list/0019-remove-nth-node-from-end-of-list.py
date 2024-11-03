# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # resulting head node
        dummy = ListNode(0, head)
        trail = dummy
        front = dummy
        # move front ptr n times in front of trailing ptr
        for _ in range(n):
            front = front.next

        # while front isn't null move front and trail
        while front.next:
            trail, front = trail.next, front.next
        
        # trailing ptr is now directly behind the Nth node, skip the next node
        trail.next = trail.next.next
        #while trail isn't none
        while trail.next != front.next:
                trail = trail.next

        # dummy is the head of the new linked list
        return dummy.next
        
'''
[1,2,3,4,5]
question: 
1. mutating original ll?

intuition :
    - 2 ptrs at the start
    - start 1 ptr at head, and 2nd ptr n-nodes away from head
    
    - traverse LL until 2nd ptr is at end
        - if it's at the end, then we know the nth node is next to our 1st ptr
    
    - reassign the ptrs from the tail n-1 times
        - [1,2,3,4, 5,  6, 7] n = 3
                            h->null
                    t->nth
                    
1.for  n = 2 
    [1,2,3, 4, 5] 
              ->h -> null
         t->nth
2. we know the nth node is next to thr trailing ptr
     
3. reassign ptrs n-1 times until trailing ptr reaches our head

'''