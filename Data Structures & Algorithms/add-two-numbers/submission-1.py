# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        APPROACH
        0. MAKE NEW LL
        1. LOOP THROUGH BOTH LLS SIMUL.
            a. ADD THE DIGITS 
            b. ADD TO NEW LL
        2. RETURN
        '''

        answer = ListNode()
        head = answer

        carry = False

        while l1 or l2:
            if l1:
                answer.val += l1.val
                l1 = l1.next

            if l2:
                answer.val += l2.val
                l2 = l2.next

            if carry:
                answer.val += 1
                carry = False

            if answer.val >= 10:
                answer.val -= 10
                carry = True
            
            if l1 or l2:
                answer.next = ListNode()
                answer = answer.next
            elif carry:
                answer.next = ListNode()
                answer.next.val = 1

        return head

        