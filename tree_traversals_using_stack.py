class StackEmpty(Exception):
    pass

class StackUsingList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0
    
    def push(self,value):
        self.data.append(value)
    
    def top(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            raise StackEmpty('Stack is Empty !')
    
    def pop(self):
        if not self.isEmpty():
            return self.data.pop()     # use inbuilt python method
        else:
            raise StackEmpty('Stack is Empty !')

class BinaryTree:
    
    class Node:
        def __init__(self,info,parent = None,left_child = None,right_child = None):
            self.info = info
            self.parent = parent
            self.left_child = left_child
            self.right_child = right_child

    def __init__(self):
        self.root = None
        self.size = 0
        self.current_ptr = None
    
    def tree_is_Empty(self):
        return self.size ==0
    
    def add_root(self,item):
        if self.root is not None:
            raise ValueError('Root already exists !')
        newNode = self.Node(item)
        self.root = newNode
        self.size += 1
        return newNode
    
    def add_left_child(self,item,parent):
        if parent.left_child is not None:
            raise ValueError('Left child is not Null !')
        newNode = self.Node(item,parent)
        parent.left_child = newNode
        self.size += 1
        return newNode
    def add_right_child(self,item,parent):
        if parent.right_child is not None:
            raise ValueError('Right child is not Null !')
        newNode = self.Node(item,parent)
        parent.right_child = newNode
        self.size += 1
        return newNode

    def preorder(self,node):
        self.current_ptr = node
        stack = StackUsingList()
        stack.push(None)

        while(self.current_ptr != None):

            print('Value of node :',self.current_ptr.info)
            
            if self.current_ptr.right_child is not None:
                stack.push(self.current_ptr.right_child)
            if self.current_ptr.left_child is not None:
                self.current_ptr = self.current_ptr.left_child
            else:
                self.current_ptr = stack.pop()
            


t= BinaryTree()
root = t.add_root(5)
c1 = t.add_left_child(1,root)
c2 = t.add_right_child(8,root)
cc1 = t.add_left_child(22,c1)
cc2 = t.add_right_child(33,c1)
t.preorder(root)


