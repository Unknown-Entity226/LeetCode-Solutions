'''
Problem Description:
Design a circular double-ended queue (deque) with a fixed size.

A circular deque allows insertion and deletion from both the front
and the rear ends.

Implement the following operations:
- MyCircularDeque(k): Initialize the deque with capacity k.
- insertFront(value): Insert an element at the front. Return True if successful.
- insertLast(value): Insert an element at the rear. Return True if successful.
- deleteFront(): Delete an element from the front. Return True if successful.
- deleteLast(): Delete an element from the rear. Return True if successful.
- getFront(): Get the front element. Return -1 if empty.
- getRear(): Get the rear element. Return -1 if empty.
- isEmpty(): Check whether the deque is empty.
- isFull(): Check whether the deque is full.

You must solve the problem without using built-in deque structures.

Approach:
- Use a fixed-size array to store deque elements.
- Maintain two pointers:
  - front: points to the front element
  - rear: points to the rear element
- Initialize front and rear to -1 to represent an empty deque.
- Use modulo arithmetic (%) to wrap indices around the array,
  enabling circular behavior.

Key Conditions:
- Deque is empty when front == -1
- Deque is full when (rear + 1) % size == front

Operations:
- insertFront:
  - Check if deque is full.
  - Move front backward circularly and insert the value.
- insertLast:
  - Check if deque is full.
  - Move rear forward circularly and insert the value.
- deleteFront / deleteLast:
  - Adjust pointers accordingly.
  - Reset front and rear when deque becomes empty.
- getFront / getRear:
  - Return the value at front or rear if deque is not empty.

Time Complexity:
O(1) for all operations.

Space Complexity:
O(k), where k is the capacity of the deque.
'''

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.items = [None] * k
        self.front = self.rear = -1

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.front == -1:
            self.front = self.rear = 0
            self.items[self.front] = value
            return True

        if self.front == (self.rear + 1) % self.size:
            return False

        self.items[(self.front - 1) % self.size] = value
        self.front = (self.front - 1) % self.size
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.front == -1:
            self.front = self.rear = 0
            self.items[self.front] = value
            return True

        if self.front == (self.rear + 1) % self.size:
            return False

        self.items[(self.rear + 1) % self.size] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.front == -1:
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
            return True

        self.items[self.front] = None
        self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.front == -1:
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
            return True

        self.items[self.rear] = None
        self.rear = (self.rear - 1) % self.size
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.front == -1:
            return -1
        return self.items[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.front == -1:
            return -1
        return self.items[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front == -1

    def isFull(self):
        """
        :rtype: bool
        """
        return self.front == (self.rear + 1) % self.size
