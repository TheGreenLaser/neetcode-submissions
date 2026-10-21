# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Make a "tail" list
        #Make a new list one from head one from tail
        #Set head = new head
        # o(n), o(n)

        #1. Find node length o(n)
        #2. edge case length = 1 or 2 just return empty
        #3. Find the "middle" node o(n) o(1) extra space
            #a. In odd cases let front half be > than back half
            #b. Must set "next" of last node of front half to None
        #4. How to deal with back half: reverse it o(n)
        #5. Go through front and back half separately and then reorder o(n)
        # o(n), o(1)

        #1_____________________________
        length = 0 
        temp_head = head

        while(temp_head != None):
            temp_head = temp_head.next
            length += 1

        #2_____________________________
        if length <= 2:
            return

        #3_____________________________
        middle = head

        #a_____________________________
        nexts = (length + 1) / 2 - 1 # number of nexts

        while(nexts > 0):
            nexts -= 1
            middle = middle.next

        second_half = middle.next

        #b_____________________________
        middle.next = None

        #4_____________________________
        second_half = self.reverseList(second_half)

        #5_____________________________
        while head and second_half:
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
        




            








 

