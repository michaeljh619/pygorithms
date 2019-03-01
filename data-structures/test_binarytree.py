from binarytree import TreeNode, BinaryTree

import pytest


def pytest_generate_tests(metafunc):
    # TreeNode lists to create
    node_lists = [
        [1],
        [1, 2],
        [2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [2, 1, 3],
        [2, 3, 1],
        [5, 12, 3, 1, 4, 10, 15]
    ]
    if 'node_list' in metafunc.fixturenames:
        metafunc.parametrize('node_list', node_lists)

    # lists to create binary trees
    test_lists = [
        [],
        [13],
        [15, 17],
        [201, 735, 6]
    ]
    if 'test_list' in metafunc.fixturenames:
        metafunc.parametrize('test_list', test_lists)


def test_TreeNode_constructor():
    # create nodes
    node = TreeNode(17)
    child_node = TreeNode(10, node)

    # tests
    assert node.data == 17
    assert child_node.data == 10
    assert child_node.parent == node


def test_TreeNode_insert():
    # create root
    root = TreeNode(10)

    # test children
    assert root.left is None
    assert root.right is None

    # insert left
    root.insert(1)
    assert root.left is not None
    assert root.left.data == 1
    assert root.left.parent == root

    # insert right
    root.insert(20)
    assert root.right is not None
    assert root.right.data == 20
    assert root.right.parent == root


def create_nodes_from_list(data_list):
    # create root
    root = None
    if len(data_list) > 0:
        root = TreeNode(data_list[0])

        # add children
        if len(data_list) > 1:
            for data in data_list[1:]:
                root.insert(data)

    # return root
    return root


def test_TreeNode_find(node_list):
    root = create_nodes_from_list(node_list)
    for data in node_list:
        node = root.find(data)
        assert node is not None
        assert node.data == data


def TreeNode_remove(node_list, remove_order, root):
    for data in remove_order:
        # node
        node = root.find(data)
        # linked nodes
        parent = node.parent
        left = node.left
        right = node.right

        # last node
        if not parent and not left and not right:
            node.remove()
            assert node.data is None
        # other nodes still left
        else:
            # remove
            node.remove()
            assert root.find(data) is None
            # check linked nodes
            if parent:
                assert root.find(parent.data) is not None
            if left:
                assert root.find(left.data) is not None
            if right:
                assert root.find(right.data) is not None


def test_TreeNode_remove(node_list):
    for i in range(len(node_list)):
        front_half = node_list[i:]
        back_half = node_list[:i]
        back_half = back_half[::-1]
        remove_order = front_half + back_half
        root = create_nodes_from_list(node_list)
        TreeNode_remove(node_list, remove_order, root)


def test_default_constructor():
    binary_tree = BinaryTree()
    assert len(binary_tree) == 0
    assert binary_tree.root is None
    assert binary_tree.find(5) is None


def test_creation_through_constructor(test_list):
    # create binary tree
    binary_tree = BinaryTree(test_list)
    assert len(binary_tree) == len(test_list)
    # assert all data is there
    for data in test_list:
        assert binary_tree.find(data) is not None


def test_creation_through_insert(test_list):
    # create binary trees
    binary_tree = BinaryTree()
    # insertions
    length = 0
    for data in test_list:
        binary_tree.insert(data)
        length += 1
        assert len(binary_tree) == length
    # assert all data is there
    for data in test_list:
        assert binary_tree.find(data) is not None


def test_contains(test_list):
    binary_tree = BinaryTree(test_list)
    for data in test_list:
        assert data in binary_tree


def test_tree_shape():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(1)
    bt.insert(9)

    # check shape
    assert bt.root.data == 5
    assert bt.root.left.data == 1
    assert bt.root.right.data == 9


def test_remove_not_in_tree():
    # empty tree remove
    bt = BinaryTree()
    assert bt.remove(0) is False
    # non existent remove
    bt.insert(5)
    assert bt.remove(0) is False


def test_remove_no_children():
    bt = BinaryTree()

    # remove of root
    bt.insert(5)
    assert bt.remove(5) is True
    assert 5 not in bt
    assert bt.root is None
    assert len(bt) == 0

    # more complicated tree
    bt.insert(5)
    bt.insert(1)
    bt.insert(9)
    # remove left child of root
    assert bt.remove(1) is True
    assert 1 not in bt
    assert bt.root.data == 5
    assert bt.root.right.data == 9
    assert bt.root.left is None
    # remove right child of root
    assert bt.remove(9) is True
    assert 9 not in bt
    assert bt.root.data == 5
    assert bt.root.right is None
    assert bt.root.left is None


def test_remove_one_right_child():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(9)

    # remove of root with one left child
    assert bt.remove(5) is True
    assert 5 not in bt
    assert bt.root.data == 9
    assert len(bt) == 1


def test_remove_one_left_child():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(1)

    # remove of root with one left child
    assert bt.remove(5) is True
    assert 5 not in bt
    assert bt.root.data == 1
    assert len(bt) == 1


def test_remove_two_children():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(1)
    bt.insert(9)

    # remove root
    assert bt.remove(5) is True
    assert bt.root.data == 9
    assert 5 not in bt
    assert len(bt) == 2
    assert bt.root.left.data == 1


def test_remove_two_children_succ_child():
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(1)
    bt.insert(9)
    bt.insert(10)

    # remove root
    assert bt.remove(5) is True
    assert bt.root.data == 9
    assert 5 not in bt
    assert len(bt) == 3
    assert bt.root.left.data == 1
    assert bt.root.right.data == 10
