from insertion_sort import insertion_sort as ins
import pytest

def test_trivial():
    # test empty list
    empty_list = ins([])
    assert empty_list == []

    # test 1 element
    one_list = ins([5])
    assert one_list == [5]

    # test empty list
    empty_list = ins([], smallest_first=False)
    assert empty_list == []

    # test 1 element
    one_list = ins([5], smallest_first=False)
    assert one_list == [5]

def test_sorting_least_to_greatest():
    # test size 2 list ordered
    two_list_ord = ins([1, 2])
    assert two_list_ord == [1, 2]

    # test size 2 list unordered
    two_list_unord = ins([2, 1])
    assert two_list_unord == [1, 2]

    # test larger list
    large_list_unord = ins([5, 3, 4, 1, 2])
    assert large_list_unord == [1, 2, 3, 4, 5]

    # test larger list
    large_list_ord = ins([1, 2, 3, 4, 5])
    assert large_list_ord == [1, 2, 3, 4, 5]


def test_sorting_greatest_to_least():
    # test size 2 list ordered
    two_list_ord = ins([2, 1], smallest_first=False)
    assert two_list_ord == [2, 1]

    # test size 2 list unordered
    two_list_unord = ins([1, 2], smallest_first=False)
    assert two_list_unord == [2, 1]

    # test larger list
    large_list_unord = ins([5, 3, 4, 1, 2], smallest_first=False)
    assert large_list_unord == [5, 4, 3, 2, 1]

def test_bad_unsorted_list_arg():
    # test non iterable input
    with pytest.raises(TypeError) as e_info:
        ins(5)
    with pytest.raises(TypeError) as e_info:
        ins(7.3)

    # test iterable, but non-list input
    with pytest.raises(TypeError) as e_info:
        ins("ABCDE")
