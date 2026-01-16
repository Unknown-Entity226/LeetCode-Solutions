'''Problem Description:
Given a string s containing only the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
Approach:
- Use a stack to keep track of opening brackets.
- Iterate through each character in the string:
  - If it is an opening bracket, push it onto the stack.
  - If it is a closing bracket:
      - Check whether the stack is non-empty and the top of the stack
        matches the corresponding opening bracket.
      - If it matches, pop the stack.
      - Otherwise, return False immediately.
- After processing all characters, the string is valid only if
  the stack is empty.
Time Complexity:
O(n), where n is the length of the string.'''

class Solution(object):
    def isValid(self, s):
        open_bracs = ['(', '[', '{']
        close_bracs = [')', ']', '}']
        stack = []

        for ch in s:
            if ch in open_bracs:
                stack.append(ch)
            else:
                if stack and stack[-1] == open_bracs[close_bracs.index(ch)]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
