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

    def __search_link(self, data):
        link = self.first
        while link:
            # if we reach the index, break
            if link.data == data:
                break
            # increment
            link = link.next_link
        return link

    def insert(self, index, data):
        # error checking
        if index < 0 or index > len(self):
            raise IndexError(str(index) + " is out of bounds of range "
                             + "0 and " + str(len(self)))

        # search through links and get the link that the new link
        # will become the next link of
        search_index = 0
        prev_link = None
        link = self.first
        while link:
            # if we reach the index, break
            if search_index == index:
                break
            # get current link at index
            prev_link = link
            # increment
            link = link.next_link
            search_index += 1

        # create new link to insert
        new_link = Link(data)

        # insert at start of list
        if index == 0:
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
