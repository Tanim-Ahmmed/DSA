class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(h):
    pre = None
    cur = h
    while cur:
        nextNode = cur.next
        cur.next = pre
        pre = cur
        cur = nextNode
    return pre

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print("Original List:")
print_list(node1)

reversed_head = reverse_list(node1)

print("Reversed List:")
print_list(reversed_head)