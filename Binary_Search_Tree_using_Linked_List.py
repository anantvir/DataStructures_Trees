"""Reference :- Data Structures and Algorithms with C by Seymour Lipschutz"""

class LinkedBinarySearchTree:
    class Node:
        def __init__(self,info):
            self.info = info
            self.left_child = None
            self.right_child = None
            self.parent = None
    def __init__(self):
        self.CURR_PTR = None
        self.size = 0
        self.root = None
    
    def find_item(self,item):
        """Using 2 variables, LOC = To store location of found item, PARENT = To store parent of LOC, SAVE = to
        store parent of CURR_PTR"""
        if self.root == None:
            LOC = None
            SAVE = None
            PARENT = None
            return LOC,PARENT
        if self.root.info == item:
            LOC = self.root
            PARENT = None
            return LOC,PARENT
        self.CURR_PTR = self.root
        if item < self.root.info:
            self.CURR_PTR = self.CURR_PTR.left_child
            SAVE = self.root
        else:
            self.CURR_PTR = self.CURR_PTR.right_child
            SAVE = self.root
        while self.CURR_PTR != None:
            if item == self.CURR_PTR.info:
                LOC = self.CURR_PTR
                PARENT = SAVE
                return LOC,PARENT
            elif item < self.CURR_PTR.info:
                SAVE = self.CURR_PTR
                self.CURR_PTR = self.CURR_PTR.left_child
            else:
                SAVE = self.CURR_PTR
                self.CURR_PTR = self.CURR_PTR.right_child
        LOC = None
        PARENT = SAVE
        return LOC,PARENT

    def insert_item(self,item):
        LOC,PARENT = self.find_item(item)
        if LOC != None:
            raise ValueError("Item already exists !")
        newNode = self.Node(item)
        if PARENT == None:
            self.root = newNode
        elif item < PARENT.info:
            PARENT.left_child = newNode
        else:
            PARENT.right_child = newNode
        print("New Node inserted successfully !")
        return newNode

    def delete_item_with_1_or_0_child(self,LOCATION,PARENT):

        if LOCATION.left_child == None and LOCATION.right_child == None:
            CHILD = None
        elif LOCATION.left_child != None and LOCATION.right_child == None:
            CHILD = LOCATION.left_child
        else:
            CHILD = LOCATION.right_child
        if PARENT != None:
            if LOCATION == PARENT.right_child:
                PARENT.right_child = CHILD
            else:
                PARENT.left_child = CHILD
        else:
            self.root = CHILD
        print("Deleted the node successfully !")
    
    def delete_item_with_2_children(self,LOCATION,PARENT):

        """Determine inorder successor SUC and parent of SUC i.e PARSUC"""
        PTR = LOCATION.right_child
        SAVE = LOCATION
        while PTR.left_child != None:
            SAVE = PTR
            PTR = PTR.left_child
        SUC = PTR
        PARSUC = SAVE

        """Delete inorder successor SUC"""
        self.delete_item_with_1_or_0_child(SUC,PARSUC)

        """Replace LOC by its inorder successor"""
        if PARENT != None:
            if LOCATION == PARENT.left_child:
                PARENT.left_child = SUC
            else:
                PARENT.right_child = SUC
        else:
            self.root = SUC
        
        """Assign left and right children of the newly added node the left and right children of the deleted node"""
        SUC.left_child = LOCATION.left_child
        SUC.right_child = LOCATION.right_child
        
        print("Deleted the node successfully !")

    def delete(self,item):
        LOC,PARENT = self.find_item(item)
        if LOC == None:
            raise ValueError("Item not in tree !")
        if LOC.left_child != None and LOC.right_child != None:
            self.delete_item_with_2_children(LOC,PARENT)
        else:
            self.delete_item_with_1_or_0_child(LOC,PARENT)
        print("Delete function completed !")


    """--------------Preorder Traversal using Stacks ------------------"""
    def preorder(self):
        STACK = [None]*1
        PTR = self.root
        output_list = []
        while PTR != None:
            output_list.append(PTR.info)
            if PTR.right_child != None:
                STACK.append(PTR.right_child)
            if PTR.left_child != None:
                PTR = PTR.left_child
            else:
                PTR = STACK.pop()
        return output_list

    """--------------Inorder Traversal using Stacks ------------------"""
    def inorder(self):
        STACK = [None]*1
        PTR = self.root
        output_list = []
        while PTR != None:
            STACK.append(PTR)
            PTR = PTR.left_child
        PTR = STACK.pop()
        while PTR != None:
            output_list.append(PTR.info)
            if PTR.right_child != None:
                PTR = PTR.right_child
                while PTR != None:
                    STACK.append(PTR)
                    PTR = PTR.left_child
            PTR = STACK.pop()
        return output_list



t = LinkedBinarySearchTree()

t.insert_item(60)
t.insert_item(25)
t.insert_item(15)
t.insert_item(50)
t.insert_item(33)
t.insert_item(44)
t.insert_item(75)
t.insert_item(66)

#t.delete(44)
#t.delete(75)
#t.delete(25)

print(t.preorder())
print(t.inorder())

print('hello')





    


