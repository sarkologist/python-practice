class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __eq__(self, other):
        return self.data == other.data and self.next == other.next

    def __repr__(self):
        return repr(to_list(self))
        
    @classmethod
    def from_list(self, lst):
        head = None
        for i in reversed(lst):
            head = Node(i, head)
        return head

def to_list(head):
    lst = []
    while head:
        lst.append(head.data)
        head = head.next
    return lst

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next, prev = prev, curr
        curr = next_node
        
    return prev
