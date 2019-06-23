# Author- Anantvir Singh------------Reference - DS and Algorithms by Michael T. Goodrich
# This implementation uses the concept of positional linked lists. We wrap a node in a Position object. _validate utility
# method is provided which checks validity of passed position when unwrapping it and returns the node associated with that position

""" Binary Tree can also be implemented by using a pointer which references the node being currently processed"""

class LinkedBinaryTree:

    class Node:
        def __init__(self,item,parent =None,left_child = None,right_child = None):
            self._item = item
            self._parent = parent
            self._left_child = left_child
            self._right_child = right_child
    
    class Position:
        def __init__(self,container, node):     # Container--> it holds a reference to current linked binary tree. So it helps keep track of nodes which belong to this particlar tree. If user passes a position which is not an instance of LinkedBinaryTree or this particular instance of LnkedBinaryTree, then we can detect it through this container
            self._container = container
            self._node = node
        
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        
        def item(self):
            return self._node._item

    def _validate(self,position):
        
        """Validate the position passed by user. Raise exception if its not an instance of of Position class or if its container doesnt hold reference to current tree"""
        
        if not isinstance(position,self.Position):
            raise TypeError('Given position is not and instance of Position class !')
        if position._container is not self:
            raise TypeError('Given positions container is not of type Position !')
        if position._node._parent is position._node:    # Convention for deprecated nodes
            raise ValueError('Parent of this node is same as itself !')
        return position._node
    
    def _make_position_object(self,node): 
        """ Return Position instance for the node which is passed by user """      
        if node is None:
            return False
        else:
            return self.Position(self,node)
    
    #-----------------Constructor for LinkedBinaryTree class------------------------
    def __init__(self):
        self._root = None
        self._size = 0

    #---------------Public methods(accessors)---------------------------------------
    def __len__(self):
        return self._size
    
    def root(self):
        """returns the position of root. returns None if no root"""
        return self._make_position_object(self._root)
    
    def parent(self,position):
        """returns position of parent of 'position' passed by user"""
        node = self._validate(position)
        return self._make_position_object(node)
    
    def left(self,position):
        node = self._validate(position)
        return self._make_position_object(node)
    
    def right(self,position):
        node = self._validate(position)
        return self._make_position_object(node)
    
    def number_of_children(self, position):
        node = self._validate(position)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count
    
    def add_root(self,item):
        if self._root is not None:
            raise ValueError('Root already exists !')
        newNode = self.Node(item)
        self._root = newNode
        self._size += 1
        return self._make_position_object(self._root)
    
    def _add_left_child(self,item,position):
        node = self._validate(position)     # get node from given position
        if node._left_child is not None:
            raise ValueError('Left child for this given position already exists !')
        node._left_child = self.Node(item,node)
        self._size += 1
        return self._make_position_object(node._left_child)
    
    def add_right_child(self,item,position):
        node = self._validate(position)     # get node from given position
        if node._right_child is not None:
            raise ValueError('Right child for this given position already exists !')
        newNode = self.Node(item,node)
        node._right_child = newNode
        self._size += 1
        return self._make_position_object(node._right_child)

    def replace(self,position,item):
        """Replace the value at given position with item passed by the user. Also, return the old value stored in temp"""
        node = self._validate(position)     # first get the node at the given position and then manipulate it
        if node.item is not None:
            temp = node.item
            node.item = item
        return temp

t= LinkedBinaryTree()
p = t.add_root(2)       # Testing
t._add_left_child(5,p)  # pass positions while adding new children
t.add_right_child(6,p)  
