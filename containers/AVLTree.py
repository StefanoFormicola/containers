'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        elif AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        else:
            lefthandside = AVLTree._is_avl_satisfied(node.left)
            if lefthandside:
                righthandside = AVLTree._is_avl_satisfied(node.right)
                if righthandside:
                    return True
                else:
                    return False
            else:
                return False

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None:
            return node
        elif node.right is None:
            return node
        newrightchild = node.right.value
        newroot = Node(newrightchild)
        rightchildchild = node.right.right
        newroot.right = rightchildchild
        nodevalue = node.value
        newleftchild = Node(nodevalue)
        oldleftchild = node.left
        newleftchild.left = oldleftchild
        rightleftchild = node.right.left
        newleftchild.right = rightleftchild
        newroot.left = newleftchild
        return newroot

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None:
            return node
        elif node.left is None:
            return node
        newleftchild = node.left.value
        newroot = Node(newleftchild)
        leftchildchild = node.left.left
        newroot.left = leftchildchild
        nodevalue = node.value
        newrightchild = Node(nodevalue)
        oldrightchild = node.right
        newrightchild.right = oldrightchild
        leftleftchild = node.left.right
        newrightchild.left = leftleftchild
        newroot.right = newrightchild
        return newroot

    def insert(self, value):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if not self.root:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if node is None:
            node = Node(value)
            return node
        else:
            if value < node.value:
                leftchild = AVLTree._insert(node.left, value)
                node.left = leftchild
            else:
                rightchild = AVLTree._insert(node.right, value)
                node.right = rightchild
        tree = AVLTree()
        tree.root = node
        rebalanced = tree._rebalance()
        return rebalanced

    def _rebalance(self):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        node = self.root
        if AVLTree._balance_factor(node) > 1:
            childbalance = AVLTree._balance_factor(node.left)
            if childbalance >= 0:
                noderotation = AVLTree._right_rotate(node)
                node = noderotation
            else:
                leftrotation = AVLTree._left_rotate(node.left)
                node.left = leftrotation
                noderotation = AVLTree._right_rotate(node)
                node = noderotation
        elif AVLTree._balance_factor(node) < -1:
            childbalance = AVLTree._balance_factor(node.right)
            if childbalance <= 0:
                noderotation = AVLTree._left_rotate(node)
                node = noderotation
            else:
                rightrotation = AVLTree._right_rotate(node.right)
                node.right = rightrotation
                noderotation = AVLTree._left_rotate(node)
                node = noderotation
        return node
