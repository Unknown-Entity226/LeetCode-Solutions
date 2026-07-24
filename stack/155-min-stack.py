"""
Problem Description:
Design a stack that supports push, pop, top, and
retrieving the minimum element in constant time.

Approach:
- Store each element as [value, minimum_so_far].
- While pushing:
  - Update the current minimum.
  - Store both the value and the minimum till that point.
- While popping:
  - Remove the top element.
  - Restore the previous minimum from the new top.
- The top element and minimum can be retrieved directly
  from the stack.

Time Complexity:
O(1)

Reason:
- push, pop, top, and getMin each perform a constant
  number of operations.

Space Complexity:
O(n)

Reason:
- The stack stores one pair [value, minimum_so_far] for
  each pushed element.
"""


class MinStack:

    def __init__(self):
            self.stack = []
            self.min = float("inf")
    def push(self, value: int) -> None:
            self.min = min(self.min, value)
            self.stack.append([value, self.min])

    def pop(self) -> None:
            popped = self.stack.pop()
            if self.stack:
                self.min = self.stack[-1][1]
            else:
                self.min = float("inf")

    def top(self) -> int:
            return self.stack[-1][0]

    def getMin(self) -> int:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
