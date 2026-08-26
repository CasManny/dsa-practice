def linkedListCycle(head): # check if the linked list is a cycle
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True
    return False