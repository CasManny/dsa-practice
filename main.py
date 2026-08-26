def reorderLinkedList(head):
    if not head or not head.next:
        return 
    
    slow = head
    fast = head 
    
    # find the middle of the linkedlist
    while fast and fast.next:
        slow = slow.next 
        fast = slow.next.next 
    
    # Reverse the second one
    current, previous = slow.next, None
    slow.next = None
    while current:
        next_node = current.next 
        current.next = previous
        previous = current
        current = next_node
        
    first, second = head, previous 
    while second:
        tmp1 = first.next 
        tmp2 = second.next 
        
        first.next = second
        second.next = tmp1
        
        first = tmp1
        second = tmp2