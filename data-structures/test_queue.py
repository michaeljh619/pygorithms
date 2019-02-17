from queue import Queue

import pytest


def test_is_empty():
    q = Queue()
    assert q.is_empty()


def test_operations():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.dequeue() == 3
    assert q.dequeue() == 2
    assert q.dequeue() == 1


def test_errors():
    q = Queue()

    with pytest.raises(IndexError) as e_info:
        q.dequeue()
