class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next

# Iterative method
class Solution:
    def reverseList(head: LinkedList):
        curr, prev = head, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
# Recursive Method
class ReSolution:
    def reverseList(self, head: LinkedList):
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
    
        