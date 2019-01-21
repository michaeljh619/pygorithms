from bubble_sort import Bubble_Sort
from insertion_sort import Insertion_Sort
from merge_sort import Merge_Sort
import pytest


def pytest_generate_tests(metafunc):
    sort_types = [Bubble_Sort, Insertion_Sort, Merge_Sort]
    if 'sorter' in metafunc.fixturenames:
        metafunc.parametrize("sorter", sort_types)


def test_trivial(sorter):
    # test empty list
    empty_list = sorter.sort([])
    assert empty_list == []

    # test list with one element
    one_list = sorter.sort([1])
    assert one_list == [1]

    # test empty list, greatest to least
    empty_list = sorter.sort([], smallest_first=False)
    assert empty_list == []

    # test list with one element, greatest to least
    one_list = sorter.sort([1], smallest_first=False)
    assert one_list == [1]


def test_sorting_least_to_greatest(sorter):
    # test size 2 list ordered
    two_list_ord = sorter.sort([1, 2])
    assert two_list_ord == [1, 2]

    # test size 2 list unordered
    two_list_unord = sorter.sort([2, 1])
    assert two_list_unord == [1, 2]

    # test larger list
    large_list_unord = sorter.sort([5, 3, 4, 1, 2])
    assert large_list_unord == [1, 2, 3, 4, 5]

    # test larger list
    large_list_ord = sorter.sort([1, 2, 3, 4, 5])
    assert large_list_ord == [1, 2, 3, 4, 5]


def test_sorting_greatest_to_least(sorter):
    # test size 2 list ordered
    two_list_ord = sorter.sort([2, 1], smallest_first=False)
    assert two_list_ord == [2, 1]

    # test size 2 list unordered
    two_list_unord = sorter.sort([1, 2], smallest_first=False)
    assert two_list_unord == [2, 1]

    # test larger list
    large_list_unord = sorter.sort([5, 3, 4, 1, 2], smallest_first=False)
    assert large_list_unord == [5, 4, 3, 2, 1]


def test_bad_unsorted_list_arg(sorter):
    # test non iterable input
    with pytest.raises(TypeError) as e_info:
        sorter.sort(5)
    with pytest.raises(TypeError) as e_info:
        sorter.sort(7.3)

    # test iterable, but non-list input
    with pytest.raises(TypeError) as e_info:
        sorter.sort("ABCDE")
