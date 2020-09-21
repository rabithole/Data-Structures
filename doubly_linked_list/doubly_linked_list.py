print('2d list\n')

def printDl():
    currentNode = dl.head
    while True:
        if currentNode is not None:
            print('---> DL Value:', currentNode.value, '\n--->', 'LENGTH', dl.length, '\n--->', 'HEAD:', dl.head.value, '\n--->', 'TAIL:', dl.tail.value, '\n'),
            currentNode = currentNode.next
        else:
            # print(dl.tail.value, '--->')
            break
"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
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
        newNode = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            # self.head.prev = None
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head == None:
            print('No Head')
        else:
            delVal = self.head
            # self.head.next.prev = None
            self.head = self.head.next
        return delVal.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newNode = ListNode(value)
        if self.tail == None:
            # print('if add to tail')
            self.head = newNode
            self.tail = newNode
        else:
            # print('else add to tail')
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        return self.tail.value
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            delVal = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            # print(delVal.value, self.tail.next.value)
        return delVal.value
            

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head.value
        if current == node:
            print('found it at the head')
        while current:
            if current == node:
                current.prev.next = current.next
                current.next.prev = current.prev
            current = current.next

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

    def printList(self):
        currentNode = self.head
        # print('Head', self.head.prev)
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
        else:
            print('\nEnd of list \n')
            
            


dl = DoublyLinkedList()
dl.add_to_head(1)
dl.add_to_head(2)
dl.add_to_head(3)
dl.add_to_head(4)
dl.add_to_head(5)
dl.add_to_head(6)
dl.add_to_head('what')
dl.add_to_head('where')

# dl.remove_from_head()

dl.add_to_tail('the end')
dl.add_to_tail('the next ending')
dl.add_to_tail('one more end')

dl.remove_from_tail()
dl.remove_from_tail()
# dl.remove_from_tail()
# dl.remove_from_tail()
# dl.remove_from_tail()


# printDl()

dl.move_to_front('where')
dl.printList()