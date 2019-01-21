# import base class
from base_sort import Base_Sort


class Insertion_Sort(Base_Sort):
    @staticmethod
    def sort(list_to_sort_arg, smallest_first=True):
        # post filter list
        list_to_sort = super(Insertion_Sort,
                             Insertion_Sort).sort(list_to_sort_arg,
                                                  smallest_first)

        # begin at second index and insert working backwards
        for i_insertee in range(1, len(list_to_sort)):

            # work backwards to find spot to insert
            i_insert_search = i_insertee-1
            insertee = list_to_sort[i_insertee]
            while i_insert_search >= 0:
                # compare and set flag if swap is needed
                needs_swap = False
                current_element = list_to_sort[i_insert_search]
                if smallest_first and insertee < current_element:
                    needs_swap = True
                elif not smallest_first and insertee > current_element:
                    needs_swap = True

                # if needs swap, then swap
                if needs_swap:
                    list_to_sort[i_insert_search+1] = current_element
                    list_to_sort[i_insert_search] = insertee
                # else break, since the insertee is in the right spot
                else:
                    break
                # decrement to keep searching backwards
                i_insert_search -= 1

        # return sorted list
        return list_to_sort
