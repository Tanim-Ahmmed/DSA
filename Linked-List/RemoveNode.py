#remove N-th node from end 

def removeNode(head, n):
    dummy = ListNode(0, head)
    first = second = dummy

    for _ in range(n):
        first = first.next

    while first.next:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next
