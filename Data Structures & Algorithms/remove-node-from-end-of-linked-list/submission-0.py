# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        # Calculate length
        while cur:
            length += 1
            cur = cur.next

        # Index of node to remove (0-indexed)
        to_remove = length - n

        cur = head
        prev = None
        count = 0

        # Find node to remove
        while count < to_remove:
            prev = cur
            cur = cur.next
            count += 1

        # Remove node
        if prev is None:
            head = cur.next
        else:
            prev.next = cur.next

        return head
            
        
        
            