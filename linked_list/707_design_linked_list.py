'''
Problem Description:
Design a linked list implementation. You may choose to use a singly
or doubly linked list.

For a singly linked list:
- Each node contains:
  - val: the value of the node
  - next: reference to the next node

All nodes are 0-indexed.

Implement the following operations:
- get(index): Get the value of the index-th node in the linked list.
- addAtHead(val): Add a node of value val before the first element.
- addAtTail(val): Append a node of value val as the last element.
- addAtIndex(index, val): Add a node of value val before the index-th node.
- deleteAtIndex(index): Delete the index-th node in the linked list.

Approach:
- Use a singly linked list with a head pointer.
- Maintain a size variable to track the number of nodes.
- Traverse the list when needed to reach a specific index.

Operation details:
- get:
  - Traverse to the index-th node and return its value.
- addAtHead:
  - Create a new node and point it to the current head.
- addAtTail:
  - Traverse to the last node and append the new node.
- addAtIndex:
  - Traverse to the node before the target index and insert the new node.
- deleteAtIndex:
  - Adjust pointers to skip the node at the given index.

Time Complexity:
- get: O(n)
- addAtHead: O(1)
- addAtTail: O(n)
- addAtIndex: O(n)
- deleteAtIndex: O(n)

'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def addAtHead(self, val):
        self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val):
        new = Node(val)

        if not self.head:
            self.head = new
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new

        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        curr.next = Node(val, curr.next)
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1
