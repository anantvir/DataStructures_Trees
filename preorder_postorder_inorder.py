"""Main idea behind traversals is when the root is processed. preorder - process root at 
first, inorder- process left subtree, then root and then right subtree, postorder - process root at last"""

class LinkedTree:
    class Node:
        def __init__(self,info,parent = None,children = None):
            self.info = info
            self.parent = parent
            self.children = []
    
    class Position:
        def __init__(self,container,node):
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
    
    def children(self,position):
        node = self._validate(position)
        temp = []
        for child in node.children:
            temp.append(self._make_position_object(child))
        return temp
        
    
    #-----------------Constructor for LinkedBinaryTree class------------------------
    def __init__(self):
        self._root = None
        self._size = 0

    """Use generator to make it more efficient"""
    def preorder(self,position): # We can make this method private and call it from another public function

        print('Position of current node :',position)    # Process the node anyway the user wants

        for child in self.children(position):           # Loop through the children
            self.preorder(child)
    
    def postorder(self,position):

        for child in self.children(position):           # Loop through the children
            self.postorder(child) 

        print('Position of current node :',position)
 

        
    


