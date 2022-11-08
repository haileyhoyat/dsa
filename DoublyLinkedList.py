'''
insert at beginning
insert at end
insert after given_node
insert before given_node
insert after node with given key
insert before node with given key
insert after given index
insert before given index

delete given_node
delete all nodes with given key
delete node at given index
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #print list
    def printList(self):
        #if list is empty
        if self.head is None:
            print("list is empty")
        #else, transverse list to print eadh node
        else:
            print("Current List: ")
            temp = self.head
            while(temp):
                print(temp.data, end=' ')
                temp = temp.next
        print()

    #check if given_node exists
    def nodeExists(self, given_node):
        if given_node is None:
            print("given node does not exist")
            return False
        else:
            return True

    #check for valid index
    def validIndex(self, index):
        if index < 0:
            print("please enter an integer that's at least 0")
            return False
        else:
            return True

    #insert node at beginning of list
    def push(self, new_node_data):
        #create new node
        new_node = Node(new_node_data)

        #if list is empty assing new_node as head
        if self.head is None:
            self.head = new_node
        #else, point new_node to current head, 
        #point head.prev to new_node
        #reassign head to new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    #insert node at end of list
    def append(self, new_node_data):
        #create new node
        new_node = Node(new_node_data)

        #if list is empty assign new_node head
        if self.head is None:
            self.head = new_node
        #else, transverse list to end
        else:
            temp = self.head
            #the last node will not point to another node
            while(temp.next):
                temp = temp.next
            #point last node to new_node
            #point new_node.prev to temp
            temp.next = new_node
            new_node.prev = temp

    #insert node after given_node
    #notice how given_node will never become head
    #when given a node don't have to transverse list because you're given the actual node
    def insertAfterGivenNode(self, given_node, new_node_data):
        if self.nodeExists(given_node):
            #create new_node
            new_node = Node(new_node_data)
            #if given_node is last node given_node.next is None
            #point given_node to new_node, new_node.prev.next = new_node
            #need last node case because new_node will become last node and not have any next node
            if given_node.next is None:
                given_node.next = new_node
                new_node.prev = given_node
            #else, point new_node to given_node.next, new_node points back to given_node
            #point given_node.next back to new_node, point given_node to new_node
            else:
                new_node.next = given_node.next
                new_node.prev = given_node
                given_node.next.prev = new_node
                given_node.next = new_node

    #insert node before given_node
    #unlike in singly linked list do not need to transverse because have .prev attribute
    def insertBeforeGivenNode(self, given_node, new_node_data):
        if self.nodeExists(given_node):
            #create new_node
            new_node = Node(new_node_data)

            #if given_node is head, point new_node to head, point head back to new_node, reassign head
            #need head case because new-node will become head and not have any previous node pointing to it
            if given_node == self.head:
                new_node.next = given_node
                given_node.prev = new_node
                self.head = new_node
            #else, point new_node to given_node, point new_node back to given_node.prev
            #point given_node.prev.next to new_node, point given_node back to new_node
            else:
                new_node.next = given_node
                new_node.prev = given_node.prev
                given_node.prev.next = new_node
                given_node.prev = new_node
            
    #insert node after given key
    #node will never be head
    def insertAfterFirstKey(self, key, new_node_data):
        new_node = Node(new_node_data)
        temp = self.head
        
        #transverse list until key is found or end of linked list (i.e. None, which is what the last node points to)
        while (temp):
            if temp.data == key:
                break
            temp = temp.next
        
        #if key was not found temp will be None because of the previous while statement
        if temp is None:
            print("key was not found")
        else:
            #if temp is last node (i.e temp.next is None)
            #point temp to new_node, point new_node back to temp
            #need case for last node because new_node will become last node and not have a proceeding node
            if temp.next == None:
                temp.next = new_node
                new_node.prev = temp
            #else, point new_node to temp.next, point new_node back to temp
            #point temp.next back to new_node, point temp to new_node
            else:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node

    #insert node before given key
    #node will never be last node
    def insertBeforeFirstKey(self, key, new_node_data):
        new_node = Node(new_node_data)
        temp = self.head

        #transverse list until key is found or end of linked list (i.e. None, which is what the last node points to)
        while (temp):
            if temp.data == key:
                break
            temp = temp.next
        
        #if key was not found temp will be None because of the previous while statement
        if temp is None:
            print("key was not found")
        else:
            #if temp is head
            #point new_node to head, point current head back to new_node, reassign head to new_node
            #need case for head because new_node will become head
            if temp == self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            #else, point new_node to temp, point new_node back to temp.prev
            #point temp.prev.next to new_node, point temp.prev to new_node
            else:
                new_node.next = temp
                new_node.prev = temp.prev
                temp.prev.next = new_node
                temp.prev = new_node

    #insert after index
    #node will never be head
    def insertAfterIndex(self, index, new_node_data):
        if self.validIndex(index):
            new_node = Node(new_node_data)
            
            #if list is empty
            if self.head is None:
                self.head = new_node
            #else, transverse list to index
            else:
                temp = self.head
                count = 0
                #the reason you need to check for temp.next is because if you get to the end of the while loop the last temp will be None and you can't add a node after None
                # so you need to stop the while before you get to None 
                while(count != index and temp.next):
                    temp = temp.next
                    count += 1

                #if count < index, index out of range
                if count < index:
                    print("index out of range")
                #elif temp is last node (i.e. temp points to None) insert new_node at end
                #point temp to new_node, point new_node back to temp
                elif temp.next == None:
                    temp.next = new_node
                    new_node.prev = temp
                #else temp is middle node, point new_node to temp.next, point new_node back to temp
                #point temp.next.prev to new_node, point temp.next to new_node
                else:
                    new_node.next = temp.next
                    new_node.prev = temp
                    temp.next.prev = new_node
                    temp.next = new_node

    #insert node before index
    #node will never be last node
    def insertBeforeIndex(self, index, new_node_data):
        if self.validIndex(index):
            new_node = Node(new_node_data)
            
            #if list is empty
            if self.head is None:
                self.head = new_node
            #else, list is not empty
            else:
                #if index == 0, make new_node head
                if index == 0:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                #else, transverse to index
                else:
                    temp = self.head
                    count = 0
                    #the reason you need to check for temp.next is because if you get to the end of the while loop the last temp will be None and you can't add a node before None
                    # so you need to stop the while before you get to None 
                    while(count != index and temp.next):
                        temp = temp.next
                        count += 1

                    #if count < index, index out of range
                    if count < index:
                        print("index out of range")
                    #else temp is middle node, point new_node to temp, point new_node back to temp.prev
                    #point temp.prev.next to new_node, point temp back to new_node
                    else:
                        new_node.next = temp
                        new_node.prev = temp.prev
                        temp.prev.next = new_node
                        temp.prev = new_node

    #delete given node
    def deleteNode(self, given_node):
        if self.nodeExists(given_node):
            #if node is head
            if given_node == self.head:
                self.head = given_node.next
                self.head.prev = None
            else:
                #if node is last node (i.e. given_node.next is None)
                #need last node case because last node does not have proceeding node 
                if given_node.next is None:
                    given_node.prev.next = None
                #else, point given_node.next back to given_node.prev
                #point given_node.prev to given_node.next
                else:
                    given_node.next.prev = given_node.prev
                    given_node.prev.next = given_node.next

    #delete all nodes with given key
    def deleteAllGivenKey(self, key):
        temp = self.head
        
        #if head has key
        #need case for head to reassign to new head
        while (temp and temp.data == key):
            self.head = temp.next
            temp.next.prev = None
            temp = temp.next
        
        # Delete occurrences other than head
        while (temp):
            print("here")
            if temp.data == key:
                #if node is last 
                #need last node case because last node does not have proceeding node
                if temp.next is None:
                    temp.prev.next = None
                else:
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
            temp = temp.next

    #delete node at given index
    def deleteGivenIndex(self, index):
        if self.validIndex(index):
            #if list is empty
            if self.head is None:
                print("list is empty")
            #else, transverse list to index
            else:
                #if index is 0 reassign head
                #need case for index 0 because need to reassign head
                if index == 0:
                    self.head = self.head.next
                    self.head.prev = None
                #else, transverse list to index
                else:
                    temp = self.head
                    count = 0

                    #the reason you need to check for temp.next is because if you get to the end of the while loop the last temp will be None
                    # and you can't add a node before or after None
                    # so you need to stop the while before you get to None 
                    while(count != index and temp.next):
                        temp = temp.next
                        count += 1

                    #if count < index index out of range
                    if count < index:
                        print("index out of range")
                    #else, 
                    else:
                        #if node is last 
                        #need last node case because last node does not have proceeding node
                        if temp.next is None:
                            temp.prev.next = None
                        else:
                            temp.next.prev = temp.prev
                            temp.prev.next = temp.next         

if __name__ == '__main__':

    dll = DoublyLinkedList()
    dll.push(4)
    dll.push(7)
    dll.push(7)
    dll.append(8)
    dll.append(9)
    dll.append(10)
    dll.printList()

    dll.insertAfterIndex(6, 100)
    dll.printList()
    

    '''
    
    '''