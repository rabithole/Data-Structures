class Node: 
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add_to_tail(self, value):
		# These three steps assume that the tail is already referring to a Node
		# 1. create new node from value
		new_node = Node(value, None)
		# 2. set the old tail's next tor refer to the new Node
		if self.head is None and self.tail is None: 
			# if the list is empty, set tail to new node
			self.head = new_node
			self.tail = new_node
		# 3. reassign self.tail to refer to the new Node
		else: 
			self.tail.set_next(new_node)
			self.tail = new_node

	def remove_head(self):
		if not self.head and not self.tail: 
			return None
		val = self.head.get_value()
		self.head = self.head.get_next()
		return val

		if not self.head.get_next():
			head = self.head
			self.tail = None
			return head.get_value()

		# Kwabena's solution
		if self.head.get_next(): 
			head = self.head
			# set head reference to None
			self.head = None
			# set tail reference to None
			self.tail = None
			return head.get_value()
		value = self.head.get_value
		self.head = self.head.get_next():
		return value
			# 3. it depends

	def remove_tail(self):
		current = self.head 

		while current.get_next() is not self.tail:
			current = current.get_next()
		val = self.tail.get_value()
		self.tail = current
		return val


