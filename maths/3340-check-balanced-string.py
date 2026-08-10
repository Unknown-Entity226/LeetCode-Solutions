"""
Problem Description:
Given a string of digits, determine whether the sum of
digits at even indices is equal to the sum of digits at
odd indices.

Approach:
- Maintain one variable to store the difference between
  the even-index and odd-index digit sums.
- Add the digit at an even index.
- Subtract the digit at an odd index.
- The string is balanced if the final difference is 0.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0

        for i in range(len(num)):
            if not i%2:
                even+=int(num[i])
            else:
                even-=int(num[i])
        return even == 0
