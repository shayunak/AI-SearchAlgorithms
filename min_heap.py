import sys

class MinHeap:
	def __init__(self):
		self.size = 0
		self.Heap = [[None, 0]]*(10**5 + 1)
		self.Heap[0] = [None, -1 * sys.maxsize]
		self.FRONT = 1

	def parent(self, pos):
		return pos//2

	def leftChild(self, pos):
		return 2 * pos

	def rightChild(self, pos):
		return (2 * pos) + 1

	def isLeaf(self, pos):
		return pos*2 > self.size

	def swap(self, fpos, spos):
		self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

	def find_element_and_replace_value(self, element, new_value):
		for i in range(1, self.size + 1):
			if self.Heap[i][0] == element:
				if new_value < self.Heap[i][1]:
					self.Heap[i][1] = new_value
					self.parent_reorder(i)

	def minHeapify(self, pos):
		if not self.isLeaf(pos):
			if (self.Heap[pos][1] > self.Heap[self.leftChild(pos)][1] or
			self.Heap[pos][1] > self.Heap[self.rightChild(pos)][1]):
				if self.Heap[self.leftChild(pos)][1] < self.Heap[self.rightChild(pos)][1]:
					self.swap(pos, self.leftChild(pos))
					self.minHeapify(self.leftChild(pos))
				else:
					self.swap(pos, self.rightChild(pos))
					self.minHeapify(self.rightChild(pos))

	def parent_reorder(self, pos):
		current = pos
		while self.Heap[current][1] < self.Heap[self.parent(current)][1]:
			self.swap(current, self.parent(current))
			current = self.parent(current)

	def insert(self, element):
		self.size += 1
		self.Heap[self.size] = element
		self.parent_reorder(self.size)

	def minHeap(self):
		for pos in range(self.size//2, 0, -1):
			self.minHeapify(pos)

	def remove(self):
		popped = self.Heap[self.FRONT][0]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -= 1
		self.minHeapify(self.FRONT)
		return popped
