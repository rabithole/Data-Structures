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
class Stack:
    def __init__(self, size, storage):
        self.size = 0
        self.storage = []

    def __len__(self):
      return len(self.storage)

    def push(self, value):
      self.storage.append(value)

    def pop(self):
      self.storage.pop()


FirstStack = Stack(1, 3)

FirstStack.push('what')
FirstStack.push('when')
FirstStack.push('where')
FirstStack.push('why')
FirstStack.push(2)

FirstStack.pop()
FirstStack.pop()
FirstStack.pop()
print(len(FirstStack))

print(FirstStack.storage)

