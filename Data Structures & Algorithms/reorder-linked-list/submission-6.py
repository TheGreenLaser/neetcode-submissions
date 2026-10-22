# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #APPROACH 1
        #Make a "tail" list
        #Make a new list one from head one from tail
        #Set head = new head
        # o(n), o(n)

        #APPROACH 2
        #1. Find node length o(n)
        #2. edge case length = 1 or 2 just return empty
        #3. Find the "middle" node o(n) o(1) extra space
            #a. In odd cases let front half be > than back half
            #b. Must set "next" of last node of front half to None
        #4. How to deal with back half: reverse it o(n)
        #5. Go through front and back half separately and then reorder o(n)
        # o(n), o(1)

        #APPROACH 2 (OPTIMAL)
        #0. Edge case: return empty if !head or !head.next
        #1. Find the "middle" node
            #a. In odd cases let front half be > than back half
            #b. Must set "next" of last node of front half to None
        #2. Reverse back half
        #3. Go through front and back half separately and then reorder o(n)

        #0_____________________________
        if not head or not head.next:
            return

        #1_____________________________
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next
        slow.next = None

        #2_____________________________
        second_half = self.reverseList(second_half)

        #3_____________________________
        while second_half:
            n = head.next
            s_n = second_half.next

            head.next = second_half
            second_half.next = n

            head = n
            second_half = s_n

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n

        return prev