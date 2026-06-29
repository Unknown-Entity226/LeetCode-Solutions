"""
Problem Description:
Given an array of asteroids:

- Positive value -> moving right.
- Negative value -> moving left.
- Absolute value -> size.

When two asteroids moving toward each other collide:
- Smaller one explodes.
- If equal size, both explode.
- Asteroids moving in the same direction never collide.

Return the state of the asteroids after all collisions.

Approach:
Use a stack.

- Traverse the asteroids from left to right.
- Push asteroids that cannot currently collide.
- A collision is only possible when:
      stack top > 0
      current asteroid < 0
- Resolve collisions by repeatedly comparing the current
  asteroid with the stack top until:
    - one asteroid survives, or
    - both explode.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                top = stack[-1]

                if (top>0 and i>0) or (top<0 and i<0):
                    stack.append(i)

                elif top>0 and i<0 and top==abs(i):
                    stack.pop()

                elif top>0:

                        while stack and top>0 and top < abs(i):
                            stack.pop()
                            if stack:
                                top = stack[-1]

                            if top == abs(i):
                                stack.pop()
                                break
                        
                        else:
                            if top<0 or not stack:
                                stack.append(i)
                else:
                    stack.append(i)
        return stack
