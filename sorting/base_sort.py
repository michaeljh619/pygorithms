class BaseSort(object):
    @staticmethod
    def sort(list_to_sort, smallest_first):
        # make sure unsorted_list is a list
        if not isinstance(list_to_sort, list):
            raise TypeError("'list_to_sort' arg must be a list!")

        # make shallow copy of list
        return list_to_sort[:]
