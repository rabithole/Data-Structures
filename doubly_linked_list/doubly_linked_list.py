"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""

def printDl():
    currentNode = dl.head
    while True:
        if currentNode is not None:
            print('Print DL: ', currentNode.value, '--->', dl.length),
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
        # Increment dl list length
        self.length += 1
        # check if there is anything at the head
        if self.head is None:
            # make head and tail the same node
            self.head = new_node
            self.tail = self.head
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            # print('Line 43: ', self.tail.value)
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            print('none')
        else:
            deletedValue = self.head.value
            # headNext = self.head.next.value
            self.head = self.head.next
            self.length -= 1
            # print('head was:', deletedValue + '!')
            return deletedValue

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
        self.length -= 1
        if self.tail is None:
            self.tail = None
        else:
            removedNode = self.tail
            # print('Line 89: ', self.tail.value) 
            self.tail = self.tail.prev
            # print('Line 91: ', removedNode.value)
            return removedNode


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, value):
        # currentNode = self.head
        if self.head is None or self.head.value is value:
            return
        currentNode = self.head.next
        while self.head is not None:
            if currentNode.value == value:
                newHead = currentNode
                self.head = currentNode
                # self.delete(newHead)
                # dl.length -= 1
                print('Line 109: ', currentNode.value, self.head.value, dl.length)
                # printDl()
                return printDl()
            elif currentNode.value != value:
                currentNode = currentNode.next
                # print('Line 112: ', currentNode.value)
            else:
                return



    """
    Removes the input value from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, value):
        # Delete a specific item
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.value == value:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
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

# # dl.remove_from_head()
# # dl.remove_from_head()

dl.add_to_tail('ten')
dl.add_to_tail('eleven')

# dl.remove_from_tail()

# dl.delete('four')
printDl()

dl.move_to_front('five')

################### Class code -------------------------------------
"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.prev = prev
#         self.value = value
#         self.next = next
            
#     """
#     Optional `delete` method on `ListNode` to make subsequent
#     methods more DRY.
#     """
#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev
            
# """
# Our doubly-linked list class. It holds references to 
# the list's head and tail nodes.
# """
# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length
    
#     """
#     Wraps the given value in a ListNode and inserts it 
#     as the new head of the list. Don't forget to handle 
#     the old head node's previous pointer accordingly.
#     """
#     def add_to_head(self, value):
#         new_node = ListNode(value, None, None)
#         self.length += 1
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
        
#     """
#     Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node.
#     """
#     def remove_from_head(self):
#         value = self.head.value
#         self.delete(self.head)
#         return value
            
#     """
#     Wraps the given value in a ListNode and inserts it 
#     as the new tail of the list. Don't forget to handle 
#     the old tail node's next pointer accordingly.
#     """
#     def add_to_tail(self, value):
#         new_node = ListNode(value, None, None)
#         self.length += 1
#         if not self.tail and not self.head:
#             self.tail = new_node
#             self.head = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
            
#     """
#     Removes the List's current tail node, making the 
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node.
#     """
#     def remove_from_tail(self):
#         value = self.tail.value
#         self.delete(self.tail)
#         return value
            
#     """
#     Removes the input node from its current spot in the 
#     List and inserts it as the new head node of the List.
#     """
#     def move_to_front(self, node):
#         if node is self.head:
#             return
#         value = node.value
#         if node is self.tail:
#             self.remove_from_tail()
#         else:
#             node.delete()
#             self.length -= 1
#         self.add_to_head(value)
        
#     """
#     Removes the input node from its current spot in the 
#     List and inserts it as the new tail node of the List.
#     """
#     def move_to_end(self, node):
#         pass

#     def delete(self, node):
#         pass

#     def get_max(self):
#         pass