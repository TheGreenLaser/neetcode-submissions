"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        APPROACH
        1. Put the nodes (original vs copy) into a hash map, creating new nodes in the process
        2. Create new LL using the info from 2

        Edge cases:
        1. head == None -> return None
        2. check if random is null
        '''

        if head == None:
            return None

        relationships = {}

        cur = head

        while cur:
            relationships[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            copy = relationships[cur]

            if cur.next:
                copy.next = relationships[cur.next]
            
            if cur.random:
                copy.random = relationships[cur.random]

            cur = cur.next

        return relationships[head]


