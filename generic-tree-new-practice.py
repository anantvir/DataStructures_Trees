class Node:
    def __init__(self, info, parent = None):
        self.info = info
        self.parent = parent
        self.children = []          # list to store 'n' number of children
    
    def node_is_empty(self):
        return len(self.children) == 0

class GenericTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def add_root(self, data):
        if self.root != None:
            raise Exception("Root already exists !")
        else:
            newNode = Node(data)
            self.root = newNode
            self.size += 1
            return newNode
    
    def add_child(self, data, parent):
        if type(parent) == Node:
            newNode = Node(data)
            parent.children.append(newNode)
            self.size += 1
        return newNode
    

t = GenericTree()
root = t.add_root(1)
n1 = t.add_child(2,root)
n2 = t.add_child(3,root)
n3 = t.add_child(4,n1)
n4 = t.add_child(5,n1)

print("Testing ....")
