from linkedlist import Link, LinkedList

import pytest


def pytest_generate_tests(metafunc):
    # lists to create linked lists with
    test_lists = [
        [],
        [12],
        [3, 1],
        [3, 1, 12],
        [15, 1000, -1, 86],
        ["mike", "sonia"],
        [[12, 1], [45, 44], [13], [1, 1, 1]],
        [LinkedList(), LinkedList(), LinkedList()]
    ]
    if 'test_list' in metafunc.fixturenames:
        metafunc.parametrize("test_list", test_lists)


def test_creation(test_list):
    # create linked list through constructor
    linked_list = LinkedList(test_list)
    # test length
    assert len(linked_list) == len(test_list)
    assert linked_list.length == len(test_list)
    # test linked list against data
    index = 0
    for data in linked_list:
        assert data == test_list[index]
        index += 1

    # create linked list through append
    linked_list = LinkedList()
    for data in test_list:
        linked_list.append(data)
    # test length
    assert len(linked_list) == len(test_list)
    assert linked_list.length == len(test_list)
    # test linked list against data
    index = 0
    for data in linked_list:
        assert data == test_list[index]
        index += 1
