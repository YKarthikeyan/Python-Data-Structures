from linkedlist.Node import Node

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.counter = 0

	def insertfirst(self,data):
		self.counter +=1
		newNode = Node(data)
		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

	def size(self):
		return self.counter
	
	def insertlast(self,data):
		if self.head is None:
			self.insertfirst(data)
			return	
		
		self.counter +=1
		newNode = Node(data)
		actualNode = self.head
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode
		actualNode.nextNode = newNode

	def remove(self,data):
		self.counter-=1
		if self.head:
			if data == self.head.data:
				self.head = self.head.nextNode
			else:
				self.head.remove(data,self.head)

	def traverselist(self):
		actualNode = self.head
		print("List is: ")
		while actualNode.nextNode is not None:
			print("%d" %actualNode.data)
			actualNode = actualNode.nextNode 
		print("%d" %actualNode.data)

	def search(self,data):
		actualNode = self.head
		if self.head:
			while actualNode.data!= data and actualNode.nextNode is not None:
				actualNode = actualNode.nextNode
			if actualNode.data == data:
				print("%d is present in the list" %data)
			else:
				print("%d is not present in the list" %data)
