#stack.py

#LIFO
#Stack class 

class Stack:
	top = None
	def __init__(self,data,next=None):
		self.data = data
		self.next = next
	def push(self,data):
		node = Stack(data)
		node.next = self.top
		self.top = node
	def pop(self):
		if self.top != None:
			popped = self.top
			self.top = self.top.next
		else:
			popped = None
		return popped
	def peek(self):
		return self.top.data

s1 = Stack(1)
s1.push(2) #pushed 2
print("Top: {}".format(s1.peek())) #shows 2 on top
s1.push(3)
s1.push(4)
popped = s1.pop() #popped 4
print("Popped: {}".format(popped.data)) #shows 4
print("Top: {}".format(s1.peek())) #shows 3
