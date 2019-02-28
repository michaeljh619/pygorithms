from binarytree import TreeNode, BinaryTree

import pytest


def pytest_generate_tests(metafunc):
    # lists to create binary trees
    test_lists = [
        [],
        [13],
        [15, 17],
        [201, 735, 6]
    ]
    if 'test_list' in metafunc.fixturenames:
        metafunc.parametrize('test_list', test_lists)


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
