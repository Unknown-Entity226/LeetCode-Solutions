"""
Problem Description:
Given a string containing lowercase English letters and parentheses,
reverse the characters inside every pair of matching parentheses,
starting from the innermost pair. Return the resulting string without
any parentheses.

Approach:
- Use a stack to store characters and opening parentheses.
- When a closing parenthesis is encountered, pop characters from the
  stack until the matching opening parenthesis is found.
- The popped characters are already in reverse order, so store them
  in a temporary list.
- Remove the opening parenthesis and append the reversed characters
  back to the stack.
- Continue until the entire string has been processed.
- Join the remaining characters in the stack to obtain the result.

Time Complexity:
O(n)

Reason:
- Every character is pushed onto and popped from the stack a constant
  number of times.
- Therefore the total work is linear.

Space Complexity:
O(n)

Reason:
- The stack and temporary list can together contain O(n) characters
  in the worst case.
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stk = []

        for i in s:
            if i==")":
                rev = []

                while stk[-1]!="(":

                    rev.append(stk.pop())

                stk.pop() #remove the open bracket

                stk.extend(rev)
            
            else:
                stk.append(i)
                
        return "".join(stk)
