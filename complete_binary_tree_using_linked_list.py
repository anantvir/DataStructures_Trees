""" Author - Anantvir Singh, concept reference:= Data Structures in C by Seymour Lipschutz"""

class Node:
    def __init__(self,info,link =None):
        self.info = info
        self.link = link

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None
        self.size = 0
        self.temp_lst = []
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self,item):
        if self.tail == None:
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            self.temp_lst.append(item)
        else:
            newNode = Node(item)
            self.tail.link = newNode
            self.tail = newNode
            self.size += 1
            self.temp_lst.append(item)
        return self.temp_lst
    
    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty. Cannot dequeue !')   # Or raise an exception here
        item = self.head.info
        temp_pointer = self.head
        self.head = self.head.link
        temp_pointer.link = None
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
            self.current_ptr = None 
        return item
    
    def get_front_node(self):
        if self.isEmpty():
            print('Queue is empty. Cannot dequeue !')
        item = self.head.info
        return item
        
class LinkedCompleteBinaryTree:

    class Node:
        def __init__(self,item,parent =None,left_child = None,right_child = None):
            self._item = item
            self._parent = parent
            self._left_child = left_child
            self._right_child = right_child
    
    def __init__(self):
        self.root = None
        self.size = 0
        self.Q = LinkedQueue()

    def insert(self,item):
        if self.root == None:
            newNode = self.Node(item)
            self.Q.enqueue(newNode)
            self.root = newNode
        else:
            existing_node = self.Q.get_front_node()     # Get front element of queue------- # can also use while loop here
            if existing_node._left_child is None:       # check if left child is None 
                newNode = self.Node(item)
                existing_node._left_child = newNode     # if yes insert new node there
                newNode._parent = existing_node
                self.size += 1
            elif existing_node._right_child is None:    # check if left child is None
                newNode = self.Node(item)
                existing_node._right_child = newNode    # if yes insert new node there
                newNode._parent = existing_node
                self.size += 1
            else:
                newNode = self.Node(item)
                self.Q.enqueue(existing_node._left_child)   # if both children are not Null, then enquque both children and dequeue the parent
                self.Q.enqueue(existing_node._right_child)
                self.Q.dequeue()                            # dequeue the parent as both its child nodes are full
                top_node = self.Q.get_front_node()          # get front element of queue and repeat the above steps
                if top_node._left_child is None:
                    top_node._left_child = newNode
                    newNode._parent = top_node
                    self.size += 1
                elif top_node._right_child is None:
                    top_node._right_child = newNode
                    newNode._parent = top_node
                    self.size += 1
        frontOfQueue = self.Q.get_front_node()
        return frontOfQueue

t = LinkedCompleteBinaryTree()
t.insert(4)
t.insert(9)
t.insert(6)
t.insert(8)
t.insert(2)
t.insert(22)
t.insert(33)
t.insert(44)
t.insert(100)
t.insert(179)
t.insert(148)