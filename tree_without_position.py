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
        return prnt.children,newNode.info

t = Tree()
root = t.add_root(5)
print(t.add_child(3,root))

print(t.add_child(8, root))
