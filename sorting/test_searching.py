from binary_search import binary_search
import pytest


def pytest_generate_tests(metafunc):
    # search types
    search_types = [binary_search]
    if 'search_type' in metafunc.fixturenames:
        metafunc.parametrize('search_type', search_types)

    # lists and their sorted versions
    test_lists = [
         [],
         [7],
         [-5, 0, 12],
         [-12, -3, 0, 15, 10070],
         [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    ]
    if 'test_list' in metafunc.fixturenames:
        metafunc.parametrize('test_list', test_lists)


def test_search(search_type, test_list):
    if len(test_list) == 0:
        assert search_type(test_list, 0) is None
    else:

        # assert element is where it's supposed to be
        for i in range(len(test_list)):
            assert search_type(test_list, test_list[i]) == i

        # same but in greatest to least order
        rev_test_list = test_list[::-1]
        for i in range(len(rev_test_list)):
            assert search_type(rev_test_list,
                               rev_test_list[i],
                               smallest_first=False) == i
