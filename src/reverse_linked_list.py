class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __eq__(self, other):
        return self.data == other.data and self.next == other.next

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next, prev = prev, curr
        curr = next_node
        
    return prev