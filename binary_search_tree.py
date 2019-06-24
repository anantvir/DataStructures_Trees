"""Author - Anantvir Singh, concept reference:= Data Structures in C by Seymour Lipschutz"""
class BinarySearchTree:

    # Nested class because it is only locally required inside BinarySearchTree class
    class Node:
        def __init__(self,info,parent =None,left_child = None,right_child = None):
            self.info = info
            self.parent = parent
            self.left_child = left_child
            self.right_child = right_child
        
    def __init__(self):
        self.root = None
        self.size = 0
        self.CURR_PTR = None
    
    def find(self,item):
        if self.root is None:                           # Tree empty ?
            LOCATION = None
            PARENT = None
            return LOCATION,PARENT
        if item == self.root.info:                      # Item at root ?
            LOCATION = self.root
            PARENT = None
            return LOCATION
        self.CURR_PTR = self.root
        if item < self.root.info:                       # Item less than root ? move to left subtree
            self.CURR_PTR = self.CURR_PTR.left_child
            SAVE = self.root
        else:                                           
            self.CURR_PTR = self.CURR_PTR.right_child   # Item greater than root ? move to right subtree
            SAVE = self.root
        while self.CURR_PTR is not None:
            if item == self.CURR_PTR.info:
                LOCATION = self.CURR_PTR
                PARENT = SAVE 
            if item < self.CURR_PTR.info:
                SAVE = self.CURR_PTR
                self.CURR_PTR = self.CURR_PTR.left_child
            else:
                SAVE = self.CURR_PTR
                self.CURR_PTR = self.CURR_PTR.right_child
        LOCATION = None
        PARENT = SAVE
        return LOCATION,PARENT
    
    def insertBST(self,item):
        LOC_PAR = self.find(item)                                   # search if item already exists in tree ?
        if LOC_PAR[0] is not None:
            print('Node already exists at location :',LOC_PAR[0])   # If it exists
        newNode = self.Node(item)                                   # create new node if does not exist
        if LOC_PAR[1] is None:                                      # make it root is no root exists already
            self.root = newNode
        elif item < LOC_PAR[1].info:                                # insert item at left or right as per BST logic
            LOC_PAR[1].left_child = newNode
        else:
            LOC_PAR[1].right_child = newNode
        return newNode

t = BinarySearchTree()
t.insertBST(5)
t.insertBST(8)
t.insertBST(2)
t.insertBST(98)




        