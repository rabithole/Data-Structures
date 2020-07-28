class Node:
	def __init__(self, value=None, next_node=None):
	# the value at this linked list node
		self.value = value
		# reference to the next node in the list
		self.next_node = next_node

	# def get_value(self):
	def __str__(self):
		return 'The next node value is ' + self.value

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
	# set this node's next_node reference to the passed in node
		self.next_node = new_next

class LinkedList:
	def __init__(self, head, tail):
	# reference to the head of the list
		self.head = head
		# reference to the tail of the list
		self.tail = tail

	def add_to_tail(self, value):
	# wrap the input value in a node
		new_node = Node(value, None)
	# check if there is no head (i.e., the list is empty)
		if not self.head:
		  # if the list is initially empty, set both head and tail to the new node
		  self.head = new_node
		  self.tail = new_node
		# we have a non-empty list, add the new node to the tail
		else:
		  # set the current tail's next reference to our new node
		  self.tail.set_next(new_node)
		  # set the list's tail reference to the new node
		  self.tail = new_node

	def remove_head(self):
	# return None if there is no head (i.e. the list is empty)
		if not self.head:
			return None
		# if head has no next, then we have a single element in our list
		if not self.head.get_next():
		# get a reference to the head
			head = self.head
		# delete the list's head reference
			self.head = None
		# also make sure the tail reference doesn't refer to anything
			self.tail = None
		# return the value
		return head.get_value()
	# otherwise we have more than one element in our list
		value = self.head.get_value()
		# set the head reference to the current head's next node in the list
		self.head = self.head.get_next()
		return value

	def contains(self, value):
		if not self.head:
	  		return False

	# get a reference to the node we're currently at; update this as we traverse the list
		current = self.head
	# check to see if we're at a valid node 
		while current:
	  # return True if the current value we're looking at matches our target value
		  	if current.get_value() == value:
		   		return True
	  # update our current node to the current node's next node
	  		current = current.get_next()
	# if we've gotten here, then the target node isn't in our list
		return False

	def get_max(self):
	  if not self.head: 
	    return None
	  current = self.head
	  max_val = self.head.value
	  while current:
	    if current.value > max_val:
	      max_val = current.value
	    current = current.next_node
	  return max_val

node1 = Node('one')
node2 = Node('two')

list = node1.next_node = node2

# node1 -> node2 -> node3

print(str(node1))

class linkedList:
	def __init__(self, head=None):
		self.head = head

	def insert(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
			return

		currentNode = self.head
		while True:
			if currentNode.next_node is None:
				currentNode.next_node = node
				break
			currentNode = currentNode.next_node

	def printLinkedList(self):
		currentNode = self.head
		while currentNode is not None:
			print(currentNode.value, '->'),
			currentNode = currentNode.next_node
		print('None')

ll = linkedList()
# ll.printLinkedList()
ll.insert('yeah')
# ll.printLinkedList()
ll.insert('we')
# ll.printLinkedList()
ll.insert('got')
# ll.printLinkedList()
ll.insert('this!')
ll.insert(200)
ll.printLinkedList()



