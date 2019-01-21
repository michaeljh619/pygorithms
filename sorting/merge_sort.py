from base_sort import BaseSort


class MergeSort(BaseSort):
    @staticmethod
    def __merge(left_list, right_list, smallest_first):
        # merge until no elements left
        sorted_list = []
        while len(left_list) > 0 and len(right_list) > 0:

            # decide which should insert
            left_should_insert = False
            if smallest_first and left_list[0] < right_list[0]:
                left_should_insert = True
            elif not smallest_first and left_list[0] > right_list[0]:
                left_should_insert = True

            # insert corresponding list's first element
            if left_should_insert:
                sorted_list.append(left_list[0])
                left_list = left_list[1:]
            else:
                sorted_list.append(right_list[0])
                right_list = right_list[1:]

        # one list ran out of elements, insert the rest at end
        if len(left_list) > 0:
            sorted_list += left_list
        else:
            sorted_list += right_list

        # return sorted list
        return sorted_list

    @staticmethod
    def __merge_sort_rec(unsorted_list, smallest_first):
        # base case: list is length <= 1
        if len(unsorted_list) <= 1:
            return unsorted_list

        # recursive case
        else:
            # split list into 2 halves
            half_index = len(unsorted_list)/2
            left_list = MergeSort.__merge_sort_rec(
                            unsorted_list[:half_index],
                            smallest_first)
            right_list = MergeSort.__merge_sort_rec(
                                        unsorted_list[half_index:],
                                        smallest_first)
            # merge sorted lists
            return MergeSort.__merge(left_list, right_list,
                                     smallest_first)

    @staticmethod
    def sort(list_to_sort_arg, smallest_first=True):
        # post filter list
        list_to_sort = super(MergeSort,
                             MergeSort).sort(list_to_sort_arg,
                                             smallest_first)

        # begin merge sort
        return MergeSort.__merge_sort_rec(list_to_sort,
                                          smallest_first)
