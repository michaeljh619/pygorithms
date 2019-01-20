def bubble_sort(unsorted_list, smallest_first=True):
    # make sure unsorted_list is a list
    if not isinstance(unsorted_list, list):
        raise TypeError("'unsorted_list' arg must be a list!")

    # make shallow copy of list
    sorted_list = unsorted_list[:]

    # passes loop
    while True:
        was_swapped = False

        # begin passes at first index
        for pass_start_index in range(len(sorted_list)-1):

            # individual pass
            for i in range(pass_start_index, len(sorted_list)-1):
            
                # compare and set flag if needs to be swapped
                needs_swap = False
                if smallest_first and sorted_list[i] > sorted_list[i+1]:
                    needs_swap = True
                elif not smallest_first and sorted_list[i] < sorted_list[i+1]:
                    needs_swap = True

                # swap if necessary
                if needs_swap:
                    tmp = sorted_list[i]
                    sorted_list[i] = sorted_list[i+1]
                    sorted_list[i+1] = tmp
                    was_swapped = True
        
        # stop passes if no swaps
        if not was_swapped:
            break

    # return sorted list
    return sorted_list
