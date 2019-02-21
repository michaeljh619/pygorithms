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


def test_creation_through_constructor(test_list):
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


def test_creation_through_append(test_list):
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


def test_linkedlist_to_list(test_list):
    # create linked list
    linked_list = LinkedList(test_list)
    assert list(linked_list) == test_list


def test_getitem(test_list):
    # create linked list
    linked_list = LinkedList(test_list)
    # test __getitem__
    for i in range(len(test_list)):
        assert linked_list[i] == test_list[i]


def test_setitem(test_list):
    # create linked list
    linked_list = LinkedList(test_list)
    # set items in linked list to the reverse of the test list
    test_list_rev = test_list[::-1]
    for i in range(len(test_list_rev)):
        linked_list[i] = test_list_rev[i]
    # test items are set properly
    for i in range(len(test_list_rev)):
        assert linked_list[i] == test_list_rev[i]


def test_remove_by_each_index(test_list):
    # remove elements by each index as many times as you can and
    # compare to removing it from original list
    length = len(test_list)
    for i in range(length):
        # create linked list
        linked_list = LinkedList(test_list)
        test_list_with_removed = test_list[:]
        num_times_can_remove = length - i
        # keep removing from this index as many times as possible
        while num_times_can_remove > 0:
            # remove index from both linked list and test list
            linked_list.remove(i)
            test_list_with_removed.pop(i)
            # assert lists match
            assert list(linked_list) == test_list_with_removed
            num_times_can_remove -= 1
