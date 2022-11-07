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
delete node at given position

'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    #print list
    def printList(self):
        print("Current List:")
        temp = self.head
        while(temp):
            print(temp.data, end = ' ')
            temp = temp.next
        print()

    #insert node to beginning of list
    def push(self, new_node_data):
        #create node
        new_node = Node(new_node_data)

        
        #if list is empty make new_node head
        if self.head is None:
            self.head = new_node
        #else point new_node to current head, make new_node head
        else:
            new_node.next = self.head
            self.head = new_node

    #insert at end
    def append(self, new_node_data):
        #create new node
        new_node = Node(new_node_data)

        #if list is empty make new_node head
        if self.head is None:
            self.head = new_node
        #else transverse list to current last node, point current last node to new_node
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = new_node

    #check if given_node exists
    def NodeExists(self, given_node):
        if given_node is None:
            print("given_node does not exist")
            return False
        else:
            return True

    #check if list is empty
    def listIsNotEmpty(self):
        print("here")
        if self.head is None:
            print("list is empty")
            return False
        else:
            return True

    #insert node after given_node
    #notice the given_node will never be inserted at front of list
    def afterGivenNode(self, given_node, new_node_data):
        if self.NodeExists(given_node):
            #create new_node
            new_node = Node(new_node_data)

            #point new_node to where given_node points to
            #point given_node to new_node
            new_node.next = given_node.next
            given_node.next = new_node

    #insert node before given_node
    def beforeGivenNode(self, given_node, new_node_data):
        if self.NodeExists(given_node):
            #create new node
            new_node = Node(new_node_data)

            #if given_node is head point new_node to current head, make head new_node
            #need head case because need to appoint new_node as head and head does not have prev_node
            if given_node == self.head:
                new_node.next = self.head
                self.head = new_node
            #else, transverse to given_node while also tracking prev_node
            #point new_node to next of given_node, point next of prev_node to new_node 
            else:
                temp = self.head
                while(temp != given_node):
                    prev_node = temp
                    temp = temp.next
                #remember to point new_node to next of prev_node first 
                #because otherwise if you point pre_node to new_node first, pointing new_node to the next of prev_node will point new-node to itself 
                new_node.next = prev_node.next
                prev_node.next = new_node
                
        
    #insert node after first occurence of node with given key
    #notice how node will never be inserted at front of list
    def afterFirstKey(self, key, new_node_data):
        if self.head is None:
            print("list is empty")
            return False
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
        #else, point new_node to next of temp, point temp to new_node
        else:
            new_node.next = temp.next
            temp.next = new_node

    #insert node before first occurence of node with given key
    def beforeFirstKey(self, key, new_node_data):
        #check if list is empty
        if self.head is None:
            print("list is empty")
            return

        new_node = Node(new_node_data)
        temp = self.head

        #if head has key point new_node to current head, make new_node head
        #need case for head because need to reassign new_node as head and head will not have a previous
        if self.head.data == key:
            new_node.next = self.head
            self.head = new_node
        #else, transverse list until key is found or end of linked list (i.e. None, which is what the last node points to)
        else:
            while (temp):
                if temp.data == key:
                    break
                prev_node = temp
                temp = temp.next
            
            #if key was not found temp will be None because of the previous while statement
            if temp is None:
                print("key was not found")
            #else, point new_node to temp, point prev_node to new_node
            else:
                new_node.next = temp
                prev_node.next = new_node

    #check that index is valid (integer at least 0)
    def validIndex(self, index):
        if index < 0:
            print("please provide an index that's at least 0")
            return False
        else:
            return True

    #insert node after given index
    #notice that node will never be inserted at beginning of lists
    def afterGivenIndex(self, index, new_node_data):

        if self.validIndex(index):
            new_node = Node(new_node_data)

            #if list is empty
            if self.head is None:
                self.head = new_node
            #else, transverse list to index
            else:
                temp = self.head
                count = 0
                
                while(count != index and temp.next):
                    temp = temp.next
                    count += 1
                
                #if index is out of range
                if count < index:
                    print("index is out of range")
                #else, point new_node to next of temp, point temp to new_node
                else:
                    new_node.next = temp.next
                    temp.next = new_node

    #insert node before given index
    def beforeGivenIndex(self, index, new_node_data):
        if self.validIndex(index):
            
            new_node = Node(new_node_data)
            
            #if list is empty
            if self.head is None:
                self.head = new_node
            #else, transverse list to index
            else:
                #if index is 0 insert node at beginning of list
                #need case for index 0 because beginning node does not hae prev_node and new_node needs to become head
                
                if index == 0:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    temp = self.head
                    count = 0

                    while(count != index and temp.next):
                        prev_node = temp
                        temp = temp.next
                        count += 1

                    #if count < index index out of range
                    if count < index:
                        print("index out of range")
                    else:
                        new_node.next = temp
                        prev_node.next = new_node

    #delete given_node
    def deleteGivenNode(self, given_node):
        if self.NodeExists:
            #if given_node is head, make next of current head new head
            #need case for head to reassign head
            if given_node == self.head:
                self.head = self.head.next
            #else, transverse list to finde prev_node of given_node
            #need prev_node because need to point prev_node to given_node.next
            else:
                temp = self.head
                while(temp != given_node):
                    prev_node = temp
                    temp = temp.next
                prev_node.next = temp.next

    #delete all nodes with given key
    def deleteAllKey(self, key):
        #if list is empty
        if self.head is None:
            print("list is empty")
            return
        #if head has key
        #need case for head to reassign to new head
        while(self.head.data == key):
            self.head = self.head.next
        
        #transverse list
        temp = self.head
        while(temp.next):
            if temp.next.data == key:
                prev_node = temp
                prev_node.next = temp.next
                temp = temp.next
        

if __name__ == '__main__':

    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(5)
    llist.push(5)
    llist.append(9)
    llist.append(16)
    llist.append(100)
    
    llist.printList()
    
    llist.deleteAllKey(5)
    llist.printList()

    '''
    
    '''