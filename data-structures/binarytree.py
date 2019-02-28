class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, data):
        # check if this node
        if self.data == data:
            return self
        elif data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        else:
            return None

    def insert(self, data):
        # check if this node
        if self.data == data:
            return False
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = TreeNode(data, self)
        elif data > self.data:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = TreeNode(data, self)
        return True

    def remove(self):
        # no children
        if not self.left and not self.right:
            # check if root
            if not self.parent:
                self.data = None
            elif self.parent.left == self:
                self.parent.left = None
            elif self.parent.right == self:
                self.parent.right = None
        # left only
        elif self.left and not self.right:
            # replace data, break all links to left
            self.data = self.left.data
            self.right = self.left.right
            if self.right:
                self.right.parent = self
            self.left = self.left.left
            if self.left:
                self.left.parent = self
        # right only
        elif self.right and not self.left:
            # replace data, break all links to right
            self.data = self.right.data
            self.left = self.right.left
            if self.left:
                self.left.parent = self
            self.right = self.right.right
            if self.right:
                self.right.parent = self
        # 2 children, replace with successor
        else:
            # get successor node
            succ = self.right.min_node()
            self.data = succ.data
            succ.remove()

    def min_node(self):
        tree_node = self
        while tree_node.left:
            tree_node = tree_node.left
        return tree_node


class BinaryTree:
    def __init__(self, array=[]):
        self.root = None
        self.length = 0
        for data in array:
            self.insert(data)

    def __len__(self):
        return self.length

    def __contains__(self, data):
        return self.find(data) is not None

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return None

    def insert(self, data):
        was_inserted = False
        if self.root:
            was_inserted = self.root.insert(data)
        else:
            self.root = TreeNode(data)
            was_inserted = True

        if was_inserted:
            self.length += 1
        return was_inserted

    def remove(self, data):
        # empty tree
        if not self.root:
            return False

        # traverse tree and look for data
        node = self.root
        while node:
            # check if this node has data
            if data == node.data:
                # remove this node
                node.remove()
                # if removed the root with no children,
                # the root node will set itself to None
                if node == self.root and node.data is None:
                    self.root = None
                self.length -= 1
                return True

            # go to next node
            if data > node.data:
                node = node.right
            else:
                node = node.left

        # reached a None node, meaning not in tree
        return False
