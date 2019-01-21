def insertion_sort(unsorted_list, smallest_first=True):
    # make sure unsorted_list is a list
    if not isinstance(unsorted_list, list):
        raise TypeError("'unsorted_list' arg must be a list!")

    # make shallow copy of list
    sorted_list = unsorted_list[:]

    # begin at second index and insert working backwards
    for i_insertee in range(1, len(sorted_list)):

        # work backwards to find spot to insert
        i_insert_search = i_insertee-1
        insertee = sorted_list[i_insertee]
        while i_insert_search >= 0:
            # compare and set flag if swap is needed
            needs_swap = False
            current_element = sorted_list[i_insert_search]
            if smallest_first and insertee < current_element:
                needs_swap = True
            elif not smallest_first and insertee > current_element:
                needs_swap = True

            # if needs swap, then swap
            if needs_swap:
                sorted_list[i_insert_search+1] = current_element
                sorted_list[i_insert_search] = insertee
            # else break, since the insertee is in the right spot
            else:
                break
            # decrement to keep searching backwards
            i_insert_search -= 1
    
    # return sorted list
    return sorted_list
