class ListNode:
    def __init__(self, value=0, next = None):
        self.value = value
        self.next = next 
        
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Move fast n steps
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the node
        slow.next = slow.next.next

        return dummy.next