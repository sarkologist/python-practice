from functools import partial
import pytest
from src.reverse_linked_list import reverse_linked_list, Node, from_list, to_list

from hypothesis import given, strategies as st

def test_reverse_linked_list():
    assert(reverse_linked_list(Node(1))) == Node(1)
    assert(reverse_linked_list(Node(1,Node(2)))) == Node(2,Node(1))

def __linked_list(elements, draw):
    lst = draw(st.lists(elements))
    return from_list(lst)

def linked_list(elements):
    return st.composite(lambda draw: __linked_list(elements, draw))

@given(linked_list(st.integers())())
def test_double_reversal(lst):
    assert reverse_linked_list(reverse_linked_list(lst)) == lst


@given(linked_list(st.integers())())
def test_to_from_linked_list(lst):
    assert from_list(to_list(lst)) == lst

@given(st.lists(st.integers()))
def test_from_to_linked_list(lst):
    assert to_list(from_list(lst)) == lst