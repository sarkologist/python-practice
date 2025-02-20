import pytest
from src.reverse_linked_list import reverse_linked_list, Node, to_list

from hypothesis import given, strategies as st

def test_reverse_linked_list():
    assert reverse_linked_list(None) == None
    assert reverse_linked_list(Node(1)) == Node(1)
    assert reverse_linked_list(Node.from_list([1,2])) == Node(2,Node(1))

def linked_list(elements):
    @st.composite
    def go(draw):
        lst = draw(st.lists(elements))
        return Node.from_list(lst)
    return go

@given(linked_list(st.integers())())
def test_double_reversal(lst):
    assert reverse_linked_list(reverse_linked_list(lst)) == lst

@given(linked_list(st.integers())())
def test_to_from_linked_list(lst):
    assert Node.from_list(to_list(lst) if lst else []) == lst

@given(st.lists(st.integers()))
def test_from_to_linked_list(lst):
    assert to_list(Node.from_list(lst)) == lst

@given(st.lists(st.integers()))
def test_to_list_respects_reverse(lst):
    assert not lst or Node.from_list(lst[::-1]) == reverse_linked_list(Node.from_list(lst))

@given(linked_list(st.integers())())
def test_from_list_respects_reverse(lst):
    as_list = to_list(lst)
    assert to_list(reverse_linked_list(lst)) == as_list[::-1]