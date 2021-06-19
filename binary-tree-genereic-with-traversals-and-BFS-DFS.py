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
            if oldNode.parent.left_child == oldNode:        # check if oldNode is left or right child of parent. Then accordingly make the same parent for newNode
                oldNode.parent.left_child = newNode
            if oldNode.parent.right_child == oldNode:
                oldNode.parent.right_child = newNode 
            oldNode.parent = None
            oldNode.left_child = None
            oldNode.right_child = None
            print("Old Node replaced successfully !")

    def children(self, node):
        temp = []
        if node.left_child != None:
            temp.append(node.left_child)
        if node.right_child != None:
            temp.append(node.right_child)
        return temp

    # Visit the root, then starting from leftmost child, make leftmost child as root and recursively call preorder i.e recursively visit children
    # starting from leftmost child by making it as root until we reach the leftmost leaf, then it comes out of 
    # recursion stack and proceeds to right children 

    def preorder(self, root):
        # Perform visit action
        print(root.data)
        for child in self.children(root):
            self.preorder(child)        # First visit child, then recursively traverse subtree rooted at child
    
    # left-right-root i.e root traversed at last, so go to leftmost leaf first, then visit it, then visit right subtree
    # and then visit the root

    def postorder(self, root):
        for child in self.children(root):
            self.postorder(child)       # Recursively traverse subtree rooted at at child and then visit the child
        # Perform visit action
        print(root.data) 
    
    #
    def inorder(self, root):
        if root.left_child:
            self.inorder(root.left_child)
        # visit
        print(root.data)
        if root.right_child:
            self.inorder(root.right_child)

    # Traverse each level of tree breadth wise using Queue
    def BFS(self):

        return
    
    def DFS(self):
        return


t = LinkedBinaryTree()
root = t.add_root(1)

n1 = t.add_left_child(2, root)
n2 = t.add_right_child(3, root)

n3 = t.add_left_child(4, n1)
n4 = t.add_right_child(5, n1)

#t.replace(n1, n2)

t.preorder(root)
t.postorder(root)
t.inorder(root)
print("Finished")


