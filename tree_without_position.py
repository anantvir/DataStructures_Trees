"""Generic Linked Tree where children are stored in any iterable"""

class Node:
    def __init__(self,info,parent =None, children = None):
        self.info = info
        self.parent = parent
        self.children = []

class Tree:
    def __init__(self):
        self.root= None
        self.size = 0
    
    def add_root(self,item):
        if self.root is not None:
            raise ValueError('Root already exists')
        newNode = Node(item)
        self.root = newNode
        self.size += 1
        return newNode
    
    def add_child(self,item,prnt):
        if type(prnt) is Node:
            newNode = Node(item,prnt)
            prnt.children.append(newNode)
        return newNode

    def preorder(self,node):
        print('Current node is :',node.info)        # Process node as per requirement
        
        for child in node.children:
            self.preorder(child)

    def postorder(self,node):

        for child in node.children:
            self.postorder(child)

        print('Current node is :',node.info)        # Process node as per requirement

t = Tree()
root = t.add_root(5)
n1 = t.add_child(3,root)
t.add_child(21, n1)
t.add_child(47, n1)

t.add_child(8, root)
t.preorder(root)
t.postorder(root)
