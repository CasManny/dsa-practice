class LinkNode:
    def __init__(self, value =0, next = None):
        self.value = value
        self.next = next 


def merge_two_sorted_list(l1, l2):
    dummy = LinkNode()
    current = dummy

    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next 
        else:
            current.next = l2
            l2 = l2.next
        current = current.next 

    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next 


def merge_k_sorted_arrays(lists):
    if not lists or len(lists) == 0:
        return 

    merged = None

    for l in lists:
        merged = merge_two_sorted_list(merged,l)

    return merged

def build_linked_list(values):
    if not values:
        return None
    head = LinkNode(values[0])
    current = head
    for val in values[1:]:
        current.next = LinkNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

list1 = build_linked_list([1, 4, 5])
list2 = build_linked_list([1, 3, 4])
list3 = build_linked_list([2, 6])

lists = [list1, list2, list3]

merged = merge_k_sorted_arrays(lists)
print_linked_list(merged)



