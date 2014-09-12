#queue.py

#Class Queue

class Queue:
	first = None
	last = None
	next = None
	def __init__(self,data=None): 
		self.data = data

	def enq(self,data):
		if self.first == None:
			self.last = Queue(data)
			self.first = self.last
			print("First")
		else:
			self.last.next = Queue(data)
			self.last = self.last.next
			print("Last")
	def deq(self):pass
	def peek(self):
		return self.first.data


q1 = Queue()
q1.enq(1)
q1.enq(2)
print(q1.peek())

