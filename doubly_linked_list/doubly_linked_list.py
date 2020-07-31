"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""

def printDl():
    currentNode = dl.head
    while True:
        if currentNode is not None:
            print('DL: ', currentNode.value, '--->', ' ', dl.length, 'TAIL:', dl.tail.value, ' ', 'HEAD:', dl.head.value),
            currentNode = currentNode.next
        else:
            # print(dl.tail.value, '--->')
            break

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node from ListNode
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            print('none')
        else:
            deletedValue = self.head
            # headNext = self.head.next.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            # print('head was:', deletedValue + '!')
            # return deletedValue
        
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            # print('Line 75: ', self.tail.prev.value)
            
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            # self.tail = None
            print('none')
        else:
            deletedValue = self.tail
            # print('Line 89: ', self.tail.value) 
            self.tail = self.tail.prev
            self.tail.next = None
            # print('Line 91: ', deletedValue.value)
            self.length -= 1
            # return deletedValue


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        # currentNode = self.head
        # while self.head != None:
        #     if self.head.value == value:
        #         print('first', 'head: ', self.head.value, currentNode.value)
        #         return
        #     if currentNode.value != value:
        #         currentNode = currentNode.next
        #         print('second: ', currentNode.value)
        #     if currentNode.value == value:
        #         print('found it: ', currentNode.value)
        #         self.head = currentNode
        #         # self.delete(currentNode)
        #         printDl()
        #     else: 
        #         currentNode = currentNode.next
        #         print('else: ', currentNode.value)


        
    """
    Removes the input value from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, value):
        if value is not self.tail:
            self.delete(value)
            self.add_to_tail(value)
        # currentNode = self.head
        # while self.head:
        #     print('CurrentNode initial:', currentNode.value, ' ', 'tail:', self.tail.value)
        #     # return 
        #     if self.head.value == value:
        #         self.tail = self.head
        #         self.head = self.head.next
        #         # self.tail = currentNode
        #         print('TAIL:', self.tail.value, ' ', 'HEAD:', self.head.value, ' ', 'CURRENTNODE VALUE:', currentNode.value)
        #         break
            # if currentNode != self.head:
            #     currentNode = self.head.next

            

            #     self.head = self.head.next
            #     self.tail.next = None
            #     print('first', 'head: ', self.head.value, currentNode.value)
            #     return
            # if currentNode.value != value:
            #     currentNode = currentNode.next
            #     print('second: ', currentNode.value)
            # if currentNode.value == value:
            #     print('found it: ', currentNode.value, self.head.value)
            #     self.tail = currentNode
            #     # self.delete(currentNode)
            # else: 
            #     currentNode = currentNode.next
            #     print('else: ', currentNode.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, value):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.value == value:
            self.head = current.next
            current.next.prev = None
            node_deleted = True

        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                print(current.value)
                if current.value == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

dl = DoublyLinkedList()
dl.add_to_head('one')
dl.add_to_head('two')
dl.add_to_head('three')
dl.add_to_head('four')
dl.add_to_head('five')

# dl.remove_from_head()
# dl.remove_from_head()

# dl.add_to_tail('ten')
# dl.add_to_tail('eleven')

# dl.remove_from_tail()

dl.delete('three')

# dl.move_to_front('two')
# dl.move_to_end('five')

printDl()