"""
Problem Description:
Given a parentheses string s, find the minimum number of parentheses
that must be inserted to make the string valid.

Approach:
- Track the number of unmatched opening and closing parentheses.
- `left` represents the number of currently unmatched '(' characters.
- `right` temporarily tracks the number of ')' characters encountered.
- When ')' is encountered:
    - If there is a matching '(', cancel the pair.
    - Otherwise, the ')' is unmatched and requires an additional '('.
      Increment `need` for this insertion.
- After processing the string, any remaining unmatched '(' requires
  an additional ')' for each one.
- Return the total number of required insertions.

Time Complexity:
O(n)

Reason:
- The string is traversed exactly once.

Space Complexity:
O(1)

Reason:
- Only a constant number of counters are maintained.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        need = 0
        left =0
        right = 0

        for i in s:
            if i == ")":
                right +=1
                if right>left:
                    need += right -left
                    right -= 1

                else:
                    right -=1
                    left -=1
            
            else:
                left+=1

        if left!=0 or right!=0:
            need+=left+ right 

        return need

        
