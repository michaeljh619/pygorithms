# import base class
from base_sort import BaseSort


class QuickSort(BaseSort):
    @staticmethod
    def __sort_rec(list_to_sort, smallest_first):
        # Base Case: small enough list
        if len(list_to_sort) < 2:
            return list_to_sort

        # Recursive Case
        pivot = list_to_sort[-1]
        low = None
        high = None

        # split list
        if smallest_first:
            low = [e for e in list_to_sort[:-1] if e <= pivot]
            high = [e for e in list_to_sort[:-1] if e > pivot]
        else:
            low = [e for e in list_to_sort[:-1] if e >= pivot]
            high = [e for e in list_to_sort[:-1] if e < pivot]

        # recurse on low and high
        sorted_low = QuickSort.__sort_rec(low, smallest_first)
        sorted_high = QuickSort.__sort_rec(high, smallest_first)
        return sorted_low + [pivot] + sorted_high

    @staticmethod
    def sort(list_to_sort_arg, smallest_first=True):
        # post filter list
        list_to_sort = super(QuickSort,
                             QuickSort).sort(list_to_sort_arg,
                                             smallest_first)

        # start to sort
        return QuickSort.__sort_rec(list_to_sort, smallest_first)
