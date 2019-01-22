from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
import pytest


def pytest_generate_tests(metafunc):
    # different sorting types
    sort_types = [BubbleSort, InsertionSort, MergeSort]
    if 'sorter' in metafunc.fixturenames:
        metafunc.parametrize("sorter", sort_types)

    # lists and their sorted versions
    test_lists_and_answers = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([7, 3, 12, 15, 200, 1, 8], [1, 3, 7, 8, 12, 15, 200]),
        ([5, 4, 3, 2, 1, 0, -12], [-12, 0, 1, 2, 3, 4, 5]),
    ]
    if 'test_list_and_answer' in metafunc.fixturenames:
        metafunc.parametrize('test_list_and_answer',
                             test_lists_and_answers)


def test_sort(sorter, test_list_and_answer):
    # get params
    test_list = test_list_and_answer[0]
    answer = test_list_and_answer[1]
    reversed_answer = answer[::-1]

    # sort LtG
    output_list = sorter.sort(test_list)
    assert output_list == answer

    # sort GtL
    output_list = sorter.sort(test_list, smallest_first=False)
    assert output_list == reversed_answer


def test_not_a_list_arg(sorter):
    # test non iterable input
    with pytest.raises(TypeError) as e_info:
        sorter.sort(5)
    with pytest.raises(TypeError) as e_info:
        sorter.sort(7.3)

    # test iterable, but non-list input
    with pytest.raises(TypeError) as e_info:
        sorter.sort("ABCDE")
