"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   a) A list will use more memory.  
   b) It will slow down when the size exceeds the allocated memory because it must relocate the stack to another memory location and increase the allocation size. 
   c) A linked list is slower to access a given value in it's nodes. You must iterate from the beginning until you find the requested value.  
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def __str__(self):
      print(f'\n Here is your queue {self.storage}')

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
      if len(self.storage) == 0:
        return None
      return self.storage.pop(-1)

inQue = Queue()

inQue.enqueue(f'First in {1}')
inQue.enqueue(2)
inQue.enqueue(3)
inQue.enqueue(4)
inQue.enqueue(5)

inQue.dequeue()

inQue.__str__()


import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList


q1 = LinkedList()

q1.add_to_tail(f'First in {1}')
q1.add_to_tail(2)
q1.add_to_tail(3)
q1.add_to_tail(4)
q1.add_to_tail(5)

q1.remove_head()

q1.printList()
