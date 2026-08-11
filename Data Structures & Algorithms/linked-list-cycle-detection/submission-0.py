# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()

        while not head == None:
            if head in hash_set:
                return True
            else:
                hash_set.add(head)
                head = head.next

        return False