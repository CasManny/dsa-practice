class LinkNode:
    def __init__(self, value=0, next=None):
        self.value = value 
        self.next = next 

def reorder_list(head):
    if not head or head.next is None:
        return 
    
    slow = fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 

    current, previous = slow.next, None 
    slow.next = None 

    while current:
        next_node = current.next 
        current.next = previous
        previous = current
        current = next_node

    first, second= head, previous

    while second:
        tmp1 = first.next 
        tmp2 = second.next 

        first.next = previous
        previous.next = tmp1

        first = tmp1
        second = tmp2

