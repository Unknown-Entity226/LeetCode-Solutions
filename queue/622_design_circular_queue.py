'''
Problem Description:
Design a circular queue (ring buffer) with a fixed size.

The circular queue follows FIFO (First In First Out) principle,
and the last position is connected back to the first position
to efficiently reuse empty spaces.

Implement the following operations:
- MyCircularQueue(k): Initialize the queue with capacity k.
- enQueue(value): Insert an element into the queue.
- deQueue(): Delete an element from the queue.
- Front(): Get the front element.
- Rear(): Get the last element.
- isEmpty(): Check if the queue is empty.
- isFull(): Check if the queue is full.

Constraint:
- Do NOT use any built-in queue data structure.

Approach:
- Use a fixed-size list (array) to store elements.
- Maintain two pointers:
  - front: points to the front element
  - rear: points to the last element
- Initialize both front and rear to -1 to represent an empty queue.
- Use modulo arithmetic (%) to wrap indices around the array,
  achieving circular behavior.

Key Conditions:
- Queue is empty when rear == -1
- Queue is full when (rear + 1) % size == front

Operations:
- enQueue:
  - Check if the queue is full.
  - If empty, initialize front and rear.
  - Otherwise, move rear circularly and insert the element.
- deQueue:
  - Check if the queue is empty.
  - If only one element exists, reset front and rear.
  - Otherwise, move front circularly.
- Front / Rear:
  - Return the respective element or -1 if empty.

Time Complexity:
O(1) for all operations.
'''

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.items = [None] * k
        self.front = self.rear = -1

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        if self.rear == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
            return True

        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
            return True

        self.items[self.front] = None
        self.front = (self.front + 1) % self.size
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.items[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.rear == -1

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear + 1) % self.size == self.front

    def print_queue(self):
        print(self.items)
