# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = []

        node = head

        while node:
            if node in l:
                return True
            
            l.append(node)
            node = node.next
        return False