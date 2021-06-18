class LinkedBinaryTree:
    class LinkedBinaryTreeNode:
        def __init__(self, data, left_child = None, right_child = None, parent = None):
            self.data = data
            self.left_child = left_child
            self.right_child = right_child
            self.parent = parent
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def add_root(self, data):
        if self.root == None:
            newNode = self.LinkedBinaryTreeNode(data)
            self.root = newNode
            self.size += 1
            return newNode
        else:
            raise Exception("Root already exists !")
    
    def add_left_child(self, data, parent):
        if not isinstance(parent, self.LinkedBinaryTreeNode):
            raise Exception("Parent is not of type LinkedBinaryNode !")
        else:
            if parent.left_child == None:
                # add new left child
                newNode = self.LinkedBinaryTreeNode(data)
                parent.left_child = newNode
                newNode.parent = parent
                self.size += 1
                return newNode
            else:
                raise Exception("Left child of this parent already exists")
            
    def add_right_child(self, data, parent):
        if not isinstance(parent, self.LinkedBinaryTreeNode):
            raise Exception("Parent is not of type LinkedBinaryNode !")
        else:
            if parent.right_child == None:
                # add new left child
                newNode = self.LinkedBinaryTreeNode(data)
                parent.right_child = newNode
                newNode.parent = parent
                self.size += 1
                return newNode
            else:
                raise Exception("Left child of this parent already exists")

    def replace(self, oldNode, newNode):
        if not isinstance(newNode, self.LinkedBinaryTreeNode):
            raise Exception("newNode is not of type LinkedBinaryTreeNode !")
        else:
            newNode.parent = oldNode.parent
            newNode.left_child = oldNode.left_child
            newNode.right_child = oldNode.right_child
            if oldNode.parent.left_child == oldNode:
                oldNode.parent.left_child = newNode
            if oldNode.parent.right_child == oldNode:
                oldNode.parent.right_child = newNode 
            oldNode.parent = None
            oldNode.left_child = None
            oldNode.right_child = None
            print("Old Node replaced successfully !")
    

t = LinkedBinaryTree()
root = t.add_root(1)

n1 = t.add_left_child(2, root)
n2 = t.add_right_child(3, root)

n3 = t.add_left_child(4, n1)
n4 = t.add_right_child(5, n1)

t.replace(n1, n2)

print("Hello")


