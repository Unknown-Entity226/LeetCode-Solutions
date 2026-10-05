"""
Problem Description:
Given a balanced parentheses string s, calculate its score using:
- "()" -> 1
- AB -> score(A) + score(B)
- (A) -> 2 * score(A)

Approach:
- Use a stack to store opening parentheses and already-computed scores.
- When '(' is encountered, push it onto the stack as a boundary marker.
- When ')' is encountered:
    1. If the top of the stack is '(', the current pair is "()",
       so remove '(' and push 1.
    2. Otherwise, there is a balanced expression inside the current
       parentheses. Pop and sum all scores until '(' is reached.
       Remove the '(' and push twice the inner score.
- After processing the entire string, the stack contains the scores
  of top-level balanced components.
- Sum these remaining scores to obtain the final answer.

Time Complexity:
O(n)

Reason:
- Every character is processed once.
- Every numeric score is pushed and popped at most once.

Space Complexity:
O(n)

Reason:
- In the worst case, the stack can contain O(n) opening parentheses
  or intermediate scores.
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack =[]

        for i in s:
            if i =="(": 
                stack.append("(")

            if i == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:

                    temp_sum = 0

                    while stack and stack[-1]!="(":
                        temp_sum += stack.pop()

                    stack.pop() # remove the (

                    stack.append(2*temp_sum)
        result = 0
        for  i in stack:
            result+=i
        return result


