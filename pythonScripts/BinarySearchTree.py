import time

# This `Node` class is the building block of the Binary Search Tree.
class Node:
    def __init__(self, item):
        self.node = item
        self.left = None
        self.right = None
    
    def addChild(self, child):
        if child == self.node:
            return
        
        if child < self.node:
            if self.left:
                self.left.addChild(child)
            else:
                self.left = Node(child)        
        else:
            if self.right:
                self.right.addChild(child)
            else:
                self.right = Node(child)
    
    def remove(self, item):
        if item < self.node:
            if self.left:
                self.left = self.left.remove(item)
        elif item > self.node:
            if self.right:
                self.right = self.right.remove(item)
        else: 
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            # v = self.left.find_max()
            # self.data = v
            # self.left = self.left.delete(v)
            
            v = self.right.findMin()
            self.node = v
            self.right = self.right.remove(v)
            
        return self
    
    def inOrder(self):
        tree = []
        
        if self.left:
            tree += self.left.inOrder()
            
        tree.append(self.node)
        
        if self.right:
            tree += self.right.inOrder()
        
        return tree
    
    def preOrder(self):
        tree = []
        tree.append(self.node)
        
        if self.left:
            tree += self.left.preOrder()
        
        if self.right:
            tree += self.right.preOrder()
        
        return tree
    
    def postOrder(self):
        tree = []
        
        if self.left:
            tree += self.left.postOrder()
        
        if self.right:
            tree += self.right.postOrder()
            
        tree.append(self.node)
        
        return tree
    
    def findMax(self):
        if self.right is None:
            return self.node
        return self.right.findMax()

    def findMin(self):
        if self.left is None:
            return self.node
        return self.left.findMin()
    
    def calcSum(self):
        leftsum = self.left.calcSum() if self.left else 0
        rightsum = self.right.calcSum() if self.right else 0
        return self.node + leftsum + rightsum
    
    def search(self, item):
        if self.node == item:
            return True
        
        if item < self.node:
            if self.left:
                return self.left.search(item)
            else:
                return False
            
        if item > self.node:
            if self.right:
                return self.right.search(item)
            else:
                return False


# Implementation of the Binary Search Tree.
def BinarySearchTree(nodes):
    root = Node(nodes[0])
    
    for i in range(1, len(nodes)):
        root.addChild(nodes[i])
        
    return root


# Demo program of the operations in a Binary Search Tree.
if __name__ == "__main__":
    nodes = [19, 22, 11, 23, 14, 10, 21, 1, 3, 17, 5, 8, 24, 20, 9, 7, 25, 13, 2, 18, 15, 12, 16, 4, 6]
    bst = BinarySearchTree(nodes)
    print('This is a demo of a binary search tree from ifunanyaScript')
    print('_' * 58)
    time.sleep(1)
    print('\nInorder Traversal')
    print(bst.inOrder())
    print('_' * 91)
    time.sleep(1)
    print('\nPreorder Traversal')
    print(bst.preOrder())
    print('_' * 91)
    time.sleep(1)
    print('\nPostorder Traversal')
    print(bst.postOrder())
    print('_' * 91)
    time.sleep(1)
    print('\nMinimum node')
    print(bst.findMin())
    print('_' * 13)
    time.sleep(1)
    print('\nMaximum node.')
    print(bst.findMax())
    print('_' * 13)
    time.sleep(1)
    print(f'\n25 is in the tree: {bst.search(25)}')
    print('_' * 23)
    time.sleep(1)
    print(f'\n30 is in the tree: {bst.search(30)}')
    print('_' * 24)
    time.sleep(1)
    print(f'\nSum of all the nodes in this tree: {bst.calcSum()}')
    print('_' * 38)
    time.sleep(1)
    print('\nAdding 30 as a node in the tree.....')
    print('_' * 36)
    bst.addChild(30)
    time.sleep(1)
    print(f'\n30 is in the tree: {bst.search(30)}')
    print('_' * 23)
    time.sleep(1)
    print('\nInorder Traversal')
    print(bst.inOrder())
    print('_' * 95)
    time.sleep(1)
    print('\nRemoving 21....')
    bst.remove(21)
    print('_' * 17)
    time.sleep(1)
    print('\nInorder Traversal')
    print(bst.inOrder())
    print('\n')
    print('\n')
    print('\n')
    alphabets = ['w', 'b', 'v', 'x', 's', 'g', 'l', 'k', 'p', 'z', 'm', 'c', 'q', 'f', 
                 'y', 't', 'i', 'e', 'r', 'd', 'u', 'o', 'h', 'n', 'a', 'j']
    alphaTree = BinarySearchTree(alphabets)
    print('Using a binary search tree to sort alphabets of the English Language.')
    print('_' * 69)
    time.sleep(1)
    print('\nBefore sort: ')
    print(alphabets)
    print('_' * 115)
    time.sleep(1)
    print('\nAfter sort: ')
    print(alphaTree.inOrder())


# ifunanyaScript