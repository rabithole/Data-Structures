"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __str__(self):
      print(f'\n The length of the list is {len(self.storage)} and here is what is in it {self.storage}\n')

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
      if len(self.storage) == 0:
        return None
      return self.storage.pop()



        
firstSt = Stack()
firstSt.push('what')
firstSt.push('when')
firstSt.push('where')
firstSt.push('how')
firstSt.push('why')
firstSt.push('who cares?')

firstSt.__str__()

firstSt.pop()
firstSt.pop()
firstSt.pop()
firstSt.pop()
firstSt.pop()

firstSt.__str__()


st1 = LinkedList()
st1.add_to_tail(1)
st1.add_to_tail(2)
st1.add_to_tail(3)
st1.add_to_tail(4)
st1.add_to_tail(5)
st1.add_to_tail(6)

print(st1.head.value)

st1.printList()