from hashtable import HashTable

import pytest


def pytest_generate_tests(metafunc):
    # lists to create hash tables with
    test_lists = [
        [],
        [18],
        [1000, 3],
        [12, 13, 15]
    ]
    if 'test_list' in metafunc.fixturenames:
        metafunc.parametrize("test_list", test_lists)


def test_creation_through_constructor(test_list):
    # create hash, assert empty
    hash_table = HashTable(len(test_list) * 3, test_list)
    assert len(hash_table) == len(test_list)


def test_creation_through_insert(test_list):
    # create hash, assert empty
    hash_table = HashTable(len(test_list) * 3)
    length = 0
    assert len(hash_table) == length
    # insert and assert lengths
    for data in test_list:
        hash_table.insert(data)
        length += 1
        assert len(hash_table) == length
