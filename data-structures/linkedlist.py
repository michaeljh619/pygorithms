class Link:
    def __init__(self, data):
        self.data = data
        self.next_link = None


class LinkedList:
    def __init__(self, array=[]):
        self.first = None
        self.length = len(array)

        # create first link
        link = None
        if len(array) > 0:
            link = Link(array[0])
            self.first = link

        # create remaining links
        last_link = link
        for data in array[1:]:
            new_link = Link(data)
            last_link.next_link = new_link
            last_link = new_link

    def __iter__(self):
        self.iter_link = self.first
        return self

    def __next__(self):
        if self.iter_link:
            data = self.iter_link.data
            self.iter_link = self.iter_link.next_link
            return data
        else:
            raise StopIteration

    def next(self):
        return self.__next__()

    def __len__(self):
        return self.length

    def __error_check_index(self, index):
        # error checking
        if index < 0 or index >= len(self):
            raise IndexError(str(index) + " is out of bounds of range "
                             + "0 and " + str(len(self)))

    def __search_link_index(self, index):
        self.__error_check_index(index)

        # search for index
        link = self.first
        search_index = 0
        while search_index < index:
            link = link.next_link
            search_index += 1

        # return link at index
        return link

    def __search_link_data(self, data):
        link = self.first
        while link:
            # if we reach the index, break
            if link.data == data:
                break
            # increment
            link = link.next_link
        return link

    def __contains__(self, data):
        return self.__search_link_data(data) is not None

    def __setitem__(self, index, data):
        self.__search_link_index(index).data = data

    def __getitem__(self, index):
        return self.__search_link_index(index).data

    def insert(self, index, data):
        # error check everything except the index at the end of the
        # linked list, since inserting there is actually valid
        if index != self.length:
            self.__error_check_index(index)

        # search for the link index directly before where you want
        # to insert this new link
        prev_link = None
        try:
            prev_link = self.__search_link_index(index - 1)
        except IndexError:
            pass

        # create new link to insert
        new_link = Link(data)

        # insert at start of list
        if prev_link is None:
            # set aside first link for now
            original_first_link = self.first
            # make original first link the new link's next
            self.first = new_link
            self.first.next_link = original_first_link
        # all other inserts, works at end of list too!
        else:
            # prev_link's next will become the new link's next
            next_link = prev_link.next_link
            # insert in between prev and next links
            prev_link.next_link = new_link
            new_link.next_link = next_link

        # update length and return
        self.length += 1
        return new_link

    def append(self, data):
        return self.insert(len(self), data)

    def remove(self, index):
        self.__error_check_index(index)

        # search for the link index directly before where you want
        # to remove
        prev_link = None
        try:
            prev_link = self.__search_link_index(index - 1)
        except IndexError:
            pass

        # remove first element
        if prev_link is None:
            self.first = self.first.next_link
        # remove some other element
        else:
            link_to_remove = prev_link.next_link
            next_link = link_to_remove.next_link
            prev_link.next_link = next_link

        # update length
        self.length -= 1
