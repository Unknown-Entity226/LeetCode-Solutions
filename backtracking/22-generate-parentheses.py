"""
Problem Description:
Given n pairs of parentheses, generate all possible combinations of
well-formed parentheses.

Approach:
- Use backtracking to construct the parenthesis string character by character.
- Track the number of opening and closing parentheses used.
- An opening parenthesis can always be added while fewer than n opening
  parentheses have been used.
- A closing parenthesis can only be added when the number of opening
  parentheses is greater than the number of closing parentheses.
- When 2*n parentheses have been placed, add the constructed string to
  the result.

Time Complexity:
O(C_n * n)

Reason:
- There are C_n valid combinations, where C_n is the nth Catalan number.
- Each valid combination contains 2*n characters and must be copied into
  the output.

Space Complexity:
O(n)

Reason:
- The recursion depth is at most 2*n.
- The temporary ans list contains at most 2*n characters.
- The returned output requires O(C_n * n) space.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        

        output = []

        def backtrack(left, right, ans):

            if (left + right) == 2*n:
                if left == right:
                    output.append("".join(ans))

                return 

            # left bracket
            curr_left= left
            curr_right = right
            ans.append("(")

            backtrack(left+1, right, ans)

            ans.pop()
            
            # right bracket
            if curr_left>curr_right:
                ans.append(")")
                backtrack(left, right+1, ans)
                ans.pop()

        backtrack(0,0, [])

        return output
