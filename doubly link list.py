#doubly link list (DLL)

class DLL:
	def __init__(self, val):
		self.prev = None
		self.next = None
		self.val = val
		
def dll_append(node1, head):
	curr = head
	if head.prev is None and head.next is None:
		curr.next = node1
		node1.next = None
		node1.prev = curr
	else:
		while curr is not None:
			#print(node.val)
			if curr.next is None:
				#print("here")
				curr.next = node1
				node1.prev = curr
				node1.next = None	
			curr = curr.next

node = DLL(10)
head = node
#dll_append(node, head)

node1 = DLL(11)
dll_append(node1, head)

node2 = DLL(12)
dll_append(node2, head)

node3 = DLL(13)
dll_append(node3, head)

node4 = DLL(14)
dll_append(node4, head)

curr = head

while curr:
	print(' - ' + str(curr.val))
	curr = curr.next