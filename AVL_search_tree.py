class AVLSearchTree:

    class Node:
        def __init__(self,info,parent =None,left_child = None,right_child = None):
            self.info = info
            self.parent = parent
            self.left_child = left_child
            self.right_child = right_child
    
    def __init__(self):
        self.root = None
        self.size = 0
        self.current_ptr = None
    
    def getBalanceFactor(self,node):
        left_edge_count = 0
        self.current_ptr = node
        while self.current_ptr is not None:
            left_edge_count += 1
            self.current_ptr = self.current_ptr.left_child
        right_edge_count = 0
        self.current_ptr = node
        while self.current_ptr is not None:
            right_edge_count += 1
            self.current_ptr = self.current_ptr.right_child
        return left_edge_count - right_edge_count
    
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

    def RR_rotation(self,node):
        temp =self.root
        temp.right_child = None
        if node.left_child is not None:
            temp_left_node = node.left_child
            node.left_child = None
        node.parent = None
        self.root = node
        self.root.left_child = temp
        self.root.left_child.right_child = temp_left_node
        bf = self.getBalanceFactor(self.root)               # should be zero in this case after RR rotation
        return bf
        

t = AVLSearchTree()
t.insertBST(5)
t.insertBST(2)
x = t.insertBST(8)
t.insertBST(7)
t.insertBST(98)
t.insertBST(200)
t.RR_rotation(x)
print(t.getBalanceFactor(x))

        
