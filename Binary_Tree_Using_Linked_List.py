class BinaryTree:
    class Node:
        def __init__(self,info):
            self.info = info
            self.left_child = None
            self.right_child = None
    
    def __init__(self):
        self.root = None
        self.current_ptr = None
        self.size = 0
    
    def insert(self,info):
        if self.root == None:
            newNode = self.Node(info)
            self.root = newNode
            self.size += 1
        else:
            