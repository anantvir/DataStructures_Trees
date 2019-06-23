"""Author - Anantvir Singh, concept reference:= Data Structures in C by Seymour Lipschutz"""

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
            self.hasBeenProcessed = False

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
        stack.push(None)                                        # Push Null as 1st element of stack to end the while loop

        while(self.current_ptr != None):
            print('Value of node :',self.current_ptr.info)      # Process the node
            if self.current_ptr.right_child is not None:
                stack.push(self.current_ptr.right_child)        # Push right child onto stack
            if self.current_ptr.left_child is not None:
                self.current_ptr = self.current_ptr.left_child  # Move to left child
            else:
                self.current_ptr = stack.pop()                  # pop from stack to process right children
    
    def inorder(self,node):
        self.current_ptr = node
        stack = StackUsingList()
        stack.push(None)
        while(self.current_ptr is not None):
            stack.push(self.current_ptr)    
            self.current_ptr = self.current_ptr.left_child
        self.current_ptr = stack.pop()
        while(self.current_ptr != None):
            print("Value of node :",self.current_ptr.info)      # Process the node
            if self.current_ptr.right_child is not None:
                self.current_ptr = self.current_ptr.right_child # Move current pointer to right is right child exists
                while(self.current_ptr != None):                # Push left children on stack again 
                    stack.push(self.current_ptr)
                    if self.current_ptr.left_child is not None:
                        self.current_ptr = self.current_ptr.left_child
                    else:
                        self.current_ptr = None                 # Make current pointer Null explicitly to exit while loop of no more left children
                self.current_ptr = stack.pop()                  # Again pop and make top of stack as current pointer
            else:
                self.current_ptr = stack.pop()
    
    def postorder(self,node):
        self.current_ptr = node
        stack = StackUsingList()
        stack.push(None)
        while(self.current_ptr is not None):        # Push all left children on stack
            stack.push(self.current_ptr)
            self.current_ptr = self.current_ptr.left_child
        self.current_ptr = stack.top()              # current now points to top of stack
        while(self.current_ptr is not None):
            
            if self.current_ptr.right_child is not None and not self.current_ptr.hasBeenProcessed:
                self.current_ptr.hasBeenProcessed = True    # Make a new helper flag or else if will convert to infinite loop in second iteration as current pointer will always have a right child.
                self.current_ptr = self.current_ptr.right_child
                
                while(self.current_ptr is not None):    # Again push all left children on stack
                    stack.push(self.current_ptr)
                    self.current_ptr = self.current_ptr.left_child
                self.current_ptr = stack.top()          # set current pointer
            else:
                self.current_ptr = stack.pop()          # If no right child, then just pop and process the node
                print('Value of node :',self.current_ptr.info)
            self.current_ptr = stack.top()
            


t= BinaryTree()
root = t.add_root(5)
c1 = t.add_left_child(1,root)
c2 = t.add_right_child(8,root)
cc1 = t.add_left_child(22,c1)
cc2 = t.add_right_child(33,c1)
t.postorder(root)


