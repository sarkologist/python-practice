import pytest
from src.reverse_linked_list import reverse_linked_list, Node

def test_reverse_linked_list():
    assert(reverse_linked_list(Node(1))) == Node(1)
    assert(reverse_linked_list(Node(1,Node(2)))) == Node(2,Node(1))