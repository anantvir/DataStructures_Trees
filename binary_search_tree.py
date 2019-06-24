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
    
    def findBST(self,item):
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
                return LOCATION,PARENT 
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
        LOC_PAR = self.findBST(item)                                # search if item already exists in tree ?
        if LOC_PAR[0] is not None:
            print('Node already exists at location :',LOC_PAR[0])   # If it exists, print it
        newNode = self.Node(item)                                   # Else, create new node if does not exist
        if LOC_PAR[1] is None:                                      # make it root is no root exists already
            self.root = newNode
        elif item < LOC_PAR[1].info:                                # insert item at left or right as per BST logic
            LOC_PAR[1].left_child = newNode
        else:
            LOC_PAR[1].right_child = newNode
        return newNode

    """This function deletes a node N where N has either no children or 1 child. Case for 2 children is handeled by next function"""
    def del_case_1_2(self,location,parent):
        # location - location of node to be deleted
        # par - parent of node to be deleted
        # child - child of node to be deleted. child = None if node has node children
        if location.left_child is None and location.right_child is None:
            child = None
        elif location.left_child is not None:
            child = location.left_child
        else:
            child = location.right_child
        if parent is not None:
            if location == parent.left_child:
                parent.left_child = child
            else:
                parent.right_child = child
        else:
            self.root = child
        return child
    
    """This function deletes a node N if it has 2 children"""
    def del_case_3(self,location,parent):
        # succ = inorder successor of node N
        # parsucc = parent of inorder successor of node N
        # -------------------find succ and parsucc---------------
        self.CURR_PTR = location.right_child
        while self.CURR_PTR.left_child is not None:     # find inorder successor
            save = self.CURR_PTR
            self.CURR_PTR = self.CURR_PTR.left_child 
        succ = self.CURR_PTR                            # inorder successor
        parsucc = save                                  # parent of inorder successor
        self.del_case_1_2(succ,parsucc)
        if parent is not None:
            if location == parent.left_child:
                parent.left_child = succ
            else:
                parent.right_child = succ
        else:
            self.root = succ
        succ.left_child = location.left_child
        succ.right_child = location.right_child
        return location
    
    def deleteBST(self,root,item):
        location= self.findBST(item)[0] 
        parent = self.findBST(item)[1]
        if location is None:
            print('Item is not in the tree. Cannot be deleted !')
        if location.right_child is not None and location.left_child is not None:
            self.del_case_3(location,parent)
        else:
            self.del_case_1_2(location,parent)
        


t = BinarySearchTree()
t.insertBST(5)
t.insertBST(8)
t.insertBST(2)
t.insertBST(98)
print(t.findBST(2))
print('hello')




        