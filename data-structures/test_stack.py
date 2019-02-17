from stack import Stack

import pytest


def test_is_empty():
    s = Stack()
    assert s.is_empty()


def test_operations():
    s = Stack()

    s.push(1)
    assert s.top() == 1

    s.push(2)
    assert s.top() == 2

    s.pop()
    assert s.top() == 1


def test_errors():
    s = Stack()

    with pytest.raises(IndexError) as e_info:
        s.pop()

    with pytest.raises(IndexError) as e_info:
        s.top()
