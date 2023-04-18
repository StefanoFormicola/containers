'''
This file implements the Binary Search Tree data structure.
than the functions in the BinaryTree file.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):

    def __init__(self, xs=None):
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __iter__(self):
        second = self.root
        while second:
            if not second.left:
                yield second.value
                second = second.right
            else:
                first = second.left
                while first.right and first.right != second:
                    first = first.right

                if not first.right:
                    first.right = second
                    second = second.left
                else:
                    first.right = None
                    yield second.value
                    second = second.right

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_bst_satisfied(self):
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        The current implementation has a bug:
        HINT:
        Use the _find_smallest and _find_largest
        functions to fix the bug.
        '''
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        Inserts value into the BST.
        FIXME:
        Implement this function.
        HINT:
        Create a staticmethod helper function
        '''
        '''
        if self.root:
            BST._insert(self.root, value)
        else:
            self.root = Node(value)
            '''
        if not self.root:
            self.root = Node(value)
        else:
            BST._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if value > node.value:
            if node.right:
                BST._insert(node.right, value)
            else:
                node.right = Node(value)
        elif value < node.value:
            if node.left:
                BST._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            pass

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        HINT:
        Repeatedly call the insert method.
        '''
        for x in xs:
            self.insert(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        '''
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return BST._find(value, node.left)
        return BST._find(value, node.right)
'''
        live = node
        while live is not None:
            if value == live.value:
                return True
            elif value > live.value:
                live = live.right
            else:
                live = live.left

        return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
        This is a helper function for find_smallest and not intended to be called directly by the user.
        '''
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.
        FIXME:
        Implement this function.
        HINT:
        Follow the pattern of the _find_smallest function.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        '''
        This is a helper function for find_smallest and
        not intended to be called directly by user
        '''
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        self.root = BST._remove(self.root, value)

    @staticmethod
    def _remove(node, value):
        if node is None:
            return None
        elif value != node.value:
            if value < node.value:
                node.left = BST._remove(node.left, value)
            else:
                node.right = BST._remove(node.right, value)
            return node
        elif node.left is None and node.right is None:
            return None
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        minimun = node.right
        while minimun.left is not None:
            minimun = minimun.left
        minimun = minimun.value
        node.value = minimun
        node.right = BST._remove(node.right, minimun)
        return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.
        FIXME:
        Implement this function.
        HINT:
        See the insert_list function.
        '''
        for x in xs:
            self.remove(x)
