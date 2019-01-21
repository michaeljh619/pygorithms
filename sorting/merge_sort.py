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

def __merge_sort_rec(unsorted_list, smallest_first):
    # base case: list is length <= 1
    if len(unsorted_list) <= 1:
        return unsorted_list

    # recursive case
    else:
        # split list into 2 halves
        half_index = len(unsorted_list)/2
        left_list = __merge_sort_rec(unsorted_list[:half_index],
                                     smallest_first)
        right_list = __merge_sort_rec(unsorted_list[half_index:],
                                      smallest_first)
        # merge sorted lists
        return __merge(left_list, right_list, smallest_first)

def merge_sort(unsorted_list, smallest_first=True):
    # make sure unsorted_list is a list
    if not isinstance(unsorted_list, list):
        raise TypeError("'unsorted_list' arg must be a list!")

    # make shallow copy of list
    sorted_list = unsorted_list[:]

    # begin merge sort
    return __merge_sort_rec(sorted_list, smallest_first)
