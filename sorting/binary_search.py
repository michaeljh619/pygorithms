def binary_search(sorted_list, element, smallest_first=True):
    # bounding indices
    low_i = 0
    high_i = len(sorted_list) - 1

    # search to the point where high and low are 1 element away
    # or lower
    while high_i - low_i > 1:
        # Get middle element
        mid_i = (low_i + high_i)/2
        mid_e = sorted_list[mid_i]

        # Compare
        if element == mid_e:
            return mid_i
        if smallest_first:
            if element < mid_e:
                high_i = mid_i
            else:
                low_i = mid_i
        else:
            if element < mid_e:
                low_i = mid_i
            else:
                high_i = mid_i

    # Did not find element
    if high_i - low_i < 0:
        return None
    # high_i and low_i converged on same index, check it
    elif high_i - low_i == 0:
        if element == sorted_list[low_i]:
            return low_i
        else:
            return None
    # high_i and low_i are 1 index away from each other,
    # check both
    else:
        if element == sorted_list[low_i]:
            return low_i
        elif element == sorted_list[high_i]:
            return high_i
        else:
            return None
