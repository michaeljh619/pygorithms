# import base class
from base_sort import Base_Sort

class Bubble_Sort(Base_Sort):
    @staticmethod
    def sort(list_to_sort_arg, smallest_first=True):
        # post filter list
        list_to_sort = super(Bubble_Sort,
                             Bubble_Sort).sort(list_to_sort_arg,
                                               smallest_first)

        # passes loop
        while True:
            was_swapped = False
    
            # begin passes at first index
            for pass_start_index in range(len(list_to_sort)-1):
    
                # individual pass
                for i in range(pass_start_index, len(list_to_sort)-1):
                
                    # compare and set flag if needs to be swapped
                    needs_swap = False
                    if smallest_first:
                        if list_to_sort[i] > list_to_sort[i+1]:
                            needs_swap = True
                    else:
                        if list_to_sort[i] < list_to_sort[i+1]:
                            needs_swap = True
    
                    # swap if necessary
                    if needs_swap:
                        tmp = list_to_sort[i]
                        list_to_sort[i] = list_to_sort[i+1]
                        list_to_sort[i+1] = tmp
                        was_swapped = True
            
            # stop passes if no swaps
            if not was_swapped:
                break
    
        # return sorted list
        return list_to_sort
