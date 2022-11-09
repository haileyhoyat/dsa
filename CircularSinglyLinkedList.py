'''
insert at beginning
inset at end
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None
    
    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, new_node_data):
        #create new_node
        new_node = Node(new_node_data)

        #if list is empty mew new-node tail, point tail to new_node
        if self.tail is None:
            self.tail = new_node
            self.tail.next = new_node
        #else point new_node to where tail points to, point tail to new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    #insert at end
    def append(self, new_node_data):
        #create new_node
        new_node = Node(new_node_data)
         #if list is empty mew new-node tail, point tail to new_node
        if self.tail is None:
            self.tail = new_node
            self.tail.next = new_node
        #else point new_node to self.tail.next, point self.tail to new_node, reassign tail to new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

        
    # Function to print nodes in a given circular linked list
    def printList(self):
        #set temp as head (i.e. where tail points to)
        temp = self.tail.next
        
        #transverse list
        while(temp):
            print(temp.data, end = ' ')
            #if at beginning of list stop printing
            if temp.next == self.tail.next:
                break
            #move to next node
            temp = temp.next
            

if __name__ == '__main__':
    csll = CircularSinglyLinkedList()

    csll.push(7)
    csll.push(7)
    csll.push(8)
    csll.push(7)
    csll.append(100)
    csll.push(17)

    csll.printList()

    '''
    
    
    '''